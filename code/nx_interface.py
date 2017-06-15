"""
Compute a given metric for given graph G
"""
def compute_nx_metric(G, metric):
    if metric == CONST.NX_AVERAGE_CLUSTERING:
        return nx.average_clustering(G)
    elif metric == CONST.NX_BETWEENNESS_CENTRALITY:
        return nx.betweenness_centrality(G)
    elif metric == CONST.NX_CLOSENESS_CENTRALITY:
        return nx.closeness_centrality(G)
    elif metric == CONST.NX_CLUSTERING_COEFFICIENT:
        # Clustering coefficient at specified nodes
        return nx.clustering(G)
    elif metric == CONST.NX_DEGREE:
        return nx.degree(G)
    elif metric == CONST.NX_DEGREE_CENTRALITY:
        return nx.degree_centrality(G)
    elif metric == CONST.NX_EIGENVECTOR_CENTRALITY:
        return nx.eigenvector_centrality(G)
    elif metric == CONST.NX_PAGE_RANK:
        return nx.pagerank(G, alpha=CONST.NX_PAGE_RANK_DEFAULT_ALPHA)
    elif metric == CONST.NX_RICH_COEFFICIENT:
        return nx.rich_club_coefficient(G, normalized=False)
    elif metric == CONST.NX_NODE_CONNECTIVITY:
        return nx.node_connectivity(G)
    elif metric == CONST.NX_TRANSITIVITY:
        return nx.transitivity(G)