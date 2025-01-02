class NetworkConnectionError(Exception):
    pass


def timeout(seconds: int, max_seconds: int = 3) -> None:
    if seconds > max_seconds:
        raise NetworkConnectionError(
            "Timeout: unable to connect to server ..."
        )
