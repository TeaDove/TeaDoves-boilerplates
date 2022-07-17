from dependency_injector import containers, providers

from service.app_service import AppService


class ServicesContainer(containers.DeclarativeContainer):
    app_service = providers.Singleton(
        AppService,
    )


class ApplicationContainer(containers.DeclarativeContainer):
    services = providers.Container(ServicesContainer)

    wiring_config = containers.WiringConfiguration(
        modules=[
            "presentation.router",
        ]
    )
