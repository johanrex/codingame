from typing import Callable
from graph import Graph
import sys

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


    def edge_cost(self, src, dst):
        assert src not in self.exit_gateways
        assert dst not in self.exit_gateways

        assert src in self.g.edges[dst]
        assert dst in self.g.edges[src]

        #if both are connected to exit node then cost is 0.
        if len(set(self.g.edges[src]) & set(self.exit_gateways)) > 0 and len(set(self.g.edges[dst]) & set(self.exit_gateways)) > 0:
            cost = 0
        else:
            cost = 1

        return cost    

    def dijkstras(self, g:Graph, start_node:object, edge_cost_func:Callable[[object, object], int]):
        unvisited_nodes = list(g.nodes)
    
        dist = {}
        prev = {}
    
        max_value = sys.maxsize
        for node in unvisited_nodes:
            dist[node] = max_value

        dist[start_node] = 0
        
        while unvisited_nodes:
            current_min_node = None
            for node in unvisited_nodes:
                if current_min_node == None:
                    current_min_node = node
                elif dist[node] < dist[current_min_node]:
                    current_min_node = node
                    
            neighbors = g.edges[current_min_node]
            for neighbor in neighbors:
                
                tentative_value = dist[current_min_node] + edge_cost_func(current_min_node, neighbor)
                if tentative_value < dist[neighbor]:
                    dist[neighbor] = tentative_value
                    prev[neighbor] = current_min_node
    
            unvisited_nodes.remove(current_min_node)
        return prev, dist


    def link_to_cut(self, agent_id):
        g = self.g
        
        ##########################
        # is next to exit gateway?
        ##########################
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
            nodes_connected_to_multiple_exit_gateways = {k:v for k, v in node_to_exit_gateway_count_lookup.items() if v>1}
            
            ###############################
            # only have one exit node left?
            ###############################
            if len(nodes_connected_to_multiple_exit_gateways) == 0:
                #just pick a link going to an exit gateway.
                eg = self.exit_gateways[0]
                u = g.edges[eg][0]
                v = eg
            else:
                #TODO increase urgency by considering how many nodes along the way that are connected to exit nodes. They are forcing moves.
                #TODO no point in using the dist from dist_no_egs since it can contain forcing moves. 

                g_no_egs = g.copy()
                for eg in self.exit_gateways:
                    g_no_egs.remove_node(eg)

                pred, dist = self.dijkstras(g_no_egs, agent_id, self.edge_cost)

                #Throw away the connected count?
                nodes_connected_to_multiple_exit_gateways = nodes_connected_to_multiple_exit_gateways.keys()

                nodes_connected_to_multiple_exit_gateways_dist_lookup = {n : dist[n] for n in nodes_connected_to_multiple_exit_gateways}

                most_urgent_node = sorted(nodes_connected_to_multiple_exit_gateways_dist_lookup.items(), key=lambda item:item[1])[0][0]

                potential_exit_gateways = set(g.edges[most_urgent_node]) & set(self.exit_gateways)
                eg = next(iter(potential_exit_gateways))

                u = most_urgent_node
                v = eg



        assert u is not None
        assert v is not None
        return u, v
