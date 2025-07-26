to_do_list = []

def menu():
    print("----to Do List----")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark as completed")
    print("4. Mark as not completed")
    print("5. Del Task")
    print("6. Exit")

def add_task():
    try:
        task = input("Enter the task: ")
        to_do_list.append({'task': task, 'status': False})
        return print("The Task is successfully added into the list")
    except:
        print("Invalid input")

def mark_as_completed():
    try:
        view_tasks()
        t = int(input("enter the task number that you want to mark as completed: "))
        to_do_list[t-1]['status'] = True
        print("Your task is successfully marked as completed")
        return
    except:
        print("Invalid input")

def delete():
    try:
        view_tasks()
        t = int(input('Enter the task number that you want to delete: '))
        to_do_list.pop(t-1)
        print("Task is succesfully remove from the list")
    except:
        print("Invalid input")

def view_tasks():
    if not to_do_list:
        print("Your list is empty")
        return
    for i, item in enumerate(to_do_list):
        if item['status']:
            print(f"{i+1}: [✓]: {item['task']}")
        else:
            print(f"{i+1}: []: {item['task']}")
    return

def mark_not_completed():
    try:
        view_tasks()
        ans = int(input("Enter the task number that you want mark as not completed: "))
        if to_do_list[ans-1]['status']:
            to_do_list[ans-1]['status'] = False
            print("Successfully marked as not completed")
        else:
            print("The task is already marked as not completed")
    except:
        print("Invalid input")

while True:
    menu()
    num = int(input("Enter an option: "))
    if num==1:
       view_tasks()
       if not to_do_list:
           print("1.continue")
           print('2.exit')
           ans = int(input('Enter an option'))
           if ans == 1:
               continue
           elif ans==2:
               break
           else:
               print("invalid input. So, im continuing")
    elif num==2:
        add_task()
    elif num==3:
        mark_as_completed()
    elif num==4:
        mark_not_completed()
    elif num==5:
        delete()
    elif num==6:
        print("Okay!")
        break


