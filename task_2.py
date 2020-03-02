#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_2():
   move_right(4)
   move_down(3)
   pass


if __name__ == '__main__':
    run_tasks()
