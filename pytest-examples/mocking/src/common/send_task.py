import time
from .network import timeout


def send_to_task_queue(data: dict[str, str]) -> None:
    """simulates sending some data to a task queue
    such as AWS SQS or Google PubSub
    """
    seconds = 0
    for _ in range(1000):
        print(">", end="", flush=True)
        time.sleep(1)
        seconds += 1
        timeout(seconds=seconds)
