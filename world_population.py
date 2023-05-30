import json
from pygal_maps_world.i18n import COUNTRIES
import pygal_maps_world.maps as map
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle
import pygal
from country_codes import get_country_code

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

country_dict = {}
#print population of each country in 2010
for pop_dict in pop_data:
    if pop_dict["Year"] == '2010':
        country_name = pop_dict["Country Name"]
        population = int(float(pop_dict["Value"]))
        code = get_country_code(country_name)
        if code:
            country_dict[code] = population

cd1,cd2,cd3 = {},{},{}
for k,v in country_dict.items():
    if v<10000000:
        cd1[k] = v
    elif v<1000000000:
        cd2[k] = v
    else:
        cd3[k] = v


#wm_style = RotateStyle('#336699')
wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)

wm = map.World(style=wm_style)
wm.title = 'World Population in 2010, by Country or Region'   
wm.add('0-10m', cd1)
wm.add('10m-1bn', cd2)
wm.add('>1bn', cd3)

wm.render_to_file('world_population_map.svg')