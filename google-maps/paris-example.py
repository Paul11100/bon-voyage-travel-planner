'''Three Group of Paris Landmark'''
import routes
places = ['Panthéon, Paris', 'Eiffel Tower, Paris', 'Louvre Museum, Paris', 'Arc de Triomphe, Paris']
# places = ['Cathédrale Notre-Dame de Paris', "Musée d'Orsay", 'Palais Garnier']
# places = ['Sainte-Chapelle, Paris', 'Moulin Rouge, Paris', 'Les Invalides, Paris']
path = routes.shortest_path(places, routes.map_client)
map_url = routes.generate_map_url(path[0], path[len(path)-1], '|'.join(path[1:-1]))
print(map_url)
