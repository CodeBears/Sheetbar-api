import logging

from flask import jsonify
from schema import SchemaError
from werkzeug.exceptions import NotFound, ServiceUnavailable
from app import app

from utils.error_code import ErrorCode


def make_error_schema(message, error_code):
    _dict = {
        'message': message,
        'code': error_code,
    }
    return _dict


class _BaseError(Exception):
    """
        base error class
    """

    def __init__(self, code=404, message=None, error_code=None):
        super(_BaseError, self).__init__()
        self.code = code
        self.message = message or ErrorCode.get_error_msg(error_code)
        self.error_code = error_code or ErrorCode.BASE_ERROR


class ValidationError(_BaseError):
    def __init__(self, message=None, error_code=None):
        super(ValidationError, self).__init__(code=400, message=message, error_code=error_code)


###############################
#    自訂的Exception Handler   #
###############################

@app.errorhandler(ValidationError)
def handle_validation_error(e):
    _schema = make_error_schema(
        message=e.message,
        error_code=e.error_code
    )
    logging.exception(e.message)
    return jsonify(_schema), e.code


@app.errorhandler(SchemaError)
def handle_schema_error(e):
    message = 'payload error'
    _schema = make_error_schema(
        message=e.autos[0].lower()[:-1],
        error_code=ErrorCode.PAYLOAD_ERROR
    )
    logging.exception(message)
    return jsonify(_schema), e.code


###############################
#   System Exception Handler  #
###############################

@app.errorhandler(NotFound)
def handle_404_error(e):
    error_code = ErrorCode.INVALID_OPERATION
    message = 'endpoint not found'
    _schema = make_error_schema(
        message=message,
        error_code=error_code
    )
    logging.exception(message)
    return jsonify(_schema), 404


@app.errorhandler(ServiceUnavailable)
def handle_503_error(e):
    error_code = ErrorCode.SYSTEM_ERROR
    message = 'service unavailable'
    _schema = make_error_schema(
        message='service unavailable',
        error_code=error_code
    )
    logging.exception(message)
    return jsonify(_schema), 503


@app.errorhandler(Exception)
def handle_500_error(e):
    error_code = ErrorCode.SYSTEM_ERROR
    message = 'internal server error'
    _schema = make_error_schema(
        message=message,
        error_code=error_code
    )
    logging.exception(message)
    return jsonify(_schema), 500
