import pygame
import random
import math
import matplotlib.pyplot as plt


class Individual:
    """
    Represents an individual in the simulation.

    Args:
        state (str): The current state of the individual ('S' for susceptible, 'E' for exposed,
                     'I' for infected, 'R' for recovered).
        beta (float): The infection transmission rate.
        screen (pygame.Surface): The Pygame screen object for visualization (optional).

    Attributes:
        x (int): The x-coordinate of the individual.
        y (int): The y-coordinate of the individual.
        state (str): The current state of the individual.
        exposed_duration (int): The number of days an individual has been exposed.
        recovered_days (int): The number of days an individual has been in the recovered state.
        modified_beta (float): The adjusted infection transmission rate based on interactions.
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
        self.COLOR_CODES = {
            "S": (0, 255, 0),  # Green
            "E": (255, 255, 0),  # Yellow
            "I": (255, 0, 0),  # Red
            "R": (0, 0, 255),  # Blue
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
        return math.sqrt(
            (self.x - other_individual.x) ** 2 + (self.y - other_individual.y) ** 2
        )


class SEIRS:
    """
    Represents the SEIRS epidemic spreading simulation.

    Args:
        population (int): Total population size.
        initial_infected (int): Initial number of infected individuals.
        alpha (float): Reduction in susceptibility for recovered individuals.
        beta (float): Infection transmission rate.
        gamma (float): Recovery rate.
        sigma (float): Exposed to Infectious transition time in days.
        mu (float): Recovery time in days.
        proximity (int): Maximum distance for infection transmission.
        max_days (int): Maximum number of simulation days.
        width (int): Width of the visualization screen.
        height (int): Height of the visualization screen.

    Attributes:
        POPULATION_SIZE (int): Total population size.
        INITIAL_INFECTED (int): Initial number of infected individuals.
        PROXIMITY (int): Maximum distance for infection transmission.
        MAX_DAYS (int): Maximum number of simulation days.
        ALPHA (float): Reduction in susceptibility for recovered individuals.
        BETA (float): Infection transmission rate.
        GAMMA (float): Recovery rate.
        SIGMA (float): Exposed to Infectious transition time in days.
        MU (float): Recovery time in days.
        individuals (list): List of Individual instances representing the population.
        infected_individuals (list): List of initially infected Individual instances.
        day (int): Current simulation day.
        s_data (list): List of susceptible population counts for each day.
        i_data (list): List of infected population counts for each day.
        r_data (list): List of recovered population counts for each day.
        e_data (list): List of exposed population counts for each day.
        COLOR_CODES (dict): Dictionary mapping states to RGB color codes.
        WIDTH (int): Width of the visualization screen.
        HEIGHT (int): Height of the visualization screen.

    Methods:
        simulate(live_visualization: bool = False): Run the SEIRS simulation.
        plot_graph(): Plot the simulation results using Matplotlib.
    """

    def __init__(
        self,
        population: int = 1500,
        initial_infected: int = 15,
        alpha: float = 0.2,
        beta: float = 0.1,
        gamma: float = 0.005,
        sigma: float = 10,
        mu: float = 120,
        proximity: int = 30,
        max_days: int = 1000,
        width: int = 800,
        height: int = 600,
    ):
        self.POPULATION_SIZE = population
        self.INITIAL_INFECTED = initial_infected
        self.PROXIMITY = proximity
        self.MAX_DAYS = max_days

        self.ALPHA = alpha
        self.BETA = beta
        self.GAMMA = gamma
        self.SIGMA = sigma
        self.MU = mu

        self.individuals = []
        self.infected_individuals = []

        self.day = 0

        self.s_data, self.i_data, self.r_data, self.e_data = [], [], [], []

        self.COLOR_CODES = {
            "S": (0, 255, 0),  # Green
            "E": (255, 255, 0),  # Yellow
            "I": (255, 0, 0),  # Red
            "R": (0, 0, 255),  # Blue
        }

        # Pygame variables
        self.WIDTH = width
        self.HEIGHT = height

    def simulate(self, live_visualization: bool = False):
        """
        Run the SEIRS simulation.

        Args:
            live_visualization (bool): Whether to visualize the simulation in real-time using Pygame.

        This method simulates the spread of an epidemic using the SEIRS model. It updates the states of individuals
        and collects data for plotting.
        """

        if live_visualization:
            # Pygame setup
            pygame.init()

            screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
            pygame.display.set_caption("SEIRS Model Simulation")

        self.individuals = [
            Individual(
                "S",
                self.BETA,
                screen=screen if live_visualization else None,
                width=self.WIDTH,
                height=self.HEIGHT,
            )
            for _ in range(self.POPULATION_SIZE)
        ]

        self.infected_individuals = random.sample(
            self.individuals, self.INITIAL_INFECTED
        )

        for individual in self.infected_individuals:
            individual.state = "I"

        if not live_visualization:
            while (
                any(
                    (person.state == "I" or person.state == "E")
                    for person in self.individuals
                )
                and self.day <= self.MAX_DAYS
            ):
                self.day += 1
                for person in self.individuals:
                    if person.state == "E":
                        person.exposed_duration += 1
                        if (
                            person.exposed_duration >= self.SIGMA
                        ):  # Exposed to Infectious transition
                            person.state = "I"
                            person.exposed_duration = 0
                    elif person.state == "I":
                        if random.random() < self.GAMMA:
                            person.state = "R"
                        else:
                            person.modified_beta *= 1 - self.ALPHA

                            for other_person in self.individuals:
                                if other_person.state == "S":
                                    distance = person.distance_to(other_person)
                                    if (
                                        distance <= self.PROXIMITY
                                        and random.random() < person.modified_beta
                                    ):
                                        other_person.state = "E"

                    elif person.state == "R":
                        person.recovered_days += 1
                        if person.recovered_days >= self.MU:
                            person.state = "S"
                            person.recovered_days = 0

                self.s_data.append(
                    sum(person.state == "S" for person in self.individuals)
                )
                self.i_data.append(
                    sum(person.state == "I" for person in self.individuals)
                )
                self.r_data.append(
                    sum(person.state == "R" for person in self.individuals)
                )
                self.e_data.append(
                    sum(person.state == "E" for person in self.individuals)
                )

                if self.day % 10 == 0:
                    print(f"Day: {self.day}/{self.MAX_DAYS}")

        else:
            while (
                any(
                    (person.state == "I" or person.state == "E")
                    for person in self.individuals
                )
                and self.day <= self.MAX_DAYS
            ):
                self.day += 1

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                # Set the background color to white (RGB: 255, 255, 255)
                screen.fill((255, 255, 255))

                for person in self.individuals:
                    if person.state == "E":
                        person.exposed_duration += 1
                        if (
                            person.exposed_duration >= self.SIGMA
                        ):  # Exposed to Infectious transition
                            person.state = "I"
                            person.exposed_duration = 0
                    elif person.state == "I":
                        if random.random() < self.GAMMA:
                            person.state = "R"
                        else:
                            person.modified_beta *= 1 - self.ALPHA

                            for other_person in self.individuals:
                                if other_person.state == "S":
                                    distance = person.distance_to(other_person)
                                    if (
                                        distance <= self.PROXIMITY
                                        and random.random() < person.modified_beta
                                    ):
                                        other_person.state = "E"

                    elif person.state == "R":
                        person.recovered_days += 1
                        if person.recovered_days >= self.MU:
                            person.state = "S"
                            person.recovered_days = 0

                # Draw individuals with updated states
                for person in self.individuals:
                    person.draw()

                susceptible_count = sum(
                    person.state == "S" for person in self.individuals
                )
                infected_count = sum(person.state == "I" for person in self.individuals)
                exposed_count = sum(person.state == "E" for person in self.individuals)
                recovered_count = sum(
                    person.state == "R" for person in self.individuals
                )

                pygame.display.set_caption(
                    f"SEIRS Model Simulation - S:{susceptible_count} | I:{infected_count} | E:{exposed_count} | R:{recovered_count} | DAY: {self.day}"
                )

                pygame.display.flip()

                self.s_data.append(susceptible_count)
                self.i_data.append(infected_count)
                self.r_data.append(exposed_count)
                self.e_data.append(recovered_count)

                if self.day % 10 == 0:
                    print(f"Day: {self.day}/{self.MAX_DAYS}")

    def plot_graph(self):
        """
        Plot the simulation results using Matplotlib.

        This method creates a graph displaying the susceptible, infected, recovered, and exposed populations over time.
        """
        plt.style.use("seaborn-v0_8-whitegrid")

        s_color = tuple(c / 255.0 for c in self.COLOR_CODES["S"])
        i_color = tuple(c / 255.0 for c in self.COLOR_CODES["I"])
        r_color = tuple(c / 255.0 for c in self.COLOR_CODES["R"])
        e_color = tuple(c / 255.0 for c in self.COLOR_CODES["E"])

        plt.plot(self.s_data, label="Susceptible", linewidth=2, color=s_color)
        plt.plot(self.i_data, label="Infected", linewidth=2, color=i_color)
        plt.plot(self.r_data, label="Recovered", linewidth=2, color=r_color)
        plt.plot(self.e_data, label="Exposed", linewidth=2, color=e_color)
        plt.xlabel("Days")
        plt.ylabel("Population")
        plt.title(
            f"SEIRS Epidemic Spreading Simulation with Proximity\nAlpha={self.ALPHA}, Beta={self.BETA}, Gamma={self.GAMMA}, Sigma={self.SIGMA}, Mu={self.MU}\nproximity={self.PROXIMITY}, population_size={self.POPULATION_SIZE}, initial infected={self.INITIAL_INFECTED}"
        )
        plt.legend()
        plt.grid(True)
        plt.show()
