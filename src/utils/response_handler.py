from flask import jsonify

from utils.error_code import ErrorCode
from utils.errors import ValidationError


class ResponseHandler:
    @staticmethod
    def _validate_results(results):
        if results is False:
            raise ValidationError(error_code=ErrorCode.INVALID_OPERATION)
        if results is None:
            raise ValidationError(error_code=ErrorCode.DATA_MISSING)
        if not (isinstance(results, dict) or isinstance(results, list)):
            raise ValidationError(error_code=ErrorCode.DATA_ERROR)

    @staticmethod
    def _validate_pager(pager):
        if pager is None:
            return

        if not isinstance(pager, dict):
            raise ValidationError(error_code=ErrorCode.DATA_ERROR)

    @classmethod
    def to_json(cls, results, pager=None, code=200):
        if results is True:
            return jsonify({'succeed': True}), code
        cls._validate_results(results=results)
        cls._validate_pager(pager=pager)
        data = {
            'success': True,
            'response': {
                'pager': pager,
                'data': results,
            }
        }
        return jsonify(data), code

    @staticmethod
    def make_pager(page, per_page, obj):
        pager = {
            'page': page,
            'per_page': per_page,
            'total': obj.total,
            'pages': obj.pages,
        }
        return pager
