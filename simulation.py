import pygame
import random
import math
import imageio

# Pygame setup
pygame.init()

# Window dimensions
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('SIR Model Simulation - S:0 I:0 R:0')
frames = []  # To store simulation frames for GIF


# SIR model parameters
BETA = 0.04       # Infection rate
GAMMA = 0.005     # Recovery rate
PROXIMITY = 30    # Transmission radius
POPULATION = 1000
INITIAL_INFECTED = 1

# Color codes
COLOR_CODES = {
    'S': (0, 255, 0),   # Green
    'I': (255, 0, 0),   # Red
    'R': (0, 0, 255)    # Blue
}


# Particle class representing individuals
class Individual:
    def __init__(self, state):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.state = state

    def draw(self):
        color = COLOR_CODES[self.state]
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), 5)

    def distance_to(self, other_individual):
        return math.sqrt((self.x - other_individual.x)**2 + (self.y - other_individual.y)**2)


def simulate_sir_model(population_size, initial_infected, beta, gamma, proximity):
    """
    Simulate the SIR model.

    Parameters:
        population_size (int): Total population size.
        initial_infected (int): Initial number of infected individuals.
        beta (float): Infection rate.
        gamma (float): Recovery rate.
        proximity (float): Transmission radius (proximity).

    Returns:
        List: A list of Individuals representing the final state of the population.
    """
    population_list = [Individual('S') for _ in range(population_size)]
    infected_individuals = random.sample(population_list, initial_infected)
    for individual in infected_individuals:
        individual.state = 'I'

    # Run the simulation until all individuals are recovered
    while any(person.state == 'I' for person in population_list):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Set the background color to white (RGB: 255, 255, 255)
        screen.fill((255, 255, 255))

        # Simulate one time step of the SIR model
        for person in population_list:
            if person.state == 'I':
                if random.random() < gamma:
                    person.state = 'R'
                else:
                    for other_person in population_list:
                        if other_person.state == 'S':
                            distance = person.distance_to(other_person)
                            if distance <= proximity and random.random() < beta:
                                other_person.state = 'I'

        # Draw individuals with updated states
        for person in population_list:
            person.draw()

        pygame.display.set_caption(
            f'SIR Model Simulation - I:{sum(person.state == "I" for person in population_list)}')

        frames.append(pygame.surfarray.array3d(screen))

        pygame.display.flip()

    return population_list


def create_sir_simulation_gif(frames, filename, frame_duration):
    """
    Create a GIF animation from the list of frames.

    Parameters:
        frames (List): A list of frames as NumPy arrays.
        filename (str): Name of the output GIF file.
        frame_duration (int): Milliseconds per frame for GIF.
    """
    imageio.mimsave(filename, frames, duration=frame_duration / 1000.0)
    print(f'GIF saved as {filename}')


def main():
    # SIR model simulation
    population_list = simulate_sir_model(
        POPULATION, INITIAL_INFECTED, BETA, GAMMA, PROXIMITY)

    # Save the frames as a GIF
    gif_filename = 'sir_simulation.gif'
    frame_duration = 100  # Milliseconds per frame for GIF
    create_sir_simulation_gif(frames, gif_filename, frame_duration)

    pygame.quit()


if __name__ == "__main__":
    main()
