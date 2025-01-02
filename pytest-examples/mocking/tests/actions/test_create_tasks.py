import pytest

from mocking.src.actions.create_task import CreateTaskAction
import mocking.src.actions.create_task
import mocking.src.common.send_task


class TestCreateTaskAction:

    def test(self, monkeypatch):
        # Given data
        data = {"username": "knaph"}

        # And fake_send_to_task_queue
        def fake_send_to_task_queue(data: dict[str, str]) -> None:
            return None

        # And replacing the behavior of send_to_task_queue with fake behavior
        monkeypatch.setattr(
            mocking.src.actions.create_task,
            "send_to_task_queue",
            fake_send_to_task_queue,
        )

        # When CreateTaskAction is performed
        action = CreateTaskAction(data=data)
        result = action.perform()

        # Then the action should be performed successfully and return None
        assert result is None

    @pytest.mark.xfail(
        strict=True, reason="Wrong implementation of the mocking in the test"
    )
    def test_incorrect_patching_of_send_to_task_queue(self, monkeypatch):
        # Given data
        data = {"username": "knaph"}

        # And fake_send_to_task_queue
        def fake_send_to_task_queue(data: dict[str, str]) -> None:
            return None

        # And replacing the behavior of send_to_task_queue with fake behavior
        # THIS IS THE WRONG WAY
        # In CreateTaskAction you have to patch the
        # `mocking.src.actions.create_task.send_to_task_queue`
        # Not the `mocking.src.common.send_task.send_to_task_queue`
        monkeypatch.setattr(
            mocking.src.common.send_task,
            "send_to_task_queue",
            fake_send_to_task_queue,
        )

        # When CreateTaskAction is performed
        action = CreateTaskAction(data=data)
        result = action.perform()

        # Then the action should be performed successfully and return None
        assert result is None
