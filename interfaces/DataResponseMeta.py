import abc


class DataResponseMeta(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def request_type(self):
        """Return the type of url we are requesting (short or long)"""
        return

    @abc.abstractmethod
    def in_url(self):
        """Return the known url value we are looking for a match for"""
        return
