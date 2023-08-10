from seird import SEIRD


simulation = SEIRD()
simulation.simulate(live_visualization=True)
simulation.plot_graph()
