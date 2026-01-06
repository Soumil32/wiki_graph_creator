from graph_tool.all import *
import time
import pickle

def main():
    openmp_set_num_threads(2)
    print("OpenMP enabled: ", openmp_enabled())
    print("OpenMP threads: ", openmp_get_num_threads())
    start = time.time()
    g = load_graph("my_graph_full_wo_properties.gt.gz")
    load_time = time.time()
    print("Time taken to load graph:", load_time - start, "seconds")
    # state: BlockState = minimize_nested_blockmodel_dl(g, state_args={"deg_corr": True}, multilevel_mcmc_args={"B_max": 100, "B_min": 5, "niter": 1, "cache_states": False})
    state: BlockState = minimize_blockmodel_dl(g, state=PPBlockState, multilevel_mcmc_args={"parallel": True, "cache_states": False, "B_min": 5, "B_max": 100})
    blockmodel_time = time.time()
    print("Time taken to compute block model:", blockmodel_time - load_time, "seconds")
    with open("state.pickle", "wb") as f:
        pickle.dump(state, f)
    end = time.time()
    print("Time taken to save graph with state:", end - blockmodel_time, "seconds")
    print("Total time taken:", end - start, "seconds")


if __name__ == "__main__":
    main()
