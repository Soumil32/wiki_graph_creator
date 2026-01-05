from graph_tool.all import *
import time

def main():
    print("OpenMP enabled: ", openmp_enabled())
    print("OpenMP threads: ", openmp_get_num_threads())
    start = time.time()
    g = load_graph("my_graph.gt.gz")



if __name__ == "__main__":
    main()