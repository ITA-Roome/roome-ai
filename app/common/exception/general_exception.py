from app.common.status.error_status import ErrorStatus


class GeneralException(Exception):

    def __init__(self, status: ErrorStatus, data=None):
        super().__init__(status.message)
        self.status = status
        self.data = data
