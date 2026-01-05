from graph_tool.all import *
import time

def main():
    print("OpenMP enabled: ", openmp_enabled())
    print("OpenMP threads: ", openmp_get_num_threads())
    start = time.time()
    g = load_graph("my_graph_full.gt.gz")
    load_time = time.time()
    print("Time taken to load graph:", load_time - start, "seconds")
    # state: BlockState = minimize_nested_blockmodel_dl(g, state_args={"deg_corr": True}, multilevel_mcmc_args={"B_max": 100, "B_min": 5, "niter": 1, "cache_states": False})
    state: BlockState = minimize_blockmodel_dl(g, state=PPBlockState)
    blockmodel_time = time.time()
    print("Time taken to compute block model:", blockmodel_time - load_time, "seconds")
    # g.graph_properties["state"] = state
    end = time.time()
    print("Time taken to save graph with state:", end - blockmodel_time, "seconds")
    print("Total time taken:", end - start, "seconds")


if __name__ == "__main__":
    main()