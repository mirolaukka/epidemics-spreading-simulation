import pygame
import random
import math
import matplotlib.pyplot as plt


# Window dimensions
width, height = 800, 600


class Individual:
    """
    Represents an individual in the SIR model simulation.

    This class encapsulates the attributes and methods associated with an individual
    in the simulation, including its position, state (S, E, I, R), and visualization.

    Attributes:
        x (int): The x-coordinate of the individual's position.
        y (int): The y-coordinate of the individual's position.
        state (str): The state of the individual (S, E, I, R).
        screen (pygame.Surface, optional): Pygame screen to draw the individual. Defaults to None.

    Methods:
        draw(): Draw the individual as a colored circle on the Pygame screen.
        distance_to(other_individual): Calculate the Euclidean distance to another individual.
    """

    def __init__(self, state, screen=None):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.state = state
        self.COLOR_CODES = {
            'S': (0, 255, 0),   # Green
            'E': (255, 255, 0),  # Yellow
            'I': (255, 0, 0),   # Red
            'R': (0, 0, 255)    # Blue
        }
        self.screen = screen

    def draw(self):
        """
        Draw the individual as a colored circle on the Pygame screen.

        This method uses the Pygame screen object and the individual's state to determine the color of the circle.
        """
        color = self.COLOR_CODES[self.state]
        pygame.draw.circle(self.screen, color, (int(self.x), int(self.y)), 5)

    def distance_to(self, other_individual):
        """
        Calculate the Euclidean distance to another individual.

        Args:
            other_individual (Individual): The other individual to calculate the distance to.

        Returns:
            float: The Euclidean distance between this individual and the other individual.
        """
        return math.sqrt((self.x - other_individual.x)**2 + (self.y - other_individual.y)**2)


class SIR:
    """
    Represents the SIR model simulation.

    This class manages the SIR model simulation, including population dynamics, infection spread,
    recovery, and visualization.

    Args:
        population (int, optional): Total population size.
        initial_infected (int, optional): Initial number of infected individuals.
        beta (float, optional): Infection rate.
        gamma (float, optional): Recovery rate.
        proximity (int, optional): Proximity threshold for infection.
        max_days (int, optional): Maximum simulation days.
        width (int, optional): Width of the simulation window.
        height (int, optional): Height of the simulation window.

    Attributes:
        POPULATION_SIZE (int): Total population size.
        INITIAL_INFECTED (int): Initial number of infected individuals.
        PROXIMITY (int): Maximum distance for infection transmission.
        MAX_DAYS (int): Maximum number of simulation days.
        BETA (float): Infection transmission rate.
        GAMMA (float): Recovery rate.
        individuals (list): List of Individual instances representing the population.
        infected_individuals (list): List of initially infected Individual instances.
        day (int): Current simulation day.
        s_data (list): List of susceptible population counts for each day.
        i_data (list): List of infected population counts for each day.
        r_data (list): List of recovered population counts for each day.
        COLOR_CODES (dict): Dictionary mapping states to RGB color codes.
        WIDTH (int): Width of the visualization screen.
        HEIGHT (int): Height of the visualization screen.

    Methods:
        simulate(live_visualization: bool = False): Run the SEIRS simulation.
        plot_graph(): Plot the simulation results using Matplotlib.
    """

    def __init__(self,
                 population: int = 1500,
                 initial_infected: int = 15,
                 beta: float = 0.1,
                 gamma: float = 0.005,
                 proximity: int = 30,
                 max_days: int = 1000,
                 width: int = 800,
                 height: int = 600):

        self.POPULATION_SIZE = population
        self.INITIAL_INFECTED = initial_infected
        self.PROXIMITY = proximity
        self.MAX_DAYS = max_days

        self.BETA = beta
        self.GAMMA = gamma

        self.individuals = []
        self.infected_individuals = []

        self.day = 0

        self.s_data, self.i_data, self.r_data = [], [], []

        self.COLOR_CODES = {
            'S': (0, 255, 0),   # Green
            'E': (255, 255, 0),  # Yellow
            'I': (255, 0, 0),   # Red
            'R': (0, 0, 255)    # Blue
        }

        # Pygame variables
        self.WIDTH = width
        self.HEIGHT = height

    def simulate(self, live_visualization: bool = False):
        """
        Run the SIR simulation.

        Args:
            live_visualization (bool, optional): Whether to show live visualization using Pygame. Defaults to False.
        """
        if not live_visualization:

            self.individuals = [Individual('S')
                                for _ in range(self.POPULATION_SIZE)]

            self.infected_individuals = random.sample(
                self.individuals, self.INITIAL_INFECTED)

            for individual in self.infected_individuals:
                individual.state = 'I'

            while any(person.state == 'I' for person in self.individuals) and self.day <= self.MAX_DAYS:
                self.day += 1
                for person in self.individuals:
                    if person.state == 'I':
                        if random.random() < self.GAMMA:
                            person.state = 'R'
                        else:
                            for other_person in self.individuals:
                                if other_person.state == 'S':
                                    distance = person.distance_to(
                                        other_person)
                                    if distance <= self.PROXIMITY and random.random() < self.BETA:
                                        other_person.state = 'I'

                self.s_data.append(
                    sum(person.state == "S" for person in self.individuals))
                self.i_data.append(
                    sum(person.state == "I" for person in self.individuals))
                self.r_data.append(
                    sum(person.state == "R" for person in self.individuals))

                if self.day % 10 == 0:
                    print(f"Day: {self.day}/{self.MAX_DAYS}")

        else:
            # Pygame setup
            pygame.init()

            screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
            pygame.display.set_caption('SIR Model Simulation')

            self.individuals = [Individual('S', screen)
                                for _ in range(self.POPULATION_SIZE)]

            self.infected_individuals = random.sample(
                self.individuals, self.INITIAL_INFECTED)

            for individual in self.infected_individuals:
                individual.state = 'I'

            while any(person.state == 'I' for person in self.individuals) and self.day <= self.MAX_DAYS:
                self.day += 1

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                # Set the background color to white (RGB: 255, 255, 255)
                screen.fill((255, 255, 255))

                for person in self.individuals:
                    if person.state == 'I':
                        if random.random() < self.GAMMA:
                            person.state = 'R'
                        else:

                            for other_person in self.individuals:
                                if other_person.state == 'S':
                                    distance = person.distance_to(
                                        other_person)
                                    if distance <= self.PROXIMITY and random.random() < self.BETA:
                                        other_person.state = 'I'

                # Draw individuals with updated states
                for person in self.individuals:
                    person.draw()

                susceptible_count = sum(
                    person.state == "S" for person in self.individuals)
                infected_count = sum(
                    person.state == "I" for person in self.individuals)
                recovered_count = sum(
                    person.state == "R" for person in self.individuals)

                pygame.display.set_caption(
                    f'SIR Model Simulation - S:{susceptible_count} | I:{infected_count} | R:{recovered_count} | DAY: {self.day}')

                pygame.display.flip()

                self.s_data.append(susceptible_count)
                self.i_data.append(infected_count)
                self.r_data.append(recovered_count)

                if self.day % 10 == 0:
                    print(f"Day: {self.day}/{self.MAX_DAYS}")

    def plot_graph(self):
        """
        Plot graphs of susceptible, infected, and recovered individuals over days.
        """
        plt.style.use('seaborn-v0_8-whitegrid')

        s_color = tuple(c / 255.0 for c in self.COLOR_CODES['S'])
        i_color = tuple(c / 255.0 for c in self.COLOR_CODES['I'])
        r_color = tuple(c / 255.0 for c in self.COLOR_CODES['R'])

        plt.plot(self.s_data, label='Susceptible', linewidth=2, color=s_color)
        plt.plot(self.i_data, label='Infected', linewidth=2, color=i_color)
        plt.plot(self.r_data, label='Recovered', linewidth=2, color=r_color)
        plt.xlabel('Days')
        plt.ylabel('Population')
        plt.title(
            f'SIR Epidemic Spreading Simulation with Proximity\nBeta={self.BETA}, Gamma={self.GAMMA}\nProximity={self.PROXIMITY}, Population_size={self.POPULATION_SIZE}, Initial infected={self.INITIAL_INFECTED}')
        plt.legend()
        plt.grid(True)
        plt.show()
