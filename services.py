
from models import Status, Task
from datetime import date, timedelta


def overdue_tasks(tasks : list[Task]) -> list[Task]:
    # Вернуть только задачи с просроченными дедлайнами
    only_overdue = []
    for task in tasks:
        result = task.is_overdue()
        if not result:
            continue
        else:
            only_overdue.append(task)
    return only_overdue
        

def deadline_sort(tasks : list[Task]) -> list[Task]:
    # Сортировка по датам дедлайнов
    tasks_sort = sorted(tasks , key = lambda task : task.deadline)
    return tasks_sort



def burning(tasks : list[Task], day : int) -> list[Task]:
    # Поиск задач , дедлайны которых попопадают на определенный промежуток времени , начиная с настоящего момента
    burn_tasks = []

    for task in tasks:
        if task.deadline >= date.today() and task.deadline <= date.today() + timedelta(days=day) and task.status != Status.DONE:
            burn_tasks.append(task)
        else:
            continue

    return burn_tasks



