import random

def generate_random_char():
    alphabet =list('qwertyuiopasdfghjklzxcvbnm ')
    random_symbol = alphabet[random.randrange(27)]
    return random_symbol

def main():
    goal = list('test')
    new_list = []
    lenght_generated, lenght_goal, count  = 0, 0, 0
    while goal != new_list:
        new_list.append(generate_random_char())
        char_of_goal = goal[lenght_goal]
        char_of_new_list = new_list[lenght_generated]
        if  char_of_goal == char_of_new_list:
            lenght_generated += 1
            lenght_goal += 1
            print(new_list)
        else:
            lenght_generated, lenght_goal = 0, 0
            new_list = []
        count += 1
    print(count)

main()