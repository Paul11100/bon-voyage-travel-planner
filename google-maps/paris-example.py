import routes
path = routes.shortest_path(['Panthéon, Paris', 'Eiffel Tower, Paris', 'Louvre Museum, Paris', 'Arc de Triomphe, Paris'], routes.map_client)
map_url = routes.generate_map_url(path[0], path[len(path)-1], '|'.join(path[1:-1]))
print(map_url)
