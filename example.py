import pygraphviz as pgv

def create_complete_graph_svg(output_file):
    # Create a new directed graph
    G = pgv.AGraph(strict=False, directed=True)

    # Set default node style: square, rounded corners, filled light blue
    G.node_attr.update(shape='rect', style='rounded,filled', fillcolor='#add8e6', color='#3399cc')

    # Add nodes
    nodes = ['A', 'B', 'C', 'D']
    for node in nodes:
        G.add_node(node)

    # Add edges between all pairs of nodes (complete graph)
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if i != j:
                G.add_edge(nodes[i], nodes[j])

    # Draw the graph to an SVG file
    G.layout(prog='circo')
    G.draw(output_file)

if __name__ == "__main__":
    create_complete_graph_svg("graph.svg")
