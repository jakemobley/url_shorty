from interfaces.DataResponseMeta import DataResponseMeta


class DataResponse(DataResponseMeta):
    """ Simply for concrete classes to inherit from """
    def request_type(self):
        return self.request_type

    def in_url(self):
        return self.out_url
