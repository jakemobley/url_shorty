from interfaces.DataRequestMeta import DataRequestMeta
from send_and_receive_data.DataRequest import DataRequest
from flask import abort


class DataReq(DataRequest):
    def __init__(self, req, url):
        self.req = req
        self.url = url

    def request_type(self):
        return self.req

    def out_url(self):
        return self.url


def validate_request(request):
    if not issubclass(type(request), DataRequestMeta):
        abort(501, f"Invalid request object: {request}")


def prepare_request_main(request_type, in_url):
    data_req = DataReq(request_type, in_url)
    validate_request(data_req)
    return data_req
