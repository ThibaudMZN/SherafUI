import sheraf

from random import random

import sheraf
from models.anything import Something, TodoItem, InlineAddendum
from datetime import date


class SherafDBManager():

    def __init__(self):
        self.populate_database()

    def get_data_from_type(self, clazz):
        # get_data_from_type(Something)
        return list(clazz.all())

    @classmethod
    def populate_database(cls):
        anything_db = sheraf.Database()
        with anything_db.connection(commit=True):
            for i in range(10):
                todos = [TodoItem.create(
                    priority=i,
                    age=int(random() * 10),
                    content=f"Content number {i}",
                ) for i in range(4)]

                addendums = [
                    InlineAddendum.create(creation_date=date.fromisoformat(f"2019-12-0{i}")) for i in range(1, 4)
                ]

                Something.create(
                    name=f"thing-{i}",
                    todo_list=todos,
                    inline_addendums=addendums
                )

        with anything_db.connection(commit=True):
            things = list(Something.all())
            length = len(things)
            for i in range(length):
                things[i].friends[f"{(i+1)%length}"] = things[(i+1) % length]
                things[i].friends[f"{(i+2)%length}"] = things[(i+2) % length]


class InlineAddendum(sheraf.InlineModel):
    creation_date = sheraf.DateAttribute()


class TodoItem(sheraf.Model):
    table = "todo"
    priority = sheraf.IntegerAttribute()
    age = sheraf.IntegerAttribute()
    content = sheraf.StringAttribute()


class Something(sheraf.Model):
    table = "something"
    name = sheraf.StringAttribute()
    todo_list = sheraf.SmallListAttribute(
        sheraf.ModelAttribute("samples.anything.TodoItem"))
    friends = sheraf.SmallDictAttribute(
        sheraf.ModelAttribute("samples.anything.Something"))
    inline_addendums = sheraf.SmallListAttribute(
        sheraf.InlineModelAttribute(model=InlineAddendum))
