from seirs import SEIRS

simulation = SEIRS()

simulation.simulate(live_visualization=True)

simulation.plot_graph()
