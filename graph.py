import numpy as np
import matplotlib.pyplot as plt

BETA = 0.04       # Infection rate
GAMMA = 0.005     # Recovery rate
PROXIMITY = 0.6   # Transmission radius (proximity)
POPULATION = 1000
INITIAL_INFECTED = 1
DAYS = 1500


def sir_model(beta, gamma, proximity, population, initial_infected, days):
    """
    Simulate the SIR epidemic spreading model.

    Parameters:
        beta (float): Infection rate.
        gamma (float): Recovery rate.
        proximity (float): Transmission radius (proximity).
        population (int): Total population size.
        initial_infected (int): Initial number of infected individuals.
        days (int): Number of days to simulate.

    Returns:
        Tuple: Three lists representing the susceptible, infected, and recovered populations over time.
    """
    if beta <= 0 or gamma <= 0 or proximity <= 0 or population <= 0 or initial_infected < 0 or days <= 0:
        raise ValueError(
            "All parameters should be positive numbers, and days should be greater than zero.")

    susceptible = population - initial_infected
    infected = initial_infected
    recovered = 0

    s_list = [susceptible]
    i_list = [infected]
    r_list = [recovered]

    for day in range(days):
        contacts = beta * susceptible * infected / population
        new_infected = contacts * proximity
        new_recovered = gamma * infected

        susceptible -= new_infected
        infected += new_infected - new_recovered
        recovered += new_recovered

        s_list.append(susceptible)
        i_list.append(infected)
        r_list.append(recovered)

    return s_list, i_list, r_list


def main():
    """
    Main function to run the SIR epidemic spreading simulation with predefined parameters and plot the results.
    """
    s, i, r = sir_model(BETA, GAMMA, PROXIMITY,
                        POPULATION, INITIAL_INFECTED, DAYS)

    plt.style.use('seaborn-v0_8-whitegrid')
    plt.plot(s, label='Susceptible', linewidth=2)
    plt.plot(i, label='Infected', linewidth=2)
    plt.plot(r, label='Recovered', linewidth=2)
    plt.xlabel('Days')
    plt.ylabel('Population')
    plt.title(
        f'SIR Epidemic Spreading Simulation with Proximity\nBeta={BETA}, Gamma={GAMMA}, Proximity={PROXIMITY}')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
