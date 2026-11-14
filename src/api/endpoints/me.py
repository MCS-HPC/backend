from fastapi import APIRouter, Request, Depends
from ...service.credits import get_balance
from src.api.endpoints.auth import get_current_user

router = APIRouter()

# why isnt this a fucking thing
@router.get("/credit")
async def get_my_credit_balance(
    request: Request,
    current_user: dict = Depends(get_current_user)
):
    return get_balance(request.app.db, current_user["username"])

