import folium

if __name__ == '__main__':
    
    # sample GeoJSON polygon
    geojson = {
        "type": "Feature",
        "geometry": {
            "type": "Polygon",
            "coordinates": [[[7.84, 52.13], [7.90, 52.09], [7.88, 52.08], [7.84, 52.13]]]
        },
        "properties": {"name": "Zone A"}
    }
    
    m = folium.Map(location=[52.10, 7.87], zoom_start=13)
    folium.GeoJson(geojson).add_to(m)
    m.save("karte.html")