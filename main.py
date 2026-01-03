from graph_tool.all import *
from typing import List
import csv
import random


def parse_pg_text_array(s):
    # Remove surrounding braces
    s = s.strip('{}')

    # Use CSV parsing to correctly handle quotes and commas
    reader = csv.reader([s], quotechar='"', escapechar='\\')
    return next(reader)

def main():
    print("OpenMP enabled: ", openmp_enabled())
    print("OpenMp threads: ", openmp_get_num_threads())
    g = Graph(directed=True)
    wiki_id = g.new_vertex_property("int")
    wiki_title = g.new_vertex_property("string")
    LINKS_PATH = "/run/media/soumil/D/enwiki/links sample copy.csv"
    with open(LINKS_PATH, "r") as f:
        # Initial read of the csv file to create the vertices
        reader = csv.reader(f)
        for row in reader:
            vertex_id = row[0]
            vertex_title = row[1]
            v = g.add_vertex()
            wiki_id[v] = int(vertex_id)
            wiki_title[v] = vertex_title

        # Second read of the csv file to create the edges
        f.seek(0)
        for row in reader:
            source_wiki_id = row[0]
            target_vertices: List[str] = parse_pg_text_array(row[2])
            if len(target_vertices) == 0:
                continue
            source_vertex = None
            for v in g.iter_vertices():
                if wiki_id[v] == int(source_wiki_id):
                    source_vertex = v
                    break
            if source_vertex is None:
                # This should not happen as we have already created all vertices
                print("Source vertex not found for vertex_id:", vertex_id)
                continue
            for target_title in target_vertices:
                target_vertex = None
                for v in g.iter_vertices():
                    if wiki_title[v] == target_title:
                        target_vertex = v
                        break
                if target_vertex is not None:
                    g.add_edge(source_vertex, target_vertex)


    print("Number of vertices:", g.num_vertices())
    print("Number of edges:", g.num_edges())
    print("Random id of a vertex:", wiki_id[g.vertex(4545)])
    pos = sfdp_layout(g)
    # state = minimize_nested_blockmodel_dl(g)
    state = minimize_blockmodel_dl(g)
    state.draw(pos=pos, output="graph_blockmodel.pdf")
    # graph_draw(g, pos=pos, vertex_text=wiki_title, output="graph.pdf", vertex_fill_color="#FFDD44")


if __name__ == "__main__":
    main()