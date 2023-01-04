from dataclasses import dataclass

from service.app_service import AppService


@dataclass
class Container:
    app_service: AppService


def init_combat_container():
    return Container(app_service=AppService())
