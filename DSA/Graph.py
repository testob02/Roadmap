class Graph:
    def __init__(self,graph_list):

        self.graph_dict = {}
        for start, end in graph_list:
            if start in self.graph_dict.keys():
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def get_all_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return
        
        paths = []

        for node in self.graph_dict[start]:
            if node and node not in path:
                new_paths = self.get_all_paths(node, end, path)
                if new_paths:
                    for i in new_paths:
                        paths.append(i)

        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path
        
        if start not in self.graph_dict:
            return
        
        shortest_path = None

        for node in self.graph_dict[start]:
            if node and node not in path:
                new_path = self.get_shortest_path(node,end,path)
                if new_path:
                    if shortest_path is None or len(shortest_path) > len(new_path):
                        shortest_path = new_path

        return shortest_path


graph_list= [
    ('Kwara','Ekiti'),
    ('Ekiti','Kogi'),
    ('Ekiti','Minna'),
    ('Kwara','Minna'),
    ('Minna','Abuja'),
    ('Kogi','Abuja'),
    ('Kwara','Oyo'),
    ('Oyo','Lagos'),
    ('Kaduna','Abuja'),
    ('Minna','Kaduna')
]

routes = Graph(graph_list)
print(routes.graph_dict)
print(routes.get_all_paths('Ekiti','Abuja'))
print(routes.get_shortest_path('Ekiti','Abuja'))