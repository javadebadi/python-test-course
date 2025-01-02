from mocking.src.apis.create_task import CreateTaskApi
from mocking.src.apis.base import Request
import mocking.src.actions.create_task


class TestCreateTaskApi:

    def test_post(self, monkeypatch):
        # Given a Request data
        request = Request(body={"username": "knaph"})

        # And fake_send_to_task_queue
        def fake_send_to_task_queue(data: dict[str, str]) -> None:
            return None

        # And replacing the behavior of send_to_task_queue with fake behavior
        monkeypatch.setattr(
            mocking.src.actions.create_task,
            "send_to_task_queue",
            fake_send_to_task_queue,
        )

        # When
        response = CreateTaskApi().post(request=request)

        # Then I should get response with status 201
        assert response.status == 201
