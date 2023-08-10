import pygame
import random
import math

import matplotlib.pyplot as plt

# Pygame setup
pygame.init()

# Window dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('SIR Model Simulation - S:0 I:0 R:0')

# SIR model parameters
BETA = 0.04       # Infection rate
GAMMA = 0.005     # Recovery rate
PROXIMITY = 30    # Transmission radius
POPULATION = 1500
INITIAL_INFECTED = 1

# Color codes
COLOR_CODES = {
    'S': (0, 255, 0),   # Green
    'I': (255, 0, 0),   # Red
    'R': (0, 0, 255)    # Blue
}

# Graph parameters
s_data, i_data, r_data = [], [], []

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
    population_list = [Individual('S') for _ in range(population_size)]
    infected_individuals = random.sample(population_list, initial_infected)
    for individual in infected_individuals:
        individual.state = 'I'

    day = 0  # Counter for days.

    # Run the simulation until all individuals are recovered
    while any(person.state == 'I' for person in population_list):
        day += 1
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

        susceptible_count = sum(
            person.state == "S" for person in population_list)
        infected_count = sum(
            person.state == "I" for person in population_list)
        recovered_count = sum(
            person.state == "R" for person in population_list)

        pygame.display.set_caption(
            f'SEIRS Model Simulation - S:{susceptible_count} | I:{infected_count} | R:{recovered_count} | DAY: {day}')

        pygame.display.flip()

        # Append data for the graph
        s_data.append(sum(person.state == "S" for person in population_list))
        i_data.append(sum(person.state == "I" for person in population_list))
        r_data.append(sum(person.state == "R" for person in population_list))


def plot_graph():
    plt.style.use('seaborn-v0_8-whitegrid')

    # Convert to (r, g, b) format
    s_color = tuple(c / 255.0 for c in COLOR_CODES['S'])
    # Convert to (r, g, b) format
    i_color = tuple(c / 255.0 for c in COLOR_CODES['I'])
    # Convert to (r, g, b) format
    r_color = tuple(c / 255.0 for c in COLOR_CODES['R'])

    plt.plot(s_data, label='Susceptible', linewidth=2, color=s_color)  # Green
    plt.plot(i_data, label='Infected', linewidth=2, color=i_color)    # Red
    plt.plot(r_data, label='Recovered', linewidth=2, color=r_color)  # Blue
    plt.xlabel('Days')
    plt.ylabel('Population')
    plt.title(
        f'SEIRS Epidemic Spreading Simulation with Proximity\nBeta={BETA}, Gamma={GAMMA}\nProximity={PROXIMITY}, Population={POPULATION}, Initial Infected={INITIAL_INFECTED}')
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    global s_data, i_data, r_data

    # SIR model simulation
    simulate_sir_model(POPULATION, INITIAL_INFECTED, BETA, GAMMA, PROXIMITY)

    plot_graph()

    pygame.quit()


if __name__ == "__main__":
    main()
