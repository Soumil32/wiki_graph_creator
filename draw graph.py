from graph_tool.all import *
import time


def main():
    print("OpenMP enabled: ", openmp_enabled())
    print("OpenMp threads: ", openmp_get_num_threads())
    start = time.time()
    og = load_graph("my_graph_with_state.graphml")
    out_degrees = og.get_out_degrees(og.get_vertices())
    in_degrees = og.get_in_degrees(og.get_vertices())
    g = GraphView(og, vfilt=((out_degrees > 0) | (in_degrees > 0)))
    wiki_id = g.vertex_properties["wiki_id"]
    wiki_title = g.vertex_properties["wiki_title"]
    load_time = time.time()
    print("Time taken to load graph:", load_time - start, "seconds")
    state: BlockState = minimize_blockmodel_dl(g, state=BlockState)
    pos = sfdp_layout(g, groups=state.get_blocks())
    layout_time = time.time()
    print("Time taken to compute layout:", layout_time - load_time, "seconds")
    state.draw(pos=pos, output="graph_blockmodel.svg", output_size=(1000, 1000), vertex_text=wiki_id)
    end = time.time()
    print("Time taken to draw block model:", end - layout_time, "seconds")
    print("Time taken to build and analyze graph:", end - start, "seconds")
    # graph_draw(g, pos=pos, vertex_text=wiki_id, output="graph.svg", vertex_fill_color="#FFDD44")


if __name__ == "__main__":
    main()