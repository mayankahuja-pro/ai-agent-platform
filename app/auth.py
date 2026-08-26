from fastapi import Header, HTTPException


async def get_current_user(
    authorization: str | None = Header(
        default=None
    ),
):

    if not authorization:

        raise HTTPException(
            status_code=401,
            detail="Authentication required",
        )

    if not authorization.startswith(
        "Bearer "
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid authorization header",
        )

    token = authorization.replace(
        "Bearer ",
        "",
        1,
    )

    if token != "demo-token":

        raise HTTPException(
            status_code=401,
            detail="Invalid token",
        )

    return {
        "user_id": "demo-user"
    }