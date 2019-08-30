class Solution(object):
    def __init__(self):
        self.node_colour_map = {}
        
    def colourNode(self, graph, current_node, node_colour):
        node_colour_map = self.node_colour_map.copy()        
        neighbouring_nodes = graph[current_node]
        
        if current_node in node_colour_map and node_colour_map[current_node] != node_colour:
            return False
        else:
            node_colour_map[current_node] = node_colour
        
        for node in neighbouring_nodes:
            neighbouring_nodes_colour = not node_colour
            if node in node_colour_map and (node_colour_map[node] != neighbouring_nodes_colour):
                return False
            else:
                node_colour_map[node] = neighbouring_nodes_colour

        return node_colour_map
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        for i in range(len(graph)):
            try_true = self.colourNode(graph, i, True)
            try_false = self.colourNode(graph, i , False)
            if  try_false:
                self.node_colour_map = try_false.copy()
            if try_true:
                self.node_colour_map = try_true.copy()
            else:
                return False
            print (self.node_colour_map)
        return True

s = Solution()
print (s.isBipartite([[3],[2,4],[1],[0,4],[1,3]]))