import logging
from django.http import JsonResponse
from global_variable.status_code import StatusCode


class BaseController:
    logger = logging.getLogger(__name__)

    @staticmethod
    def handle_success(data = None, message: str = "Success"):
        response_data = {
            "message": message,
            "status": StatusCode.SUCCESS,
        }
        if data is not None:
            response_data["data"] = data
        return JsonResponse(response_data)

    @staticmethod
    def handle_error(data = None, message: str = "Error", status: int = StatusCode.INTERNAL_SERVER_ERROR):
        response_data = {
            "status": status,
            "message": message,
        }
        if data is not None:
            response_data["data"] = data
        return JsonResponse(response_data, status=status)