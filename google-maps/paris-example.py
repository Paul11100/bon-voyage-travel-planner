import routes
places = ['Panthéon, Paris', 'Eiffel Tower, Paris', 'Louvre Museum, Paris', 'Arc de Triomphe, Paris']
path = routes.shortest_path(places, routes.map_client)
map_url = routes.generate_map_url(path[0], path[len(path)-1], '|'.join(path[1:-1]))
print(map_url)
