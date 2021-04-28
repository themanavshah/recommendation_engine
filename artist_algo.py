from dummy_data import *

IDs = {id for id in  data}
artists = set()

for x in IDs:
    artists.add(data[x]['artist'])

listx = ['m1', 'm2', 'm3']    

    
def artist_algorithm(user_input_list):
    dummy_artist = set()
    for i in user_input_list:
        dummy_artist.add(data[i]['artist'])
    artist_counter = {}
    for y in listx:
        if data[y]['artist'] not in dummy_artist:
            dictx = {f'{data[y]["artist"]}': 0}
            artist_counter.update(dictx)
        else:
            artist_counter[{f"{data[y]['artist']}"}] += 1



    