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
        
        #is next to exit gateway?
        if len(egs := set(g.edges[agent_id]) & set(self.exit_gateways)) > 0:
            u = agent_id
            v = next(iter(egs))
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

            #do we only have one exit node left?
            if len(node_to_exit_gateway_count_lookup) == 0:
                #just pick a link going to an exit gateway.
                eg = self.exit_gateways[0]
                u = g.edges[eg][0]
                v = eg
            else:
                dist, pred = g.bfs(agent_id)

                most_urgent_node = next((node for node in node_to_exit_gateway_count_lookup.keys() if dist[node] == 1), None)
                if most_urgent_node is not None:
                    potential_exit_gateways = set(g.edges[most_urgent_node]) & set(self.exit_gateways)
                    eg = next(iter(potential_exit_gateways))

                    u = most_urgent_node
                    v = eg
                else:
                    non_exit_node_edge_count_lookup = {}

                    for node in node_to_exit_gateway_count_lookup.keys():
                        non_exit_node_edge_count_lookup[node] = len([e for e in g.edges[node] if e not in self.exit_gateways])

                    urgency_lookup = {}
                    for node in node_to_exit_gateway_count_lookup.keys():
                        urgency_lookup[node] = non_exit_node_edge_count_lookup[node] - dist[node]

                    most_urgent_node = sorted(urgency_lookup.items(), key=lambda item:item[1], reverse=True)[0][0]
                    potential_exit_gateways = set(g.edges[most_urgent_node]) & set(self.exit_gateways)
                    eg = next(iter(potential_exit_gateways))

                    u = most_urgent_node
                    v = eg

        #paths.sort(key=lambda path: len(path))

        assert u is not None
        assert v is not None
        return u, v
