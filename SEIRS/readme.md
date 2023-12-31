# SEIRS Epidemic Spreading Simulation

This repository contains an implementation of the SEIRS (Susceptible-Exposed-Infectious-Recovered-Susceptible) epidemic spreading simulation model. The simulation is implemented in Python and uses the Pygame library for visualization and the Matplotlib library for plotting the results.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Example Usage](#example-usage)
- [Visualization](#visualization)
- [Testing](#testing)
- [License](#license)

## Introduction

The SEIRS model is a further extension of the SEIRD (Susceptible-Exposed-Infectious-Recovered-Deceased) model. It introduces an additional state transition, allowing recovered individuals to transition back to the susceptible state. This accounts for the waning immunity over time and the possibility of reinfection, which is particularly relevant for diseases with short-lived immunity.

The simulation involves a population of individuals a defined area. Individuals can transition between different states: susceptible, exposed, infectious, recovered, and susceptible again. The simulation accounts for factors like infection transmission rate, recovery rate, and proximity for transmission.

## Installation

To run the simulation, you need to have Python and the required libraries installed. You can use the provided `requirements.txt` file to install the necessary dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/mirolaukka/epidemics-spreading-simulation.git
cd epidemics-spreading-simulation/SEIRS
```

2. Run the simulation test file or see [Example Usage](#example-usage) for more information:

```bash
python test_seirs.py
```

4. The simulation will display either live visualization using Pygame or plot the simulation results using Matplotlib.

### SEIRS Simulation Parameters

You can modify the following arguments in the `SEIRS` class constructor to customize the simulation behavior. Default values are provided for each parameter.

- `population` (int): Total population size. (Default: 1500)
- `initial_infected` (int): Initial number of infected individuals. (Default: 15)
- `alpha` (float): Reduction in susceptibility for recovered individuals. (Default: 0.2)
- `beta` (float): Infection transmission rate. (Default: 0.1)
- `gamma` (float): Recovery rate. (Default: 0.005)
- `sigma` (float): Exposed to Infectious transition time in days. (Default: 10)
- `mu` (float): Recovery time in days. (Default: 120)
- `proximity` (int): Maximum distance for infection transmission. (Default: 30)
- `max_days` (int): Maximum number of simulation days. (Default: 1000)
- `width` (int): Width of the visualization screen. (Default: 800)
- `height` (int): Height of the visualization screen. (Default: 600)

## Customization

You can customize the simulation by adjusting the provided parameters. These parameters control various aspects of the simulation, such as population size, infection rate, recovery rate, and visualization dimensions.

### Example Usage

```python
from seirs import SEIRS

# Customize simulation parameters
population_size = 1500  # Total population size
initial_infected = 15   # Initial number of infected individuals
alpha = 0.2             # Reduction in susceptibility for recovered individuals.
beta = 0.1              # Infection transmission rate
gamma = 0.005           # Recovery rate
sigma = 10              # Exposed to Infected rate in days
mu = 120                # Recovered to Susceptible rate in days
proximity = 30          # Proximity threshold for infection transmission
max_days = 1000         # Maximum number of simulation days
width = 800             # Width of the visualization screen
height = 600            # Height of the visualization screen.

# Create an instance of the SEIRS simulation model
model = SEIRS(population=population_size, initial_infected=initial_infected,
              alpha=alpha, beta=beta, gamma=gamma, sigma=sigma,
              mu=mu, proximity=proximity, max_days=max_days,
              width=width, height=height)

# Run the simulation with live visualization
model.simulate(live_visualization=True)

# Plot the simulation results
model.plot_graph()
```

## Visualization

The simulation can be run with or without live visualization. In live visualization mode, individuals are represented as colored circles on the screen, showing their states (S, E, I, R) (Green, Yellow, Red, Blue).



## Testing

To run the default simulation values and visualize the model, you can use the provided `test_seirs.py` file:

```bash
python test_seirs.py
```

## License

This project is licensed under the [MIT License](LICENSE).
