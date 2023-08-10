# Epidemic Spreading Simulation (SIR, SEIRD, SEIRS)

This repository contains an epidemic spreading simulation project that implements three different models: SIR (Susceptible-Infectious-Recovered), SEIRD (Susceptible-Exposed-Infectious-Recovered-Deceased), and SEIRS (Susceptible-Exposed-Infectious-Recovered-Susceptible). These models are used to simulate the spread of infectious diseases within a population.

## Table of Contents

- [Introduction](#introduction)
- [Models](#models)
  - [SIR Model](#sir-model)
  - [SEIRD Model](#seird-model)
  - [SEIRS Model](#seirs-model)
- [Usage](#usage)
- [Requirements](#requirements)
- [License](#license)

## Introduction

In the field of epidemiology, understanding how diseases spread within a population is crucial for making informed decisions regarding public health interventions. This project provides implementations for three common epidemic models: SIR, SEIRD, and SEIRS. Each model builds upon the previous one by introducing new compartments to capture different stages of the disease progression.

## Models

### SIR Model

The SIR model divides the population into three compartments: susceptible (S), infectious (I), and recovered (R). It assumes that individuals who recover from the disease gain immunity and cannot be infected again during the simulation.

### SEIRD Model

The SEIRD model extends the SIR model by introducing an additional compartment for exposed (E) individuals. Exposed individuals are not yet infectious but have been exposed to the disease and may transition to the infectious state after a certain incubation period. This model also includes a compartment for deceased (D) individuals to track the fatalities due to the disease.

### SEIRS Model

The SEIRS model further extends the SEIRD model by allowing recovered individuals to transition back to the susceptible state. This accounts for the waning immunity over time and the possibility of reinfection, which is particularly relevant for diseases with short-lived immunity.

## Usage

Each model (SIR, SEIRD, SEIRS) has its own directory within this repository, containing the necessary scripts and files for running simulations. To run a simulation, navigate to the respective model's directory and follow the instructions provided in the associated `readme.md` file.

## Requirements

The simulations are implemented using Python and require certain dependencies to be installed. You can find the necessary Python packages listed in the `requirements.txt` file at the root of this repository. To install the required packages, you can use the following command:

```bash
pip install -r requirements.txt
```

## TODO

* Need to optimize SEIRD and SEIRS alot. Current runtime is around 60 seconds with default parameters.

## License

This project is licensed under the [MIT License](LICENSE).
