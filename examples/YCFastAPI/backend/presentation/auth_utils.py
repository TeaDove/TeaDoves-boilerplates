from fastapi import Request

from core.settings import security_settings


def get_yc_token(request: Request) -> str:
    if context := request.scope.get("aws.context"):
        return context.token["access_token"]
    elif security_settings.yc_token is not None:
        return security_settings.yc_token
    else:
        raise Exception("no aws context and yc_token not set")
