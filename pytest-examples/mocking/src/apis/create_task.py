from .base import Request
from .base import Response
from mocking.src.actions.create_task import CreateTaskAction


class CreateTaskApi:

    def post(self, request: Request) -> Response:
        data = request.body
        CreateTaskAction(data=data).perform()
        return Response(body={}, status=201)
