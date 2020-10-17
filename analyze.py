# Functions to analyze database
import itertools
import networkx as nx

def get_coauthorship_graph(papers, authors, papers_filter=3):
    nodes_to_add=[]
    edges_to_add=[]

    # First we create the nodes (authors) but only the ones that >=
    # papers_filter number of papers
    for author in authors:
        if len(authors[author]['papers_list']) >= papers_filter:
            nodes_to_add.append(author)
    nodes_to_add = list(set(nodes_to_add)) # paranoid attempt to reduce dups
    print('Number of nodes ', len(nodes_to_add))

    # Now the edges
    for paper in papers:
        author_list=papers[paper]['authors']
        intersection = list(set(author_list) & set(nodes_to_add))
        if len(intersection) >0:
            # There are authors here that satisfy the condition
            for (auth1, auth2) in itertools.combinations(intersection,2):
                edges_to_add.append((auth1, auth2))
    edges_to_add=list(set(edges_to_add))
    print('Number of edges to add: ', len(edges_to_add))

    # Create the graph using networkx
    G= nx.Graph()
    G.add_nodes_from(nodes_to_add)
    G.add_edges_from(edges_to_add)

    return G
