import pytest
import mocking.src.common.send_task


@pytest.mark.xfail(
        strict=True,
        reason=(
            "By design we set the default behavior of"
            " `send_to_task_queue` result to an error."
            " This simulates error happens in network connection."
            )
)
def test_send_to_task_queue_failed():
    # Given data
    data = {
        "username": "knaph",
    }
    # When send_to_task_queue is called
    result = mocking.src.common.send_task.send_to_task_queue(data=data)

    # Then result should be None
    assert result is None


def test_send_to_task_queue(monkeypatch):
    # Given data
    data = {
        "username": "knaph",
    }

    # And fake_send_to_task_queue
    def fake_send_to_task_queue(data: dict[str, str]) -> None:
        return None

    # And replacing the behavior of send_to_task_queue with fake behavior
    monkeypatch.setattr(
        mocking.src.common.send_task,
        "send_to_task_queue",
        fake_send_to_task_queue,
    )

    # When send_to_task_queue is called
    result = mocking.src.common.send_task.send_to_task_queue(data=data)

    # Then result should be None
    assert result is None
