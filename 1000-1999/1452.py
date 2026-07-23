while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    application_servers = {}

    for server in range(n):
        data = input().split()

        for application in data[1:]:
            if application not in application_servers:
                application_servers[application] = set()

            application_servers[application].add(server)

    connections = 0

    for _ in range(m):
        data = input().split()
        connected_servers = set()

        for application in data[1:]:
            connected_servers.update(application_servers.get(application, ()))

        connections += len(connected_servers)

    print(connections)
