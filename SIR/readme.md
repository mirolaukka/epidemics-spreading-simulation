# SIR Epidemic Spreading Simulation

This repository contains an implementation of the SIR (Susceptible-Infectious-Recovered) epidemic spreading simulation model. The simulation is implemented in Python and utilizes the Pygame library for visualization and the Matplotlib library for plotting the results.

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

The SIR model is a classic epidemic spreading simulation model that divides the population into three compartments: susceptible (S), infectious (I), and recovered (R). The simulation tracks the dynamics of disease spread by modeling transitions between these compartments. This implementation incorporates features like infection transmission rate, recovery rate, and proximity for transmission.

## Installation

To run the simulation, you need to have Python and the required libraries installed. You can use the provided `requirements.txt` file to install the necessary dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/mirolaukka/epidemics-spreading-simulation.git
cd epidemics-spreading-simulation/SIR
```

2. Run the simulation test file or see [Example Usage](#example-usage) for more information:

```bash
python test_sir.py
```

4. The simulation will either display live visualization using Pygame or plot the simulation results using Matplotlib.

### SIR Simulation Parameters

You can modify the following arguments in the `SIR` class constructor to customize the simulation behavior. Default values are provided for each parameter.

- `population` (int): Total population size. (Default: 1500)
- `initial_infected` (int): Initial number of infected individuals. (Default: 15)
- `beta` (float): Infection rate. (Default: 0.1)
- `gamma` (float): Recovery rate. (Default: 0.005)
- `proximity` (int): Maximum distance for infection transmission. (Default: 30)
- `max_days` (int): Maximum number of simulation days. (Default: 1000)
- `width` (int): Width of the visualization screen. (Default: 800)
- `height` (int): Height of the visualization screen. (Default: 600)

## Customization

You can customize the simulation by adjusting the provided parameters. These parameters control various aspects of the simulation, such as population size, infection rate, recovery rate, and visualization dimensions.

## Example Usage

```python
from sir import SIR

# Customize simulation parameters
population_size = 1500  # Total population size
initial_infected = 15   # Initial number of infected individuals
beta = 0.1              # Infection transmission rate
gamma = 0.005           # Recovery rate
proximity = 30          # Proximity threshold for infection transmission
max_days = 1000         # Maximum number of simulation days
width = 800             # Width of the visualization screen
height = 600            # Height of the visualization screen.

# Create an instance of the SIR simulation model
model = SIR(population=population_size, initial_infected=initial_infected,
            beta=beta, gamma=gamma, proximity=proximity, max_days=max_days,
            width=width, height=height)

# Run the simulation with live visualization
model.simulate(live_visualization=True)

# Plot the simulation results
model.plot_graph()
```

## Visualization

The simulation can be run with or without live visualization. In live visualization mode, individuals are represented as colored circles on the screen, showing their states (S, I, R) (Green, Red, Blue).


## Testing

To run the default simulation values and visualize the model, you can use the provided `test_sir.py` file:

```bash
python test_sir.py
```

## License

This project is licensed under the [MIT License](LICENSE).