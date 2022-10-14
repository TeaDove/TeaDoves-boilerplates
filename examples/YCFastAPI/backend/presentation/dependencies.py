from service.service_app import ServiceApp

_service_app = ServiceApp()


def get_service_app():
    return _service_app
