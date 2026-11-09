from dataclasses import dataclass
import sqlite3
from models import Task, Status
from datetime import date


@dataclass
class TaskRepo:
    def __init__(self, db_path : str):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute("""CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        title TEXT ,
        status TEXT NOT NULL,
        deadline TEXT NOT NULL
        )
          """)
        self.conn.commit()

    def add_task(self, task : Task) -> bool:
        # добавление новой задачи в бд
        
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO tasks (id , title , status, deadline) VALUES (?,?,?,?)", (task.id , task.title, task.status.value, task.deadline.isoformat(),))

            return cursor.rowcount > 0
    


        
    def get_task_by_id(self, task_id : int ) -> Task | None:
        # найти задачу по id 
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        task = cursor.fetchone()
        task_obj = Task(task[0], task[1], Status(task[2]), date.fromisoformat(task[3])) if task is not None else None
        return task_obj

        
    def get_all_tasks(self) -> list[Task]:
        # получить список всех задач в базе
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM tasks ")
        tasks = cursor.fetchall()
        task_list = []
        for id, title, status, dat in tasks:
            task = Task(id, title, Status(status), date.fromisoformat(dat))
            task_list.append(task)

        return task_list


    def set_status(self, id : int , status : Status) -> bool:
        # изменить сатус задачи
        
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (status.value, id,))
            return cursor.rowcount>0

        


