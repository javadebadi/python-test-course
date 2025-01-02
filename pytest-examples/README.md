# Pytest Examples


# [Mocking with `monkeypatch`](./mocking/)
Mocking a function was always confusing to me especially regarding to its imports. Sometimes I was mocking the function from where it defined and sometimes it was working and sometimes not. This example shows how we should mock a function. Here is the summary of what you should notice when reviewing this example.

Here is the situation:
- function named `send_to_task_queue` is defined at `mocking.src.common.send_task.py`
- Class named `CreateTaskAction` is defined at `mocking.src.actions.create_task.py` and has used `send_to_task_queue` in its `perform` method
- Class named `CreateTaskApi` is defined at `mocking.src.apis.create_task.py` and has used `CreateTaskAction.perform` in its `post` method

To patch a function (`send_to_task_queue`), you need to patch it in the module **where it is used**, not necessarily where it is defined or where a higher-level method (like `post` in class `CreateTaskApi`) calls another method that ultimately invokes the function. Since function (`send_to_task_queue`) is used by `CreateTaskAction` in `mocking.src.actions.create_task`, that is where the patching needs to happen, even if the higher-level method (like `post` in class `CreateTaskApi`) is in a different module (`mocking.src.apis.create_task`).