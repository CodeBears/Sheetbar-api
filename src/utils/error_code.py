class ErrorCode:
    SYSTEM_ERROR = 100
    SIZE_ERROR = 101
    INVALID_TOKEN = 102
    EXPIRED_TOKEN = 103
    HEADER_FORMAT_ERROR = 104
    DATA_ERROR = 200
    DATA_MISSING = 201
    INVALID_OPERATION = 202
    SCHEMA_ERROR = 203
    USERNAME_OR_PASSWORD_WRONG = 204
    MEMBER_IS_EXIST = 205
    MEMBER_IS_NOT_EXIST = 206
    PAYLOAD_ERROR = 207

    @staticmethod
    def get_error_key(error_code):
        for key, value in ErrorCode.__dict__.items():
            if key.startswith('_'):
                continue
            if value == error_code:
                return key
        return None

    @staticmethod
    def get_error_msg(error_code):
        for key, value in ErrorCode.__dict__.items():
            if key.startswith('_'):
                continue
            if value == error_code:
                msg = ' '.join(key.split('_')).title()
                return msg
        return None
