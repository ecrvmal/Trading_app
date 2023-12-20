from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from operations.router import get_specific_operations

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="templates")

@router.get("/base")
def get_base_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@router.get("/search")
def get_search_page(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})

@router.get("/search/{operation_type}")
def get_search_page(request: Request, operations=Depends(get_specific_operations)):
            # JS (в search.html)  подставит тип операции из поля ввода в адресную строку,
            # в функцию get_specific_operation  передастся operation type ,
            # далее выполнится operations/get_specific_operation, данные operations подставятся в шаблонизатор
    return templates.TemplateResponse("search.html", {"request": request, "operations": operations["data"]})

