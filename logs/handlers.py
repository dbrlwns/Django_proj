import logging

from django.apps import apps

class LogHandler(logging.Handler):

    def emit(self, record): # logger 자동호출 함수
        try:
            log = apps.get_model('logs', 'Log')
            log.objects.create(
                level=record.levelname,
                logger_name=record.name,
                message=record.getMessage(),
            )
        except Exception:
            pass