from gmplot import gmplot
import json

# Place map
gmap = gmplot.GoogleMapPlotter(37.766956, -122.438481, 6)


with open('Location History.json') as json_data:
    d = json.load(json_data)
    lat_long = []
    for location in d["locations"]:
        lat_calc = (int(location["latitudeE7"] / 10000) * 10000) / 1e7
        long_calc = (int(location["longitudeE7"] / 10000) * 10000) / 1e7
        lat_long.append((lat_calc, long_calc))
    print(len(lat_long))
    set_lat_long = set(lat_long)
    print(len(set_lat_long))

#
# # Polygon
# golden_gate_park_lats, golden_gate_park_lons = zip(*lat_long)
# gmap.plot(golden_gate_park_lats, golden_gate_park_lons, 'cornflowerblue', edge_width=3)

# Scatter points
top_attraction_lats, top_attraction_lons = zip(*set_lat_long)
gmap.scatter(top_attraction_lats, top_attraction_lons, 'cornflowerblue', edge_width=4, marker=False)
#gmap.heatmap(top_attraction_lats, top_attraction_lons)

# Draw
gmap.draw("my_map.html")
