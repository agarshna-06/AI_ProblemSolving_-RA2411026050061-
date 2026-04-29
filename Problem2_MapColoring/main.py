def is_valid(node, color, assignment, graph):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


def map_coloring(graph, colors, assignment={}):
    if len(assignment) == len(graph):
        return assignment

    unassigned = [n for n in graph if n not in assignment]
    node = unassigned[0]

    for color in colors:
        if is_valid(node, color, assignment, graph):
            assignment[node] = color
            result = map_coloring(graph, colors, assignment)
            if result:
                return result
            del assignment[node]

    return None


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']

solution = map_coloring(graph, colors)

print(solution)
