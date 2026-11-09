from dataclasses import dataclass
from datetime import date
from enum import Enum

class Status(Enum):
    TODO = "todo"
    DONE = "done"
    DOING = "doing"

@dataclass
class Task:
    id : int
    title : str
    status : Status
    deadline : date 

    def is_overdue(self):
        return self.deadline < date.today() and self.status != Status.DONE

