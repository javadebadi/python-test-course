class Request:

    def __init__(self, body: dict[str, str]) -> None:
        self.body = body


class Response:
    def __init__(
        self, body: dict[str, str] | None = None, status: int = 200
    ) -> None:
        if body is None:
            body = {}
        self.body = body
        self.status = status


class BaseApi:

    def post(self, request: Request) -> Response:
        return Response()
