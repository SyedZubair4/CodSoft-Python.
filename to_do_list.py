import sys
import emoji

#initialization
choice=int(input('Welcome'+emoji.emojize(":smiling_face_with_open_hands:")+'''Have a GOOD DAY!
These are the options we are providing to you for your daily Tasks!
Available Options-->
Please select your Choice\n'''+
'1) Add' +emoji.emojize(":smiling_face_with_halo:") +
'\n2) Delete' +emoji.emojize(":relieved_face:")+
'\n3) Mark as Completed' +emoji.emojize(":face_exhaling:") +
'\n4) View Tasks' +emoji.emojize(":eyes:") +
'\n5) To Quit ''' + emoji.emojize(":pleading_face:")+'\n'))

#functions defining section

#used for updating the choice variable
def start():
    global choice
    choice=int(input('Enter your choice:'))
    return

#for adding tasks
def add_task():
    task=input('Enter you task:')
    tasks.append(task)
    start()
    return

#for deleting tasks
def delete_task():
    option=int(input('Enter your task number:'))
    tasks.pop(option-1)
    print('Tasks number ' + str(option) + ' has been removed successfully')
    start()
    return

#for viewing tasks
def view_tasks():
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")
    start()
    return

#for marking a task as completed or done
def done():
    option=int(input('Enter the task number which you want to mark as completed:'))
    tasks[option-1]='[completed]' + tasks[option-1]
    a=input('Tasks has been marked do you want to view it? (y/n)')
    if a=='y':
        view_tasks()
    start()
    return



tasks=[]
point=0
while True:
    if point==1:
        choice=int(input('You have entered an invalid '
                     'Choice please select a valid choice'+emoji.emojize(":upside-down_face:")))
        point=0

    if choice == 1:
        add_task()
    elif choice == 2:
        delete_task()
    elif choice == 3:
        show = input('Do you want to show your TASKS (y/n)')
        if show == 'y':
            view_tasks()
        else:
            done()
    elif choice == 4:
        view_tasks()
    elif choice == 5:
        sys.exit()

    else:
        print('Please enter valid input' + emoji.emojize(":expressionless_face:"))
        point = 1
