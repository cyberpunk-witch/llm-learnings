#!/usr/bin/env python3

## task

# eventual goal:
## a todo list manager for the command line
## maintains a stack of todo list items
## items have state
## items can have sub-items
## items can be grouped into super-items
## top level items listed in the top list
## items can be popped up or down levels
## items can be urgent 
## items can be important
## items can have values attached
## items can have dates
## items can be filtered
## items with sub-items show in filters if sub-items' tags / values / importance / urgency match filter.

# step 0: write a simple todo list, where I can add, remove, and display items from the commmand line.

import os, re, argparse
from enum import Enum

parser = argparse.ArgumentParser(prog="task", description="a simple command line task manager", epilog="====")

parser.add_argument("-l","--list", help="List tasks", action="store_true")
parser.add_argument("-r", "--remove", help="Delete a task by #", type=int)

class Color(Enum):
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# usage: print(Color.BOLD.value + 'Hello, World!' + Color.END.value)

class TaskType(Enum):
    ITEM = 1
    PROJECT = 2

class TaskList:
    def __init__(self, desc, name='main', parent=None, initial_tasks=[], task_type=TaskType.ITEM):
        self.tasks = []
        self.desc = desc
        self.name = name
        self.parent = parent
        self.task_type = task_type
        self.tasks.extend(initial_tasks)
    def list_tasks(self):
        print('listing tasks')
        iter = 0
        for sometask in self.tasks:
            iter += 1
            if (sometask.task_type == TaskType.ITEM):
                print(str(iter) +". "+sometask.name+"\n")
            if (sometask.task_type == TaskType.PROJECT):
                print(str(iter) +". "+Color.BOLD.value+sometask.name+Color.END.value+"\n")
#instantiate main list

main = TaskList(desc="the main list", name="main", parent=None, initial_tasks=[], task_type=TaskType.PROJECT)
item1 = TaskList(desc="", name="do the dishes", parent=main)
item2 = TaskList(desc="", name="pet the cat", parent=main, task_type=TaskType.PROJECT)
item3 = TaskList(desc="", name="feed the cat", parent=main)
main.tasks=[item1,item2, item3]
#get args
args = parser.parse_args()
myargs = vars(args)

#do stuff
if args.list:
    main.list_tasks()
else:
    if args.remove:
        print('removing task '+main.tasks[args.remove-1].name)
        del main.tasks[args.remove-1]
        print('new list: ')
        main.list_tasks()