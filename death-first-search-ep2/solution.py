from graph import Graph, GraphUtils


class Solution:
    def __init__(self, n) -> None:
        self.n: int

        self.g = Graph()
        for i in range(n):
            self.g.add_node(i)

        self.exit_gateways = []

    def add_link(self, n1, n2):
        self.g.add_edge(n1, n2)

    def remove_link(self, n1, n2):
        self.g.remove_edge(n1, n2)

        #if we cut the last link to a node, remove all knowledge of it from state. 
        ns = [n1, n2]
        for n in ns:
            if len(self.g.edges[n]) == 0:
                self.g.remove_node(n)
                if n in self.exit_gateways:
                    self.exit_gateways.remove(n)

    def add_exit_gateway(self, e):
        self.exit_gateways.append(e)

    def link_to_cut(self, agent_id):
        g = self.g
        dist, pred = g.bfs(agent_id)
        
        #is agent next to exit node?
        if (eg := next((eg for eg in self.exit_gateways if dist[eg] == 1), None)) is not None:
            u = agent_id
            v = eg
        else:
            #find nodes connected to more than one exit node, pick the most urgent one to cut.
            node_to_exit_gateway_count_lookup = {}

            for eg in self.exit_gateways:
                for node in g.edges[eg]:
                    if node not in node_to_exit_gateway_count_lookup:
                        node_to_exit_gateway_count_lookup[node] = 0
                    node_to_exit_gateway_count_lookup[node] += 1

            #only keep nodes that have a connection to more than one exit node
            node_to_exit_gateway_count_lookup = {k:v for k, v in node_to_exit_gateway_count_lookup.items() if v>1}

            if len(node_to_exit_gateway_count_lookup) == 0:
                #just pick a link going to an exit gateway.
                eg = self.exit_gateways[0]
                u = g.edges[eg][0]
                v = eg
            else:
                urgency_lookup = {}
                for node, exit_gateway_count in node_to_exit_gateway_count_lookup.items():
                    urgency_lookup[node] = exit_gateway_count - dist[node]

                #sort urgency_lookup on urgency
                sorted_urgency_lookup = sorted(urgency_lookup.items(), key=lambda item: item[1], reverse=True)

                most_urgent_node = sorted_urgency_lookup[0][0]
                potential_exit_gateways = set(g.edges[most_urgent_node]) & set(self.exit_gateways)
                
                eg = next(iter(potential_exit_gateways))

                u = most_urgent_node
                v = eg

        #paths.sort(key=lambda path: len(path))

        assert u is not None
        assert v is not None
        return u, v
