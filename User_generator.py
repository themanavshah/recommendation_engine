from dummy_data import *
import random

datals = [id for id in data]
user1 = set()
user2 = set()
user3 = set()
user4 = set()

def generate_user_list(user):
    for _ in range(5): 
        user.add(random.choice(datals))
    return user    

user1list = generate_user_list(user1)
user2list = generate_user_list(user2)
user3list = generate_user_list(user3)
user4list = generate_user_list(user4)




    
