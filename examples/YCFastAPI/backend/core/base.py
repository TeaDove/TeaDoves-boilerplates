from logging import _nameToLevel
from typing import Any, Union

import structlog
from aws_lambda_powertools import Logger, Metrics, Tracer
from aws_lambda_powertools.metrics import MetricUnit  # noqa: F401

from core.settings import app_settings, settings


def _get_logger() -> Union[Logger, Any]:
    if app_settings.local_run:
        structlog.configure(
            wrapper_class=structlog.make_filtering_bound_logger(_nameToLevel[settings.log_level]),
        )
        return structlog.get_logger()
    else:
        return Logger()


logger = _get_logger()
metrics: Metrics = Metrics()
tracer: Tracer = Tracer()
