#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_2():

         move_right()
    pass


if __name__ == '__main__':
    run_tasks()
