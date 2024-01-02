# Code will determine the light intensity planets receive from the sun.
# Planet data will be based on their distance and size.
# Light intensity is affected by distance, size, and if they are in the shadow of another planet.

# Convert following planet data from csv file to a list of dictionaries.
# Name, Distance (AU), Size (km)
# Mercuria, 0.4, 4879
# Earthia, 1, 12742
# Marsia, 1.5, 6779
# Venusia, 0.7, 12104

# Light Dynamics
# If a smaller planet is behind a larger planet (relative to the Lumorian Sun), it will be in the shadow and will receive no light (None).
# If a larger planet is behind a smaller planet (relative to the Lumorian Sun), it will have Partial light.
# If a planet is in the shadow of multiple planets, it will be marked as None (Multiple Shadows).
# If two planets are of similar size and are near each other in alignment, they might partially eclipse each other, but for simplicity, you can consider them both to receive full light.

# Output
# Your system should output a list of planets and the light intensity they receive: Full, Partial, None, or None (Multiple Shadows).


# Sort the planets by distance from the sun, closest to farthest.
def sort():
    planetnames = ['Mercuria', 'Earthia', 'Marsia', 'Venusia']
    planetdistance = [0.4, 1, 1.5, 0.7]
    planetsize = [4879, 12742, 6779, 12104]
    planetdata = []
    for i in range(len(planetnames)):
        planetdata.append({'name': planetnames[i], 'distance': planetdistance[i], 'size': planetsize[i]})
    planetdata.sort(key=lambda x: x['distance'])
    return planetdata


def lightintensity():
    lightdata = sort()
    #print(lightdata)
    for i in range(len(lightdata)):
        # if size of current planet is smaller than size of previous planet, then current planet is in shadow of previous planet
        if i > 0 and lightdata[i]['size'] < lightdata[i-1]['size']:
            lightdata[i]['lightintensity'] = 'None'
        # if size of current planet is larger than size of previous planet, then current planet is in shadow of previous planet
        elif i > 0 and lightdata[i]['size'] > lightdata[i-1]['size']:
            lightdata[i]['lightintensity'] = 'Partial'
        # if size of current planet is equal to size of previous planet, then current planet is in shadow of previous planet
        elif i > 0 and lightdata[i]['size'] == lightdata[i-1]['size']:
            lightdata[i]['lightintensity'] = 'Full'
        # if a current planet is in the shadow of multiple planets, it will be marked as None (Multiple Shadows)
        elif i > 0 and lightdata[i]['size'] < lightdata[i-1]['size']:
            lightdata[i]['lightintensity'] = 'None (Multiple Shadows)'
    print(lightdata)

lightintensity()