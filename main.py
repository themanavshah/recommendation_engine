from dummy_data import *
import user_algo
import genre_algo


proceed = True
user_input_list = set()
avaiable_list = {id for id in data}
user_input = ''
final_recom_list = []

while proceed or (user_input not in avaiable_list):
    user_input = str(input("create your list: "))
    if user_input not in avaiable_list:
        print("Not available")
    else:    
        user_input_list.add(user_input)
    proceed_input = input("Do you want to add more?: y or n")
    if proceed_input == 'y' or proceed_input == 'Y':
        continue
    else:
        proceed = False


#genre_algo.genre_algorithm(user_input_list, final_recom_list)












