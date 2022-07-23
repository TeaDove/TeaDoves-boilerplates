from logging import _nameToLevel
from typing import Any, Union

from aws_lambda_powertools import Logger, Metrics, Tracer
from aws_lambda_powertools.metrics import MetricUnit  # noqa: F401

import structlog
from core.settings import app_settings, settings

structlog.configure(
    wrapper_class=structlog.make_filtering_bound_logger(_nameToLevel[settings.log_level]),
)
logger: Union[Logger, Any] = structlog.get_logger() if app_settings.local_run else Logger()
metrics: Metrics = Metrics()
tracer: Tracer = Tracer()
