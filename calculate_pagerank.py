import graph_tool.all as gt
import pickle

def main():
    print("OpenMP enabled: ", gt.openmp_enabled())
    print("OpenMP threads: ", gt.openmp_get_num_threads())
    g = gt.load_graph("./graphs/my_graph_full_wo_properties.gt.gz")
    pagerank, num_iter = gt.pagerank(g, ret_iter=True, epsilon=1e-5)
    print("pagerank: ", pagerank)
    print("Number of iterations: ", num_iter)
    with open("pagerank_values_full.pickle", "wb") as f:
        pickle.dump(pagerank.a, f)
    print("Pagerank values saved to pagerank_values.pickle")


if __name__ == "__main__":
    main()