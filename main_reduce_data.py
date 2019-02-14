import json
import io

with open('Location History.json') as json_data:
    d = json.load(json_data)
    lat_long = []
    for location in d["locations"]:
        lat_calc = (int(location["latitudeE7"] / 100000) * 100000) / 1e7
        long_calc = (int(location["longitudeE7"] / 100000) * 100000) / 1e7
        lat_long.append((lat_calc, long_calc))
    print(len(lat_long))
    set_lat_long = set(lat_long)

    array = []
    for i in lat_long:
        val = {"lat": i[0], "long": i[1]}
        array.append(val)

    with io.open('reduce_location.json', 'w', encoding="utf-8") as json_file_out:
        json_file_out.write(unicode(json.dumps(array, ensure_ascii=False, indent=0)))
