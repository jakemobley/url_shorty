from flask import abort
from .external_api_calls import get_all_links_data, create_new_short_url
from .DataResponse import DataResponse
from interfaces.DataRequestMeta import DataRequestMeta


class DataRes(DataResponse):
    def __init__(self, req, url):
        self.req = req
        self.url = url

    def request_type(self):
        return self.req

    def in_url(self):
        return self.url


def validate_request(request):
    if not issubclass(type(request), DataRequestMeta):
        abort(501, f"Received invalid request object: {request}")


def get_short_url(long_url):
    full_data = get_all_links_data()
    for i in full_data:
        if i.get('destination') == long_url and i.get('shortUrl') is not None:
            return i.get('shortUrl')
        new_short_url = create_new_short_url(long_url)
        return new_short_url


def get_long_url(short_url):
    full_data = get_all_links_data()
    for i in full_data:
        if i.get('shortUrl') == short_url and i.get('destination') is not None:
            return i.get('destination')
        else:
            return None


def triage_request(request):
    if 'get_short' in request.request_type():
        return get_short_url(request.out_url())
    if 'get_long' in request.request_type():
        return get_long_url(request.out_url())


def process_request(request):
    validate_request(request)
    request_type = request.request_type()
    url_to_return = triage_request(request)
    data_response = DataRes(request_type, url_to_return)
    return data_response

