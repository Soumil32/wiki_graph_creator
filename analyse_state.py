import graph_tool.all as gt
import pickle


def main():
    print("OpenMP enabled: ", gt.openmp_enabled())
    print("OpenMP threads: ", gt.openmp_get_num_threads())
    with open("state_sbm_full.pickle", "rb") as f:
        state: gt.PPBlockState = pickle.load(f)
    print("Number of blocks:", state.get_B())


if __name__ == "__main__":
    main()