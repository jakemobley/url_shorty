from flask import abort
from .prepare_request import prepare_request_main
from process_data_request.process_request import process_request
from interfaces.DataRequestMeta import DataRequestMeta
from interfaces.DataResponseMeta import DataResponseMeta


def validate_response(response):
    if not issubclass(type(response), DataResponseMeta):
        abort(501, f"Invalid response object received: {response}")


def validate_request(request):
    if not issubclass(type(request), DataRequestMeta):
        abort(501, f"Invalid request object received: {request}")


def send_and_receive_data(request_type, url):
    data_request = prepare_request_main(request_type, url)
    validate_request(data_request)
    data_response = process_request(data_request)
    validate_response(data_response)
    return data_response
