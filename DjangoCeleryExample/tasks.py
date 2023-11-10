from .celery import app
from time import sleep


@app.task(name="SimpleTask1", queue="queue1")
def simple_task_1() -> None:
    for i in range(10):
        sleep(0.5)
        print(f"Simple Task 1: {i}")


@app.task(name="SimpleTask2", queue="queue2")
def simple_task_2() -> None:
    for i in range(10):
        sleep(1)
        print(f"Simple Task 2: {i}")
