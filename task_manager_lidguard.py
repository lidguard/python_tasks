from datetime import datetime, date
DATETIME_STRING_FORMAT = "%d-%m-%Y"

import os

#define menu functions
def reg_user():
    newusername = input("Enter a username: ")
    newpassword = input("Enter a password: ")
    if newusername in usernames:
        print("Username already taken. Select another option or try again. \n")
    else:
        userfile = open("user.txt", "a")
        userfile.write(f"\n{newusername};{newpassword}")
        print("New user added successfully.")
        userfile.close()

def add_task():
    assigned_user = input("Enter assigned user: ")
    taskname = input("Enter task name: ")
    description = input(f"Enter a short description for {taskname}: ")
    duedate = input(f"Enter the due date of {taskname} (DD-MM-YYYY): ")
    completed = "No"
    print(f"""
    Task saved successfully. 
    User: {assigned_user} 
    Task: {taskname}
    Description: {description} 
    Due date: {duedate} 
    Complete Status: {completed}\n""")
    taskfile = open("tasks.txt", "a")
    taskfile.write(f"{assigned_user},{taskname},{description},{duedate},{completed}\n""")
    taskfile.close()

def view_all():
    taskfile = open("tasks.txt", "r")
    lines = taskfile.readlines()
 #   print(lines)
    for line in lines:
        splitline = line.split(",")
        print(f"""
        User: {splitline[0]}
        Task Name: {splitline[1]}
        Description: {splitline[2]}
        Due Date {splitline[3]}
        Completed? {splitline[4]}""")

#function to read and amend tasks assigned to current user
def view_my():
    taskfile = open("tasks.txt", "r")
    count = 1

    all_tasks = {}
    for line in taskfile:
        split_line = line.split(",")
        all_tasks[count] = split_line
        count += 1

    task_count = 0
    for key in all_tasks:
        task_count += 1
        if username == all_tasks[key][0]:
            print(f"""
                Task Number {str(task_count)}:  
                User: {str(all_tasks[key][0])}
                Task Name: {str(all_tasks[key][1])}
                Description: {str(all_tasks[key][2])}
                Due Date {str(all_tasks[key][3])}
                Completed? {str(all_tasks[key][4])}""")

    edit = input("Enter the number of the task you wish to edit, or '-1' to exit: ")
    if edit == "-1":
        return menu
    else:
        editcomplete = input("Would you like to mark the task as complete or edit the task? (mark or edit) \n")
        if editcomplete == "mark":
            all_tasks[int(edit)][4] = "Yes"

        elif editcomplete == "edit":
            date_edit = input("Enter a new due date for this task: ")
            name_edit = input("Please enter the username for the task: ")
            all_tasks[int(edit)][0] = name_edit
            all_tasks[int(edit)][3] = date_edit

        for i in all_tasks.values():
            print(", ".join(i))

    with open("tasks.txt", "a") as taskfile:
        taskfile.write(", ".join(i))

def generate():
    #this generates task report from task_overview.txt
    #set counters
    current_date = datetime.today()
    task_count = 0
    uncompleted_task = 0
    completed_task = 0
    overdue_task = 0
    user_total_tasks = 0
    user_overdue = 0
    user_completed = 0
    user_uncompleted = 0

    taskfile = open("tasks.txt", "r")

    with open("user.txt", "r") as userfile:
        users = {}
        for line in userfile:
            username, password = line.strip().split(";")
            users[username] = password
        #set user counters and calculate totals
        for username, password in users.items():
            user_total_tasks = 0
            user_overdue = 0
            user_completed = 0
            user_uncompleted = 0

    for line in taskfile:
        split_line = line.split(",")
        task_count += 1

        if "No" in split_line[-1]:
            uncompleted_task += 1
        elif "Yes" in split_line[-1]:
            completed_task += 1
        elif str(current_date.strftime("%d %m %Y")) in split_line[3]:
            overdue_task += 1


        if username in split_line[0]:
            user_total_tasks += 1
            if "No" in split_line[-1]:
                user_uncompleted += 1
            else:
                user_completed += 1

            if str(current_date.strftime("%d %m %Y")) in split_line[3] and "No" in line:
                user_overdue += 1

    #write totals
    with open("task_overview.txt", "w") as taskoverview:
        taskoverview.write(f"""
        The total number of tasks is: {task_count}
        The total number of uncompleted tasks is: {uncompleted_task}
        The total number of completed tasks is: {completed_task}
        The total number of overdue tasks is: {overdue_task}
        {(uncompleted_task / task_count * 100):.2f}% of all tasks are uncompleted
        {(overdue_task / task_count * 100):.2f}% of all tasks are overdue""")
        print(f"The total number of tasks is: {task_count}")
        print(f"The total number of uncompleted tasks is: {uncompleted_task}")
        print(f"The total number of completed tasks is: {completed_task}")
        print(f"The total number of overdue tasks is: {overdue_task}")
        print(f"{(uncompleted_task / task_count * 100):.2f}% of all tasks are uncompleted")
        print(f"{(overdue_task / task_count * 100):.2f}% of all tasks are overdue")

    #calculate and write percentages for the user
    with open("user_overview.txt", "w") as useroverview:
        useroverview.write(f"""
        The total number of tasks assigned to {username} is: {user_total_tasks}
        {username} has been assigned {(user_total_tasks / task_count * 100):.2f}% of all tasks
        {username} has completed {(user_completed / user_total_tasks * 100):.2f}% of their assigned tasks
        {username} must complete {(user_uncompleted / user_total_tasks * 100):.2f}% of their assigned tasks
        {(user_overdue / user_total_tasks * 100):.2f}% of {username}'s assigned tasks are overdue""")
        print(f"The total number of tasks assigned to {username} is: {user_total_tasks}")
        print(f"{username} has been assigned {(user_total_tasks / task_count * 100):.2f}% of all tasks")
        print(f"{username} has completed {(user_completed / user_total_tasks * 100):.2f}% of their assigned tasks")
        print(f"{username} must complete {(user_uncompleted / user_total_tasks * 100):.2f}% of their assigned tasks")
        print(f"{(user_overdue / user_total_tasks * 100):.2f}% of {username}'s assigned tasks are overdue")


def displaystatistics():
    with open("user_overview.txt", "r") as useroverview:
        print("\n *** Here are your statistics *** ")
        for line in useroverview:
            print(line, end="")
    print("\n")

    with open("task_overview.txt", "r") as taskoverview:
        print("\n *** Here are the statistics for all tasks *** ")
        for line in taskoverview:
            print(line, end="")

    print("\n")

#create lists to store login info
usernames = []
passwords = []

if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

userfile = open("user.txt", "r")

for lines in userfile:
    item = lines.strip()
    item = item.split(";")
    usernames.append(item[0])
    passwords.append(item[1])
#print(usernames)
#print(passwords)

userfile.close()

#create login interface
logged_in = False

while not logged_in:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username not in usernames:
        print("Incorrect username")

    elif password not in passwords:
        print("Incorrect password")

    else:
        print(f"Welcome {username}. Please make a selection from the menu below.")
        logged_in = True

#create menu
while logged_in:
        menu = input("r - register new user \n"
                     "a - add task \n"
                     "va - view all tasks \n"
                     "vm - view my tasks \n"
                     "gr - generate reports \n"
                     "ds - display statistics \n"
                     "e - exit \n")

        if menu == 'r':
            reg_user()
        elif menu == "a":
            add_task()
        elif menu == "va":
            view_all()
        elif menu == "vm":
            view_my()
        elif menu == "gr":
            generate()
        elif menu == "ds":
            displaystatistics()
        elif menu == "e":
            exit()



