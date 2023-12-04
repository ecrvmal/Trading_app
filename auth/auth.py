# https://fastapi-users.github.io/fastapi-users/12.1/configuration/authentication/transports/cookie/
from fastapi_users.authentication import CookieTransport, AuthenticationBackend

cookie_transport = CookieTransport(cookie_name='bonds', cookie_max_age=3600)

# https://fastapi-users.github.io/fastapi-users/12.1/configuration/authentication/strategies/jwt/
from fastapi_users.authentication import JWTStrategy

SECRET = "SECRET"
def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


# https://fastapi-users.github.io/fastapi-users/12.1/configuration/authentication/backend/
auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)


