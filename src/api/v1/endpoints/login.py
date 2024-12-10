from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from motor.core import AgnosticDatabase

from src import crud, models, schemas
from src.api import deps
from src.core import security

router = APIRouter()



"""
https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Authentication_Cheat_Sheet.md
Specifies minimum criteria:
    - Change password must require current password verification to ensure that it's the legitimate user.
    - Login page and all subsequent authenticated pages must be exclusively accessed over TLS or other strong transport.
    - An application should respond with a generic error message regardless of whether:
        - The user ID or password was incorrect.
        - The account does not exist.
        - The account is locked or disabled.
    - Code should go through the same process, no matter what, allowing the application to return in approximately
      the same response time.
    - In the words of George Orwell, break these rules sooner than do something truly barbaric.

See `security.py` for other requirements.
"""


@router.post("/oauth", response_model=schemas.Token)
async def login_with_oauth2(
    db: AgnosticDatabase = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    First step with OAuth2 compatible token login, get an access token for future requests.
    """
    user = await crud.user.authenticate(db, email=form_data.username, password=form_data.password)
    if not form_data.password or not user or not crud.user.is_active(user):
        raise HTTPException(status_code=400, detail="Login failed; incorrect email or password")

    refresh_token = security.create_refresh_token(subject=user.id)
    await crud.token.create(db=db, obj_in=refresh_token, user_obj=user)
    return {
        "access_token": security.create_access_token(subject=user.id),
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }

@router.post("/refresh", response_model=schemas.Token)
async def refresh_token(
    db: AgnosticDatabase = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_refresh_user),
) -> Any:
    """
    Refresh tokens for future requests
    """
    refresh_token = security.create_refresh_token(subject=current_user.id)
    await crud.token.create(db=db, obj_in=refresh_token, user_obj=current_user)
    return {
        "access_token": security.create_access_token(subject=current_user.id),
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }

