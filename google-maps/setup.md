## Set-Up

Brief document with basic set-up instructions and links

### Installing Libraries

1. `pip install python-dotenv`
2. `pip install googlemaps`

### Add API KEY

Create a .env file inside this google-maps directory, and add

```
API_KEY=YOUR_GOOGLE_CLOUD_API_KEY
```

### Run Example

Once you've set up the API Key, you can run the paris example by opening up terminal:

```
python3 paris-example.py
```

### Modifying Example

To find shortest path for different places, modify the list passed as the first parameter into routes.shortest_path(). This list can be an arbitrary length, and the suggested entry format is "PLACE_NAME, CITY"

There is no need to modify the call to generate_map_url.

### Helpful Links

- [Docs for Python Client](https://googlemaps.github.io/google-maps-services-python/docs/index.html)
