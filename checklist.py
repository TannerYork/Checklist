from termcolor import colored

checklist = list()

# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    return checklist[index]

# UPDATE
def update(index, item):
    checklist[index] = item

# DELETE
def delete(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print('{} {}'.format(index, list_item))
        index += 1

def mark_completed(index):
    item_index = valid_index(user_input('Index Number: '))
    if item_index is 0 or item_index:
        checklist[item_index] = colored(checklist[item_index], 'green')

def mark_uncomplete(index):
    item_index = valid_index(user_input('Index Number: '))
    if item_index is 0 or item_index:
        checklist[item_index] = colored(checklist[item_index], 'grey')

def select(function_code):
    if function_code == 'C' or function_code == 'c':
        input_item = user_input('Input item: ')
        create(input_item)
    
    elif function_code == 'R' or function_code == 'r':
        item_index = valid_index(user_input('Index Number: '))
        if item_index is 0 or item_index:
            print(read(item_index))

    elif function_code == 'U' or function_code == 'u':
        item_index = valid_index(user_input('Index Number: '))
        if item_index is 0 or item_index:
            update(item_index, user_input('New Item: '))
    
    elif function_code == 'MD' or function_code == 'md':
        item_index = valid_index(user_input('Index Number: '))
        if item_index is 0 or item_index:
            mark_completed(item_index)

    elif function_code == 'MU' or function_code == 'mu':
        item_index = valid_index(user_input('Index Number: '))
        if item_index is 0 or item_index:
            mark_uncompleted(item_index)

    elif function_code == 'D' or function_code == 'd':
        item_index = valid_index(user_input('Index Number: '))
        if item_index is 0 or item_index:
            delete(item_index)

    elif function_code == 'P' or function_code == 'p':
        list_all_items()

    elif function_code == 'Q' or function_code == 'q':
        return False

    else:
        print('Unkown Option')
    return True

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def valid_index(index):
    if index.isnumeric() and int(index) <= len(checklist):
        return int(index)
    else:
        print('Invaled, index is either not an int or out of range')
        return False

running = True
while running:
    selection = user_input('Press C to add list, R to read from list, U to update item in list, MC to mark item as complete, MU to mark uncomplete, D to delete item in list, P to display all items, and Q to quit ')
    running = select(selection)


def test ():
    create('purple sox')
    create('red cloaks')

    print(read(0))
    print(read(1))

    update(0, 'purple socks')
    delete(1)

    print(read(0))

    mark_completed(0)

    list_all_items()

    select('C')
    
    list_all_items()

    select('R')

    list_all_options()

