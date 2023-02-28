import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration
from decouple import config
from logging import ERROR


sentry_logging = LoggingIntegration(level=ERROR, event_level=ERROR)


def start_sentry():
    sentry_sdk.init(
        dsn=config("SENTRY_DSN"),
        environment=config("EC2_NAME"),
        integrations=[sentry_logging],
        send_default_pii=True,
        traces_sample_rate=0.01,
    )
