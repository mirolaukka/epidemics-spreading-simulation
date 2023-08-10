# SEIRD Epidemic Spreading Simulation

This repository contains an implementation of the SEIRD (Susceptible-Exposed-Infectious-Recovered-Dead) epidemic spreading simulation model. The simulation is implemented in Python and uses the Pygame library for visualization and the Matplotlib library for plotting the results.

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

The SEIRD model is an extension of the classic SIR model that includes additional states for exposed individuals and those who have died. This model is widely used to study the spread of epidemics, including the progression of infectious diseases through a population. This implementation of the SEIRD model takes into account various factors like infection transmission rate, recovery rate, incubation period, death rate, and more.

## Installation

To run the simulation, you need to have Python and the required libraries installed. You can use the provided `requirements.txt` file to install the necessary dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/mirolaukka/epidemics-spreading-simulation.git
cd epidemics-spreading-simulation/SEIRD
```

2. Open the `seird.py` file and customize the simulation parameters as needed.

3. Run the simulation:

```bash
python seird.py
```

4. The simulation will display either live visualization using Pygame or plot the simulation results using Matplotlib.

### SEIRD Simulation Parameters

You can modify the following arguments in the `SEIRD` class constructor to customize the simulation behavior. Default values are provided for each parameter.

- `population` (int): Total population size. (Default: 1500)
- `initial_infected` (int): Initial number of infected individuals. (Default: 15)
- `alpha` (float): Reduction in susceptibility for recovered individuals. (Default: 0.2)
- `beta` (float): Infection transmission rate. (Default: 0.1)
- `gamma` (float): Recovery rate. (Default: 0.005)
- `sigma` (float): Exposed to Infectious transition time in days. (Default: 10)
- `eta` (float): Death rate. (Default: 0.0005)
- `mu` (float): Recovery period. (Default: 120)
- `kappa` (int): Number of infections needed for immunity. (Default: 100)
- `proximity` (int): Proximity threshold for infection transmission. (Default: 30)
- `max_days` (int): Maximum number of simulation days. (Default: 1000)
- `width` (int): Width of the visualization screen. (Default: 800)
- `height` (int): Height of the visualization screen. (Default: 600)

## Customization

You can customize the simulation by adjusting the provided parameters. These parameters control various aspects of the simulation, such as population size, infection rate, recovery rate, and visualization dimensions.

### Example Usage

```python
from seird import SEIRD

# Customize simulation parameters
population_size = 1500  # Total population size
initial_infected = 15   # Initial number of infected individuals
alpha = 0.2             # Reduction in susceptibility for recovered individuals.
beta = 0.1              # Infection transmission rate
gamma = 0.005           # Recovery rate
sigma = 10              # Exposed to Infected rate in days
eta = 0.0005            # Death rate
mu = 120                # Recovered to Susceptible rate in days
kappa = 100             # Number of infections needed for immunity
proximity = 30          # Proximity threshold for infection transmission
max_days = 1000         # Maximum number of simulation days
width = 800             # Width of the visualization screen
height = 600            # Height of the visualization screen.

# Create an instance of the SEIRD simulation model
model = SEIRD(population=population_size, initial_infected=initial_infected,
              alpha=alpha, beta=beta, gamma=gamma, sigma=sigma,
              eta=eta, mu=mu, kappa=kappa, proximity=proximity,
              max_days=max_days, width=width, height=height)

# Run the simulation with live visualization
model.simulate(live_visualization=True)

# Plot the simulation results
model.plot_graph()
```

## Visualization

The simulation can be run with or without live visualization. In live visualization mode, individuals are represented as colored circles on the screen, showing their states (S, E, I, R, D, Immune) using various colors (Green, Yellow, Red, Blue, Gray, Purple).

## Testing

To run the default simulation values and visualize the model, you can use the provided `test_seird.py` file:

```bash
python test_seird.py
```

## License

This project is licensed under the [MIT License](LICENSE).