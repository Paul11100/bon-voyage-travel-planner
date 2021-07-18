"""Will use distance matrix api to find and return optimal path link"""
import os
import googlemaps # pip install googlemaps
from dotenv import load_dotenv
from pprint import pprint
from itertools import permutations

def encode(s):
    return s.replace(' ', '+').replace('|','%7C').replace(',', '%2C')

def generate_map_url(origin, dest, waypoints):
    if waypoints:
        return f"https://www.google.com/maps/dir/?api=1&origin={encode(origin)}&destination={encode(dest)}&waypoints={encode(waypoints)}"

def paths(places):
    return list(permutations(places))

def shortest_path(places, map_client):
    # Find all pairs of places
    dists = {}
    for place1 in places:
        for place2 in places:
            if place1 != place2:
                duration = map_client.distance_matrix(place1, place2)['rows'][0]['elements'][0]['distance']['value']
                if place1 not in dists:
                    dists[place1] = {}
                dists[place1][place2] = duration
    
    min_dist = float('inf')
    res = None
    for path in paths(places):
        d = 0
        for i in range(len(path)-1):
            d += dists[path[i]][path[i+1]]
        if d < min_dist:
            min_dist = d
            res = path
    return res

load_dotenv()

API_KEY = os.environ.get("API_KEY")

map_client = googlemaps.Client(API_KEY)