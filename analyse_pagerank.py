import graph_tool.all as gt
import matplotlib.pyplot as plt
import pickle

def main():
    print("OpenMP enabled: ", gt.openmp_enabled())
    print("OpenMP threads: ", gt.openmp_get_num_threads())
    with open("pagerank_values_full.pickle", "rb") as f:
        pagerank: gt.PropertyArray = pickle.load(f)
    print("random pagerank: ", pagerank[461353])
    min = pagerank.min()
    max = pagerank.max()
    mean = pagerank.mean()
    pagerank.sort()
    median = pagerank[(pagerank.size // 2)]
    upper_quartile = pagerank[(3 * pagerank.size) // 4]
    lower_quartile = pagerank[pagerank.size // 4]
    print("min: ", min, "\nmax: ", max, "\nmean: ", mean, "\nmedian: ", median, "\nupper_quartile: ", upper_quartile, "\nlower_quartile: ", lower_quartile)
    plt.hist(pagerank, range=(min, max))
    plt.show()


if __name__ == "__main__":
    main()