import logging

from core.models import Log


class LoggingHandler(logging.Handler):
    """Save log messages to MongoDB
    """

    def emit(self, record):
        Log.objects.create(
            message=self.format(record),
        )
