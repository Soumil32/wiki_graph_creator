import csv
import sys
from typing import List
from graph_tool.all import *
import time


def parse_pg_text_array(s):
    # Remove surrounding braces
    s = s.strip('{}')

    # Use CSV parsing to correctly handle quotes and commas
    reader = csv.reader([s], quotechar='"', escapechar='\\')
    return next(reader)


def main():
    csv.field_size_limit(sys.maxsize)
    print("OpenMP enabled: ", openmp_enabled())
    print("OpenMp threads: ", openmp_get_num_threads())
    start = time.time()
    g = Graph(directed=True)
    wiki_id = g.new_vertex_property("int")
    wiki_title = g.new_vertex_property("string")

    LINKS_PATH = "/run/media/soumil/D/enwiki/links sample 500k.csv"

    # Build title -> index mapping and fill properties
    title_to_index = {}
    with open(LINKS_PATH, "r") as f:
        # Initial read of the csv file to create the vertices
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            page_wiki_id = int(row[0])
            vertex_title = row[1]
            title_to_index[vertex_title] = i
            v = g.add_vertex()
            wiki_id[v] = page_wiki_id
            wiki_title[v] = vertex_title

        add_vertices_time = time.time()
        print("Time taken to add vertices:", add_vertices_time - start, "seconds")
        # Second read of the csv file to create the edges
    with open(LINKS_PATH, "r") as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            source_wiki_id = int(row[0])
            target_vertices: List[str] = parse_pg_text_array(row[2])  # List of target wiki_titles as strings
            if len(target_vertices) == 0:
                continue
            source_vertex = g.vertex(i)
            if source_vertex is None:
                # This should not happen as we have already created all vertices
                print("Source vertex not found for vertex_id:", source_wiki_id)
                continue

            edges_to_add = []
            for target_title in target_vertices:
                target_index = title_to_index.get(target_title)
                if target_index is not None:
                    target_vertex = g.vertex(target_index)
                    edges_to_add.append((i, target_index))
            g.add_edge_list(edges_to_add)

    g.vertex_properties["wiki_id"] = wiki_id
    g.vertex_properties["wiki_title"] = wiki_title
    g.save("my_graph_500k.gt.gz")
    end = time.time()
    print("Time taken to build graph:", end - start, "seconds")
    print("Number of vertices:", g.num_vertices())
    print("Number of edges:", g.num_edges())
    print("Random id of a vertex:", wiki_id[g.vertex(4545)])
    print("Random title of a vertex:", wiki_title[g.vertex(4545)])



if __name__ == "__main__":
    main()
