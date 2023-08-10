import pygame
import random
import math
import matplotlib.pyplot as plt
import numpy as np


class Individual:
    """
    Represents an individual in the simulation.

    Args:
        state (str): The current state of the individual ('S' for susceptible, 'E' for exposed,
                     'I' for infected, 'R' for recovered).
        beta (float): The infection transmission rate.
        screen (pygame.Surface): The Pygame screen object for visualization (optional).
        width (int): The width of the simulation visualization (optional, default: 800).
        height (int): The height of the simulation visualization (optional, default: 600).

    Attributes:
        x (int): The x-coordinate of the individual.
        y (int): The y-coordinate of the individual.
        state (str): The current state of the individual.
        exposed_duration (int): The number of days an individual has been exposed.
        recovered_days (int): The number of days an individual has been in the recovered state.
        modified_beta (float): The adjusted infection transmission rate based on interactions.
        infection_count (int): Number of times the individual has been infected.
        COLOR_CODES (dict): Dictionary mapping states to RGB color codes.
        screen (pygame.Surface): The Pygame screen object for visualization.
    """

    def __init__(self, state, beta, screen=None, width: int = 800, height: int = 600):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.state = state
        self.exposed_duration = 0
        self.recovered_days = 0
        self.modified_beta = beta
        self.infection_count = 0
        self.COLOR_CODES = {
            'S': (0, 255, 0),       # Green
            'E': (255, 255, 0),     # Yellow
            'I': (255, 0, 0),       # Red
            'R': (0, 0, 255),       # Blue
            'D': (85, 85, 85),      # Gray
            'Immune': (252, 0, 230)  # Pink
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


class SEIRD:
    """
    Represents a simulation using the SEIRD (Susceptible-Exposed-Infectious-Recovered-Dead) model.

    Args:
        population (int): Total population size.
        initial_infected (int): Initial number of infected individuals.
        alpha (float): Proportion of infected becoming deceased.
        beta (float): Infection transmission rate.
        gamma (float): Recovery rate.
        sigma (float): Incubation period.
        eta (float): Death rate.
        mu (float): Recovery period.
        kappa (int): Number of infections needed for immunity.
        proximity (int): Proximity threshold for infection transmission.
        max_days (int): Maximum number of simulation days.
        width (int): Width of the simulation visualization.
        height (int): Height of the simulation visualization.

    Attributes:
        POPULATION_SIZE (int): Total population size.
        INITIAL_INFECTED (int): Initial number of infected individuals.
        PROXIMITY (int): Proximity threshold for infection transmission.
        MAX_DAYS (int): Maximum number of simulation days.
        ALPHA (float): Proportion of infected becoming deceased.
        BETA (float): Infection transmission rate.
        GAMMA (float): Recovery rate.
        SIGMA (float): Incubation period.
        ETA (float): Death rate.
        MU (float): Recovery period.
        KAPPA (int): Number of infections needed for immunity.
        individuals (list): List of Individual objects representing the population.
        susceptible_individuals (list): List of susceptible Individual objects.
        infected_individuals (list): List of infected Individual objects.
        day (int): Current simulation day.
        s_data (list): List to store susceptible population data for plotting.
        e_data (list): List to store exposed population data for plotting.
        i_data (list): List to store infected population data for plotting.
        r_data (list): List to store recovered population data for plotting.
        d_data (list): List to store deceased population data for plotting.
        immune_data (list): List to store immune population data for plotting.
        COLOR_CODES (dict): Dictionary mapping states to RGB color codes.
        WIDTH (int): Width of the simulation visualization.
        HEIGHT (int): Height of the simulation visualization.
    """

    def __init__(self,
                 population: int = 1500,
                 initial_infected: int = 15,
                 alpha: float = 0.2,
                 beta: float = 0.1,
                 gamma: float = 0.005,
                 sigma: float = 10,
                 eta: float = 0.0005,
                 mu: float = 120,
                 kappa: int = 100,
                 proximity: int = 30,
                 max_days: int = 1000,
                 width: int = 800,
                 height: int = 600):

        self.POPULATION_SIZE = population
        self.INITIAL_INFECTED = initial_infected
        self.PROXIMITY = proximity
        self.MAX_DAYS = max_days

        self.ALPHA = alpha
        self.BETA = beta
        self.GAMMA = gamma
        self.SIGMA = sigma
        self.ETA = eta
        self.MU = mu
        self.KAPPA = kappa

        self.individuals = []
        self.susceptible_individuals = []
        self.infected_individuals = []

        self.day = 0

        self.s_data, self.i_data, self.r_data, self.e_data, self.d_data, self.immune_data = [
        ], [], [], [], [], []

        self.COLOR_CODES = {
            'S': (0, 255, 0),       # Green
            'E': (255, 255, 0),     # Yellow
            'I': (255, 0, 0),       # Red
            'R': (0, 0, 255),       # Blue
            'D': (85, 85, 85),      # Gray
            'Immune': (252, 0, 230)  # Pink
        }

        # Pygame variables
        self.WIDTH = width
        self.HEIGHT = height

    def simulate(self, live_visualization: bool = False):
        """
        Run the SEIRD simulation.

        Args:
            live_visualization (bool): Whether to visualize the simulation in real-time using Pygame.

        This method simulates the spread of an epidemic using the SEIRD model. It updates the states of individuals
        and collects data for plotting.
        """

        if live_visualization:
            # Pygame setup
            pygame.init()

            screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
            pygame.display.set_caption('SEIRD Model Simulation')

        self.individuals = [Individual('S', self.BETA, screen=screen if live_visualization else None, width=self.WIDTH, height=self.HEIGHT)
                            for _ in range(self.POPULATION_SIZE)]

        self.infected_individuals = random.sample(
            self.individuals, self.INITIAL_INFECTED)

        for individual in self.infected_individuals:
            individual.state = 'I'

        if not live_visualization:
            while any((person.state == 'I' or person.state == 'E') for person in self.individuals) and self.day <= self.MAX_DAYS:
                self.day += 1

                for person in self.individuals:
                    if person.state == 'E':
                        person.exposed_duration += 1
                        if person.exposed_duration >= self.SIGMA:  # Exposed to Infectious transition
                            person.state = 'I'
                            person.exposed_duration = 0
                            person.infection_count += 1
                    elif person.state == 'I':
                        if random.random() < self.GAMMA:

                            if random.random() < self.ETA:
                                person.state = 'D'
                            else:
                                person.state = 'R'

                        elif random.random() < self.ETA:
                            person.state = 'D'
                        else:

                            person.modified_beta *= (1 - self.ALPHA)

                            for other_person in self.individuals:
                                if other_person.state == 'S':
                                    distance = person.distance_to(other_person)
                                    if distance <= self.PROXIMITY and random.random() < person.modified_beta:
                                        other_person.state = 'E'

                    elif person.state == 'R':

                        # If person has been infected self.KAPPA times, it's immune
                        if person.infection_count >= self.KAPPA:
                            person.state = 'Immune'
                        else:
                            person.recovered_days += 1
                            if person.recovered_days >= self.MU:
                                person.state = 'S'
                                person.recovered_days = 0

                self.s_data.append(
                    sum(person.state == "S" for person in self.individuals))
                self.e_data.append(
                    sum(person.state == "E" for person in self.individuals))
                self.i_data.append(
                    sum(person.state == "I" for person in self.individuals))
                self.r_data.append(
                    sum(person.state == "R" for person in self.individuals))
                self.d_data.append(
                    sum(person.state == "D" for person in self.individuals))

                if self.day % 10 == 0:
                    print(f"Day: {self.day}/{self.MAX_DAYS}")

        else:
            while any((person.state == 'I' or person.state == 'E') for person in self.individuals) and self.day <= self.MAX_DAYS:
                self.day += 1

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                # Set the background color to white (RGB: 255, 255, 255)
                screen.fill((255, 255, 255))

                for person in self.individuals:
                    if person.state == 'E':
                        person.exposed_duration += 1
                        if person.exposed_duration >= self.SIGMA:  # Exposed to Infectious transition
                            person.state = 'I'
                            person.exposed_duration = 0
                            person.infection_count += 1
                    elif person.state == 'I':
                        if random.random() < self.GAMMA:

                            if random.random() < self.ETA:
                                person.state = 'D'
                            else:
                                person.state = 'R'

                        elif random.random() < self.ETA:
                            person.state = 'D'
                        else:

                            person.modified_beta *= (1 - self.ALPHA)

                            for other_person in self.individuals:
                                if other_person.state == 'S':
                                    distance = person.distance_to(other_person)
                                    if distance <= self.PROXIMITY and random.random() < person.modified_beta:
                                        other_person.state = 'E'

                    elif person.state == 'R':

                        # If person has been infected self.KAPPA times, it's immune
                        if person.infection_count >= self.KAPPA:
                            person.state = 'Immune'
                        else:
                            person.recovered_days += 1
                            if person.recovered_days >= self.MU:
                                person.state = 'S'
                                person.recovered_days = 0

                # Draw individuals with updated states
                for person in self.individuals:
                    person.draw()

                susceptible_count = sum(
                    person.state == "S" for person in self.individuals)
                exposed_count = sum(
                    person.state == "E" for person in self.individuals)
                infected_count = sum(
                    person.state == "I" for person in self.individuals)
                recovered_count = sum(
                    person.state == "R" for person in self.individuals)
                dead_count = sum(
                    person.state == "D" for person in self.individuals)
                immune_count = sum(
                    person.state == 'Immune' for person in self.individuals)

                pygame.display.set_caption(
                    f'SEIRD Model Simulation - S:{susceptible_count} | E:{exposed_count} | I:{infected_count} | R:{recovered_count} | D: {dead_count} | Immune: {immune_count} | DAY: {self.day}')

                pygame.display.flip()

                self.s_data.append(susceptible_count)
                self.e_data.append(exposed_count)
                self.i_data.append(infected_count)
                self.r_data.append(recovered_count)
                self.d_data.append(dead_count)
                self.immune_data.append(immune_count)

                if self.day % 10 == 0:
                    print(f"Day: {self.day}/{self.MAX_DAYS}")

    def plot_graph(self):
        """
        Plot the simulation results using Matplotlib.

        This method creates a graph displaying the susceptible, exposed, infected, recovered, dead, and immune populations over time.
        """
        plt.style.use('seaborn-v0_8-whitegrid')

        s_color = tuple(c / 255.0 for c in self.COLOR_CODES['S'])
        e_color = tuple(c / 255.0 for c in self.COLOR_CODES['E'])
        i_color = tuple(c / 255.0 for c in self.COLOR_CODES['I'])
        r_color = tuple(c / 255.0 for c in self.COLOR_CODES['R'])
        d_color = tuple(c / 255.0 for c in self.COLOR_CODES['D'])
        immune_color = tuple(c / 255.0 for c in self.COLOR_CODES['Immune'])

        plt.plot(self.s_data, label='Susceptible', linewidth=2, color=s_color)
        plt.plot(self.e_data, label='Exposed', linewidth=2, color=e_color)
        plt.plot(self.i_data, label='Infected', linewidth=2, color=i_color)
        plt.plot(self.r_data, label='Recovered', linewidth=2, color=r_color)
        plt.plot(self.d_data, label='Dead', linewidth=2, color=d_color)
        plt.plot(self.immune_data, label='Immune',
                 linewidth=2, color=immune_color)
        plt.xlabel('Days')
        plt.ylabel('Population')
        plt.title(
            f'SEIRD Epidemic Spreading Simulation with Proximity\nAlpha={self.ALPHA}, Beta={self.BETA}, Gamma={self.GAMMA}, Sigma={self.SIGMA}, Mu={self.MU}\nEta={self.ETA}, Kappa={self.KAPPA}, proximity={self.PROXIMITY}, population_size={self.POPULATION_SIZE}, initial infected={self.INITIAL_INFECTED}')
        plt.legend()
        plt.grid(True)
        plt.show()
