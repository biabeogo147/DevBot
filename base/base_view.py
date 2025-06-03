import logging
from django.core import serializers
from django.http import JsonResponse
from global_variable.status_code import StatusCode


class BaseView:
    logger = logging.getLogger(__name__)

    @staticmethod
    def to_json(data):
        """
        Converts a Django QuerySet or model instance to JSON format.

        Args:
            data: Django QuerySet or model instance to be serialized.

        Returns:
            str: JSON string representation of the data.
        """
        return serializers.serialize('json', data)


    def handle_success(self, data = None, message: str = "Success"):
        response_data = {
            "message": message,
            "status": StatusCode.SUCCESS.value,
        }
        if data is not None:
            json_data = self.to_json(data)
            response_data["data"] = json_data
        return JsonResponse(response_data)


    def handle_error(self, data = None, message: str = "Error", status: StatusCode = StatusCode.INTERNAL_SERVER_ERROR):
        response_data = {
            "status": status.value,
            "message": message,
        }
        if data is not None:
            json_data = self.to_json(data)
            response_data["data"] = json_data
        return JsonResponse(response_data, status=status)