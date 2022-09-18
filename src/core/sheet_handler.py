from orm.models import Sheet
from utils.toolkit import Toolkit


class SheetHandler:
    @classmethod
    def post_sheet(cls, title, instrument, category, sheet_files):
        pass

    @classmethod
    def get_sheet_detail(cls, sheet_id):
        pass

    @classmethod
    def get_sheets(cls, keyword, category, instrument, page, per_page, member_id=None):
        conditions = []
        if member_id:
            conditions.append(Sheet.member_id == member_id)
        if keyword:
            conditions.append(Sheet.title.like(f'%{keyword}%'))
        if category:
            conditions.append(Sheet.category == category)
        if instrument:
            conditions.append(Sheet.instrument == instrument)
        sheet = Sheet.query.filter(
            *conditions
        ).order_by(
            Sheet.create_datetime.desc()
        ).paginate(
            page=page,
            per_page=per_page
        )
        pager = Toolkit.make_pager(
            page=page,
            per_page=per_page,
            obj=sheet
        )
        results = list()
        for sheet in sheet.items:
            result = {
                'id': sheet.id,
                'member_id': sheet.member_id,
                'title': sheet.title,
                'author': sheet.author,
                'category': sheet.category,
                'instrument': sheet.instrument,
                'view': sheet.view,
                'download': sheet.download,
                'update_datetime': sheet.update_datetime,
                'create_datetime': sheet.create_datetime,
            }
            results.append(result)
        return results, pager
