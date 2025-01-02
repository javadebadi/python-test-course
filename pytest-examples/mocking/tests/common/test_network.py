import pytest
from mocking.src.common.network import timeout
from mocking.src.common.network import NetworkConnectionError


def test_timeout_not_happens_when_max_seconds_is_not_exceeded():
    # Given seconds and max_seconds
    seconds = 1
    max_seconds = 60

    # When timeout is called
    result = timeout(seconds=seconds, max_seconds=max_seconds)

    # Then no error should happen
    assert result is None


def test_timeout_happens_when_max_seconds_exceeded():
    # Given seconds and max_seconds
    seconds = 10
    max_seconds = 5

    # When timeout is called
    # Then NetworkConnectionError should be raised
    with pytest.raises(NetworkConnectionError):
        timeout(seconds=seconds, max_seconds=max_seconds)
