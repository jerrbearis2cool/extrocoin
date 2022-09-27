import folium
from folium.plugins import FloatImage
map = folium.Map(location=[51.142189, -114.152878], tiles="Stamen Terrain", zoom_start=4)


geocache_image = folium.features.CustomIcon("5.png", icon_size=(50,50))

iframe = folium.IFrame("""<h2 style="text-align: left;"><strong>ExtroCache </strong>#<span style="text-decoration: underline;">101</span></h2><h4>Cache reward: <span style="text-decoration: underline;">10</span> EXC</h4><h4>World ranking: #<span style="text-decoration: underline;">1</span> </h4><h4>Additional info: <span style="text-decoration: underline;">code hidden in trees</span></h4><p>good luck!</p><p>&nbsp;</p>""")
popup = folium.Popup(iframe, min_width=300, max_width=300)
folium.Marker(location=[51.142189, -114.152878], icon=geocache_image, popup=popup).add_to(map)

map.save("global_map.html")
"""image_file = 'legend.PNG'
FloatImage(image_file, bottom=0, left=80).add_to(map)"""