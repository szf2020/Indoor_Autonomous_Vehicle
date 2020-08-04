# Distance of each poins
G = {1: {1: 0, 2: 3},
     2: {1: 3, 2: 0, 3: 2, 11: 4},
     3: {2: 2, 3: 0, 4: 2, },
     4: {3: 2, 4: 0, 5: 3, 8: 2},
     5: {4: 3, 5: 0, 6: 4},
     6: {5: 3, 6: 0, 7: 5,12:10},
     7: {6: 5, 7: 0},
     8: {4: 2, 8: 0, 9: 2},
     9: {8: 2, 9: 0, 10: 4},
     10: {9: 4, 10: 0, 11: 4},
     11: {2: 4, 10: 4, 11:0, 13:10},
     12: {6: 10, 12:0},
     13: {11: 10, 13:0},
     }

encode_list = {
    26: "Z",
    25: "Y",
    24: "X",
    23: "W",
    22: "V",
    21: "U",
    20: "T",
    19: "S",
    18: "R",
    17: "Q",
    16: "P",
    15: "O",
    14: "N",
    13: "M",
    12: "L",
    11: "K",
    10: "J",
    9: "I",
    8: "H",
    7: "G",
    6: "F",
    5: "E",
    4: "D",
    3: "C",
    2: "B",
    1: "A",
    }

def Dijkstra(G, v0, INF=999):  # 999 means that the distance from the node to the starting point does not have an exact value
    dis = dict((i, INF) for i in G.keys())  # Initialize a distance table, this table records the distance from the starting node v0 to each point in the graph
    current_node = v0  # At the beginning, the current point is set as the starting point v0
    dis[v0] = 0 # The distance from the initial point to destination is 0
    visited = []  # Record the nodes that have been traversed
    ###
    path = dict((i, []) for i in G.keys())  #Initialize a path table, this table records the shortest path from the starting node to each point on the way
    path[v0] = str(v0)  # The path from the initial point to yourself is naturally for yourself
    ###
    while len(G) > len(visited):  # When the nodes of the graph have not been traversed, the loop is executed to continue the traversal
        visited.append(current_node)  # The current point is being traversed, so put the current point in the visited table
        for k in G[current_node]:  # Traverse all adjacent points of the current point
            if dis[current_node] + G[current_node][k] < dis[k]:  # If (the distance from the starting point to the adjacent point k of the current point) is greater than (the distance from the starting point to the current point + the distance from the current point to the adjacent point k)
                dis[k] = dis[current_node] + G[current_node][k]  # Then (the distance from the starting point to the adjacent point k of the current point) is updated to (the distance from the starting point to the current point + the distance from the current point to the adjacent point k)
                seq = (path[current_node], str(k))
                sym = '-'
                path[k] = sym.join(seq)  # The shortest path from the starting point to (the neighboring point k of the current point), connect the two strings in seq with'-'
         # Then choose the next current node (current_node)
         # From the remaining untraversed points, select the point with the smallest distance from the current point as the next current point
        new = INF
        for node in dis.keys():
            if node in visited:
                continue
            if dis[node] < new:
                new = dis[node]
                current_node = node
    return dis, path
# Generate result to A-Z dictionary
length_dictionary = len(G)
for x1 in range(1, length_dictionary+1):
    dis, path = Dijkstra(G, v0=x1)
    x = str(x1)
    x = x.replace(x, "'{}':".format(encode_list[int(x)]))
    print(x)
    path = str(path)
    for a in range(26, 0,-1):
        path = path.replace("{}:".format(str(a)), "'{}':".format(encode_list[int(a)]))
        path = path.replace(str(a), "{}".format(encode_list[int(a)]))
    path = path.replace("-", "")
    print(path)
    x1 = x1 + 1
