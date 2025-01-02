from mocking.src.common.send_task import send_to_task_queue


class CreateTaskAction:

    def __init__(self, data: dict[str, str]) -> None:
        self.data = data

    def perform(self):
        return send_to_task_queue(data=self.data)
