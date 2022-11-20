import random
import art
import data
import replit
scr =0
f =1
def format_data(rand):
    # Format the account data into printable format
    name = rand['name']
    country = rand['country']
    description = rand['description']
    return (f'{name}, from {country}, a{description}')

def check_answer(g,fa,fb):
    # -Use if statement to chick if user is correct
    if (fa > fb and g == 'A'):
        return  g=='a'
        print(f"you are right ! current score : {scr}")

    else:
        return g== 'b'


#Display art
print(art.logo)
#Making the game repeatable
continue_game =True
while(continue_game):
    randb = random.choice(data.data)
    #Genarate a random account from the game data
    # Making account at position B become the next account at position A
    randa =randb
    randb = random.choice(data.data)

    while(randb == randa):
        randb = random.choice(data.data)

    print(f"Compare A :{format_data(randa)}")
    print(art.vs)
    print(f"Compare B :{format_data(randb)}")

    #Ask user for a guess
    guess = input("who has more followers ? Type 'A' or 'B'").upper()

    #Chick if user is correct
    #-Get follower count of each account
    follower_a =randa['follower_count']
    follower_b =randb['follower_count']

    answer = check_answer(guess,follower_a,follower_b)

    # Clear the screen
    replit.clear()
    #Give user fedback on their guss
    #Score keeping
    if answer:
        scr = scr + 1
        print(f"You're right! Current score : {scr}")

    else:
        continue_game= False
        print(f"sorry, that's wrong. Final score : {scr}.")








