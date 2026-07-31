class Dinic:
    def __init__(self, size):
        self.graph = [[] for _ in range(size)]

    def add_edge(self, start, end, capacity):
        forward = [end, capacity, None]
        backward = [start, 0, forward]
        forward[2] = backward
        self.graph[start].append(forward)
        self.graph[end].append(backward)

    def max_flow(self, source, sink):
        total = 0

        while True:
            level = [-1] * len(self.graph)
            level[source] = 0
            queue = [source]

            for node in queue:
                for edge in self.graph[node]:
                    if edge[1] > 0 and level[edge[0]] == -1:
                        level[edge[0]] = level[node] + 1
                        queue.append(edge[0])

            if level[sink] == -1:
                return total

            position = [0] * len(self.graph)

            def send(node, flow):
                if node == sink:
                    return flow

                while position[node] < len(self.graph[node]):
                    edge = self.graph[node][position[node]]

                    if edge[1] > 0 and level[edge[0]] == level[node] + 1:
                        sent = send(edge[0], min(flow, edge[1]))
                        if sent:
                            edge[1] -= sent
                            edge[2][1] += sent
                            return sent

                    position[node] += 1

                return 0

            while True:
                sent = send(source, 10**9)
                if sent == 0:
                    break
                total += sent


while True:
    n, m, g = map(int, input().split())

    if n == 0 and m == 0 and g == 0:
        break

    points = [0] * n
    played = [[0] * n for _ in range(n)]

    for _ in range(g):
        first, result, second = input().split()
        first = int(first)
        second = int(second)
        played[first][second] += 1
        played[second][first] += 1

        if result == "<":
            points[second] += 2
        else:
            points[first] += 1
            points[second] += 1

    favorite_points = points[0]
    for opponent in range(1, n):
        favorite_points += 2 * (m - played[0][opponent])

    games = []
    total_points = 0

    for first in range(1, n):
        for second in range(first + 1, n):
            remaining = m - played[first][second]
            if remaining:
                games.append((first, second, 2 * remaining))
                total_points += 2 * remaining

    source = 0
    game_start = 1
    team_start = game_start + len(games)
    sink = team_start + n - 1
    flow = Dinic(sink + 1)

    for index, (first, second, available) in enumerate(games):
        game_node = game_start + index
        flow.add_edge(source, game_node, available)
        flow.add_edge(game_node, team_start + first - 1, available)
        flow.add_edge(game_node, team_start + second - 1, available)

    possible = True

    for team in range(1, n):
        capacity = favorite_points - 1 - points[team]
        if capacity < 0:
            possible = False
            capacity = 0
        flow.add_edge(team_start + team - 1, sink, capacity)

    possible = possible and flow.max_flow(source, sink) == total_points
    print("Y" if possible else "N")
