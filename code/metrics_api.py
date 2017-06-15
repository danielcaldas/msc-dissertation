@app.route(CONST.ROUTE_PREFIX + '/metrics', methods=['POST'])
def calculate_metrics_for_graph():
    try:
        payload = request.get_json()

        if 'multigraph' not in payload:
            payload['multigraph'] = False

        # Check for metrics, if no metrics assume all available as default
        metrics = []
        if 'metrics' not in payload:
            metrics = CONST.NX_AVAILABLE_NODE_METRICS + CONST.NX_AVAILABLE_GRAPH_METRICS
        else:
            metrics = payload['metrics']

        if payload['graph']:
            G = json_graph.node_link_graph(payload)
            return jsonify(nx_interface.calculate_metrics(G, metrics)), 200
        else:
            return jsonify({CONST.MSG: CONST.ERR_INVALID_PAYLOAD}), 404
    except:
        return jsonify({CONST.MSG: CONST.ERR_GENERIC}), 500