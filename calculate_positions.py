from graph_tool.all import *
import pickle
import time

def main():
    openmp_set_num_threads(1)
    print("OpenMP enabled: ", openmp_enabled())
    print("OpenMP threads: ", openmp_get_num_threads())
    start = time.time()
    g = load_graph("./graphs/my_graph_full_wo_properties.gt.gz")
    load_time = time.time()
    print("Time taken to load graph:", load_time - start, "seconds")
    with open("state_sbm_full.pickle", "rb") as f:
        state: PPBlockState = pickle.load(f)
    end = time.time()
    print("Time taken to load state:", end - load_time, "seconds")
    pos = sfdp_layout(g, groups=state.get_blocks())
    layout_time = time.time()
    print("Time taken to compute layout:", layout_time - end, "seconds")
    with open("pos_sfdp_full.pickle", "wb") as f:
        pickle.dump(pos, f)
    final_time = time.time()
    print("Time taken to save positions:", final_time - layout_time, "seconds")
    print("Total time taken:", final_time - start, "seconds")



if __name__ == "__main__":
    main()