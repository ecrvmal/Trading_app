from fastapi import APIRouter, BackgroundTasks, Depends

from auth.base_config import current_user

from .tasks import send_email_report_dashboard
# from ..auth.models import User

router = APIRouter(prefix="/report")

# for testing purposes:
# current_user = User()
# current_user.id = 1
# current_user.email = 'user@mail.ru'
# current_user.username = 'user'
# current_user.registered_at = '2023-12-17 16:00:44.618'
# current_user.role_id = 1
# current_user.hashed_password = '$2b$12$5FtNSnGGpS1HTz8js9t.v.AfJ8rYKg6gvpuOyNxFzWVr8uK1IO6pu'
# current_user.is_active = True
# current_user.is_superuser = False
# current_user.is_verified = True

# via background:
# @router.get("/dashboard")
# def get_dashboard_report(background_tasks: BackgroundTasks, user=Depends(current_user)):
#                          variable          class             only authorized user
def get_dashboard_report(background_tasks: BackgroundTasks):
    # 500 ms - Задача выполняется на фоне FastAPI в event loop'е или в другом треде
    # background_tasks.add_task(send_email_report_dashboard, user.username)         this with current_user
    background_tasks.add_task(send_email_report_dashboard, 'Vlad')
    return {
        "status": 200,
        "data": "Письмо отправлено",
        "details": None
    }

# Normal:
# @router.get("/dashboard")
# # def get_dashboard_report(user=Depends(current_user)):
# def get_dashboard_report():
#     # 1400 ms - Клиент ждет
#     send_email_report_dashboard("Igor")
#     return {
#         "status": 200,
#         "data": "Письмо отправлено",
#         "details": None
#     }


# via celery  .delay
@router.get("/dashboard")
# def get_dashboard_report(user=Depends(current_user)):
def get_dashboard_report():
    # 600 ms - Задача выполняется воркером Celery в отдельном процессе
    send_email_report_dashboard.delay('Vlad')
    return {
        "status": 200,
        "data": "Письмо отправлено",
        "details": None
    }
