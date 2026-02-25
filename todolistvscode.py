import os
print('To Do List')
to_dos = []

def add_task():
    print('Add a new task.')
    print('---------------')
    new_task = input('Enter a task: ')
    to_dos.append(new_task)

def show_task():
    print('List the tasks.')
    print('---------------')
    n = 1
    for todo in to_dos:
        print(f'{n} - {todo}')
        n += 1

def update_task():
    print('Update the tasks.')
    print('-----------------')
    show_task()
    i = int(input('Choose index to update:'))
    if i > 0 and i <= len(to_dos):
        update = input('Enter the update task: ')
        to_dos[i - 1] = update
    else:
        print('Index out of range!')

def delete_task():
    print('Delete the task.')
    print('----------------')
    show_task()
    j = int(input('Choose index to delate: '))
    if j > 0 and j <= len(to_dos):
        del to_dos[j - 1]
    else:
        print('Your number is out of range!')

while True:
    os.system("cls")
    print('Menu')
    print('----')
    print('0 - Exist')
    print('1 - Add the task')
    print('2 - Show the tasks')
    print('3 - Update the task')
    print('4 - Delete the task')
    choice = int(input('Enter a number from the menu: '))

    os.system('cls')
    match choice:
        case 0:
            exit(0)
        case 1:
            add_task()
        case 2:
            show_task()
        case 3:
            update_task()
        case 4:
            delete_task()
        case _:
            print('Please enter the number from the Menu lise!!')

    os.system('pause')