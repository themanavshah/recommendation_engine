from dummy_data import *
import user_algo 

avaiable_list = {id for id in data}


def genre_algorithm(user_input_list, final_recom_list):
    edm = 0
    romance = 0
    buisness_podcast = 0
    self_devlopment_podcast = 0
    pop = 0

    rem_list = avaiable_list.difference(user_input_list)

    for x in user_input_list:
        if data[f'{x}']['genre'] == 'edm':
            edm += 1
        elif data[f'{x}']['genre'] == 'romace':
            romance += 1
        elif data[f'{x}']['genre'] == 'buisness podcast':
            buisness_podcast += 1
        elif data[f'{x}']['genre'] == 'self devlopment podcast':
            self_devlopment_podcast += 1 
        elif data[f'{x}']['genre'] == 'pop':
            pop += 1        
        else:
            continue    

    #Here we can also use max() function but to make this project algorithmic I have created this algorithm:

    if edm > romance and edm > buisness_podcast and edm > self_devlopment_podcast and edm > pop:
        for z in data:
                if z in rem_list and data[f'{z}']['genre'] == 'edm':
                    final_recom_list.insert(0, data[f'{z}']['name'])
                else:
                    pass
    elif romance > edm and romance > buisness_podcast and romance > self_devlopment_podcast and romance > pop:
        for z in data:
                if z in rem_list and data[f'{z}']['genre'] == 'romance':
                    final_recom_list.insert(0, data[f'{z}']['name'])
                else:
                    pass 
    elif buisness_podcast > edm and buisness_podcast > romance and buisness_podcast > self_devlopment_podcast and buisness_podcast > pop:
        for z in data:
                if z in rem_list and data[f'{z}']['genre'] == 'buisness podcast':
                    final_recom_list.insert(0, data[f'{z}']['name'])
                else:
                    pass  
    elif self_devlopment_podcast > edm and self_devlopment_podcast > romance and self_devlopment_podcast > buisness_podcast and self_devlopment_podcast > pop:
        for z in data:
                if z in rem_list and data[f'{z}']['genre'] == 'self devlopment podcast':
                    final_recom_list.insert(0, data[f'{z}']['name'])
                else:
                    pass 
    elif pop > edm and pop > romance and pop > self_devlopment_podcast and pop > buisness_podcast:
        for z in data:
                if z in rem_list and data[f'{z}']['genre'] == 'pop':
                    final_recom_list.insert(0, data[f'{z}']['name'])
                else:
                    pass
    else:
        user_algo.user_based_algorithm(user_input_list)                                                      


    
    print(final_recom_list)