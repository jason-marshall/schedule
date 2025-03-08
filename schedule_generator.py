import networkx as nx
import matplotlib.pyplot as plt

class Schedule:
    def __init__(self):
        self.graph = nx.DiGraph()

    def visualize(self):
        labels = {n: str(n) + '; duration = ' + str(self.graph.nodes[n]['weight']) for n in self.graph.nodes}
        colors = [self.graph.nodes[n]['color'] for n in self.graph.nodes]
        nx.draw(self.graph, with_labels=True, labels=labels, node_color=colors)

        #show the graph
        plt.show()

def main():
    schedule = Schedule()
    print("Initialized Schedule with an empty graph:", schedule.graph)
    schedule.graph.add_node(0,weight=10, color='green')
    schedule.graph.add_node(1,weight=20, color='red')
    schedule.graph.add_edge(0,1,duration=10)
    schedule.visualize()

if __name__ == "__main__":
    main()