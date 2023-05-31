from app.common.views import router as common_router
from app.task.views import router as task_router
from fastapi import APIRouter

router = APIRouter()
router.include_router(common_router)
router.include_router(task_router)
