from service.app_service import AppService
from shared.containers import init_combat_container


def get_app_service() -> AppService:
    return container.app_service


container = init_combat_container()
