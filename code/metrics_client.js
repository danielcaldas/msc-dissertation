export class SociiMetricsClient {
    constructor(transport) {
        this.transport = transport;
    }

    fetchMetrics(directed=false, graphName='graph', nodes, links, metrics=DEFAULT_METRICS) {
        if (links.length && nodes.length && metrics.length) {
            return this.transport.post('/metrics', {
                directed,
                graph: {name: graphName},
                links,
                nodes,
                metrics
            });
        } else {
            return Promise.reject({msg: CONST.ERROR.NOT_ENOUGH_DATA_PROVIDED});
        }
    }
}
