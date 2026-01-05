import igraph as ig
import pickle


def main():
    g: ig.Graph = ig.load("my_graph.graphml.gz")
    print("graph vertex properties:", g.vs.attributes())
    print(g.summary(verbosity=0))
    print("Is simple:", g.is_simple())
    communities = g.community_leiden()
    # store the communities to disk as a list so that they can be loaded later
    print("communities:", len(communities))


if __name__ == "__main__":
    main()