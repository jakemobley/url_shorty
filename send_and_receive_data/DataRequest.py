from interfaces.DataRequestMeta import DataRequestMeta


class DataRequest(DataRequestMeta):
    """ Simply for concrete classes to inherit from """
    def request_type(self):
        return self.request_type

    def out_url(self):
        return self.out_url
