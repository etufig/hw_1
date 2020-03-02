#!/usr/bin/python3
from shutil import move

import white as white

from pyrob.api import *


@task
def task_3_1():
  if wall_is_above():
    move()
    up()
  elife not wall_is_beneath():
    move_down()
  elif not wall_is_on_the_left():
    move_left()
  else:
    move_right()


if __name__ == '__main__':
    run_tasks()
