import sys
from models import Task, Status
from db_repo import TaskRepo
from services import deadline_sort, burning, overdue_tasks
from datetime import date


def status_from_menu(num : int) -> Status:
    # Выбор status через условие
    if num == 1:
        status = Status.DONE
    elif num == 2:
        status = Status.DOING
    elif num == 3:
        status = Status.TODO
    return status


def controller():
    # контроллер программы 

    if len(sys.argv) < 2:
        return

    command = sys.argv[1]
    task_keeper = TaskRepo("task_base.db")

    if command == "--add":
        print("add params to add task")
        id = task_keeper.get_all_tasks()[-1].id + 1
        title = input("choose title: ")
        num = int(input("choose status 1-done / 2- doing/ 3- todo: "))
        status = status_from_menu(num)
        print("choose deadline date")
        year = int(input("year: "))
        month = int(input("month: "))
        day = int(input("day: "))
        task = Task(id, title, status, date(year, month, day))
        result = task_keeper.add_task(task)
        if result:
            print("succes")
        else:
            print("error")

    elif command == "--get_all":
        result = task_keeper.get_all_tasks()
        for task in result:
            print(task)

    elif command == "--by_id":
        task_id = int(input("choose tasks id to search: "))
        result = task_keeper.get_task_by_id(task_id)
        if result:
            print(result)
        else:
            print("nothing found")

    elif command == "--set_stat":
        task_id = int(input("choose tasks id to search: "))
        num = int(input("choose status 1-done / 2- doing/ 3- todo: "))
        status = status_from_menu(num)
        result = task_keeper.set_status(task_id, status)
        if result:
            print("success")
        else:
            print("error")

    elif command == "--get_over":
        tasks = task_keeper.get_all_tasks()
        over_tasks = overdue_tasks(tasks)
        if len(over_tasks) != 0:
            for task in over_tasks:
                print(task)
        else:
            print("nothing was found")

    elif command == "--burn":
        days = int(input("choose days gap to sort: "))
        tasks = task_keeper.get_all_tasks()
        gap_tasks = burning(tasks, days)
        if len(gap_tasks) != 0:
            for task in gap_tasks:
                print(task)
        else:
            print("nothing was found")

    elif command == "--line_sort":
        tasks = task_keeper.get_all_tasks()
        result = deadline_sort(tasks)
        for i in result:
            print(i)
    else:
        print(f"ivalid command: {command}")


controller()
        


    