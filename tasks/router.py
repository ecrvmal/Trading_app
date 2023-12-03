from fastapi import APIRouter, BackgroundTasks, Depends
from auth.base_config import current_user
from .tasks import send_email_report_dashboard

router = APIRouter(prefix="/report")


# with normal programm
@router.get("/dashboard1")
def get_dashboard_report(background_tasks: BackgroundTasks, user=Depends(current_user)):
    # 1400 ms - Клиент ждет
    send_email_report_dashboard(user.username)  # usual subprogramm sendemail
    return {
        "status": 200,
        "data": "Письмо отправлено",
        "details": None }

# with background tasks
@router.get("/dashboard2")
def get_dashboard_report(background_tasks: BackgroundTasks, user=Depends(current_user)):
    # 500 ms - Задача выполняется на фоне FastAPI в event loop'е или в другом треде
    background_tasks.add_task(send_email_report_dashboard, user.username)   # background task in fastapi
    return {
        "status": 200,
        "data": "Письмо отправлено",
        "details": None  }

# with redis > celery
@router.get("/dashboard3")
def get_dashboard_report(user=Depends(current_user)):
    # 600 ms - Задача выполняется воркером Celery в отдельном процессе
    send_email_report_dashboard.delay(user.username)
    return {
        "status": 200,
        "data": "Письмо отправлено",
        "details": None }
