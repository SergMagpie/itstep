from fastapi import APIRouter

from api import records, logins, incomes, outcomes


router = APIRouter()
router.include_router(records.router)
router.include_router(incomes.router)
router.include_router(outcomes.router)
router.include_router(logins.router)
