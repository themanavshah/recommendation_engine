from dummy_data import *
import User_generator as ug

def user_based_algorithm(user_list):

    def intersection_length(user_list, user_random):
        intersect = user_list.intersection(user_random)
        #print(user_random)
        return len(intersect)

    def difference_set(user_list, user_random):
        diffrence = user_random.difference(user_list)
        #print(user_random)
        return diffrence

    def len_algo_check(userint, user0list):
        if userint >= 2:
            for i in difference_set(user_list, user0list):
                recomm_list.append(data[f'{i}']['name'])


    user1int = intersection_length(user_list, ug.user1list)
    user2int = intersection_length(user_list, ug.user2list)
    user3int = intersection_length(user_list, ug.user3list)
    user4int = intersection_length(user_list, ug.user4list)
    recomm_list = []

    len_algo_check(user1int, ug.user1list)
    len_algo_check(user2int, ug.user2list)
    len_algo_check(user3int, ug.user3list)
    len_algo_check(user4int, ug.user4list)  

    recomm_list_user = []
    for i in recomm_list:
        if i not in recomm_list_user:
            recomm_list_user.append(i)
        else:
            continue                    


    print("Here some things you may like:")
    print(recomm_list_user)
