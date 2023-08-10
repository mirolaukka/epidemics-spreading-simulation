# SEIRS Epidemic Spreading Simulation

This repository contains an implementation of the SEIRS (Susceptible-Exposed-Infectious-Recovered-Susceptible) epidemic spreading simulation model. The simulation is implemented in Python and uses the Pygame library for visualization and the Matplotlib library for plotting the results.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
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

2. Open the `seirs.py` file and customize the simulation parameters as needed.

3. Run the simulation:

```bash
python seirs.py
```

4. The simulation will display either live visualization using Pygame or plot the simulation results using Matplotlib.

### SEIRS Simulation Parameters

You can modify the following arguments in the `SEIRS` class constructor to customize the simulation behavior. Default values are provided for each parameter.

- `population` (int): Total population size. (Default: 1500)
- `initial_infected` (int): Initial number of infected individuals. (Default: 15)
- `alpha` (float): Reduction in susceptibility for recovered individuals. (Default: 0.2)
- `beta` (float): Infection transmission rate. (Default: 0.1)
- `gamma` (float): Recovery rate. (Default: 0.005)
- `sigma` (float): Exposed to Infectious transition time. (Default: 10)
- `mu` (float): Recovery time. (Default: 120)
- `proximity` (int): Maximum distance for infection transmission. (Default: 30)
- `max_days` (int): Maximum number of simulation days. (Default: 1000)
- `width` (int): Width of the visualization screen. (Default: 800)
- `height` (int): Height of the visualization screen. (Default: 600)

### Example Usage

```python
from seirs import SEIRS

# Customize simulation parameters
population_size = 1500
initial_infected = 15
alpha = 0.2
beta = 0.1
gamma = 0.005
sigma = 10
mu = 120
proximity = 30
max_days = 1000
width = 800
height = 600

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


## License

This project is licensed under the [MIT License](LICENSE).
