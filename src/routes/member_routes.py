from app import app
from core.member_handler import MemberHandler
from utils.data_validator import DataValidator, DataSchema
from utils.response_handler import ResponseHandler


@app.route('/sign-in', methods=['POST'])
@DataValidator.validate(schema=DataSchema.SIGN_IN)
def member_sign_in(payload):
    """
    用戶登入
    """
    results = MemberHandler.sign_in(
        email=payload['email'],
        password=payload['password'],
    )
    return ResponseHandler.to_json(results=results)


@app.route('/sign-up', methods=['POST'])
@DataValidator.validate(schema=DataSchema.SIGN_UP)
def member_register(payload):
    """
    用戶註冊
    """
    results = MemberHandler.sign_up(
        email=payload['email'],
        username=payload['username'],
        password=payload['password'],
    )
    return ResponseHandler.to_json(results=results)
