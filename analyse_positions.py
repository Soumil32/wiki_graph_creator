import graph_tool.all as gt
import pickle
import numpy as np

def main():
    print("OpenMP enabled: ", gt.openmp_enabled())
    print("OpenMP threads: ", gt.openmp_get_num_threads())
    g = gt.load_graph("graphs/my_graph_full_wo_properties.gt.gz")
    with open("pos_sfdp_full.pickle", "rb") as f:
        positions: gt.VertexPropertyMap = pickle.load(f)
    positions = g.own_property(positions)
    print("Number of positions loaded:", len(positions))
    print("Data type of positions:", type(positions))
    print("Data type of postions numpy:", type(""))
    print("Position of vertex 5312:", positions[5312])
    print("Biggest x coordinate:", positions[].max())
    print("Smallest y coordinate:", positions[:, 1].min())


if __name__ == "__main__":
    main()
