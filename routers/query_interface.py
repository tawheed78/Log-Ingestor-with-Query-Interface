from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates
from config import db, convert_to_unix_timestamp, convert_to_utc_timestamp

templates = Jinja2Templates(directory="static")
router = APIRouter()
collection = db['logs']

async def search_logs(query_params):
    result_cursor = collection.find(query_params)
    return await result_cursor.to_list(length=None)

@router.post("/search")
async def search_logs_view(request: Request, filter_field: str = Form(...), filter_value: str = Form(...)):
    if filter_field == 'dateRange':
        from_date_str, to_date_str = filter_value.split(' and ')
        from_date = convert_to_unix_timestamp(from_date_str)
        to_date = convert_to_unix_timestamp(to_date_str)
        query_params = {
            "timestamp": {
                "$gte": from_date,
                "$lte": to_date
            }
        }
    else:
        query_params = {
            filter_field: {
                '$regex': filter_value, '$options': 'i'
                }
            }
    result = await search_logs(query_params)
    for res in result:
        res['timestamp'] = convert_to_utc_timestamp(res['timestamp'])
    return templates.TemplateResponse("index.html", {"request": request, "result": result})