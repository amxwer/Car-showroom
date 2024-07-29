from fastapi import APIRouter, Depends

from auth.base_config import current_user


from tasks.tasks import send_email_notification

router = APIRouter(prefix="/configuration",
                   tags=["configuration"])

@router.get("/")
async def get_configuration(user = Depends(current_user)):
    send_email_notification(user.username)
    return {
        "status":200,
        "data": "Send configuration",
        "details":None

    }