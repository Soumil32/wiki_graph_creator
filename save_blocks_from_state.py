import graph_tool.all as gt
import pickle


def main():
    print("OpenMP enabled: ", gt.openmp_enabled())
    print("OpenMP threads: ", gt.openmp_get_num_threads())
    with open("state_100_communities.pickle", "rb") as f:
        state: gt.PPBlockState = pickle.load(f)
    print("Number of blocks:", state.get_B())
    blocks = state.get_blocks()
    with open("blocks_100_communities.pickle", "wb") as f:
        pickle.dump(blocks, f)
    print("Blocks saved to blocks_100_communities.pickle")


if __name__ == "__main__":
    main()