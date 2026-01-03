from graph_tool.all import *
import time


def main():
    print("OpenMP enabled: ", openmp_enabled())
    print("OpenMp threads: ", openmp_get_num_threads())
    start = time.time()
    g = load_graph("my_graph.gt.gz")
    wiki_id = g.vertex_properties["wiki_id"]
    wiki_title = g.vertex_properties["wiki_title"]
    pos = sfdp_layout(g)
    # state = minimize_nested_blockmodel_dl(g)
    state = minimize_blockmodel_dl(g)
    state.draw(pos=pos, output="graph_blockmodel.pdf", vertex_text=wiki_id)
    end = time.time()
    print("Time taken to build and analyze graph:", end - start, "seconds")
    # graph_draw(g, pos=pos, vertex_text=wiki_title, output="graph.pdf", vertex_fill_color="#FFDD44")


if __name__ == "__main__":
    main()