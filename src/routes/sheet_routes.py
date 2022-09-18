from app import app
from core.sheet_handler import SheetHandler
from utils.auth_tool import AuthTool
from utils.data_validator import DataValidator, DataSchema
from utils.response_handler import ResponseHandler


@app.route('/my-sheets', methods=['GET'])
@DataValidator.validate()
@AuthTool.get_member()
def get_my_sheet_list(payload, member):
    """
    我的譜
    """
    results = SheetHandler.get_sheets(
        keyword=payload.get('keyword'),
        category=payload.get('category'),
        instrument=payload.get('instrument'),
        page=int(payload.get('page', 1)),
        per_page=int(payload.get('per_page', 10)),
        member_id=member.id,
    )
    return ResponseHandler.to_json(results=results)


@app.route('/sheets', methods=['GET'])
@DataValidator.validate()
def get_sheets(payload):
    """
    所有譜
    """
    results = SheetHandler.get_sheets(
        keyword=payload.get('keyword'),
        category=payload.get('category'),
        instrument=payload.get('instrument'),
        page=int(payload.get('page', 1)),
        per_page=int(payload.get('per_page', 10)),
    )
    return ResponseHandler.to_json(results=results)


@app.route('/sheet/<int:sheet_id>', methods=['GET'])
def get_sheet_detail(sheet_id):
    """
    特定譜
    """
    results = SheetHandler.get_sheet_detail(
        sheet_id=sheet_id,
    )
    return ResponseHandler.to_json(results=results)


@app.route('/my-sheet', methods=['PUT'])
@DataValidator.validate(schema=DataSchema.SIGN_IN)
def member_post_sheet(payload):
    """
    上傳譜
    """
    results = SheetHandler.post_sheet(
        title=payload['title'],
        instrument=payload['instrument'],
        category=payload['category'],
        sheet_files=payload['sheet_files']
    )
    return ResponseHandler.to_json(results=results)
