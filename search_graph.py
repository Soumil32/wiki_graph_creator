import graph_tool.all as gt


def main():
    print("OpenMP enabled: ", gt.openmp_enabled())
    print("OpenMP threads: ", gt.openmp_get_num_threads())
    g = gt.load_graph("my_graph_full.gt.gz")
    wiki_id = g.vertex_properties["wiki_id"]
    wiki_title = g.vertex_properties["wiki_title"]
    print("Number of vertices:", g.num_vertices())
    print("Number of edges:", g.num_edges())


if __name__ == "__main__":
    main()