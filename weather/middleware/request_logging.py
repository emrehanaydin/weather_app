# request_logging.py
from __future__ import annotations

import json
import logging

from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin

from weather.models import RequestLog

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        super().__init__(get_response)

        self.user_reqeusts = {}

    def process_request(self, request):
        try:
            user = request.user
            if not user:
                return {'message': 'User Not Found'}, 504

            user_name = user.username
            path = request.path
            key = f'{user_name}&&{path}'

            if user_name not in self.user_reqeusts:
                self.user_reqeusts[key] = {}

            self.user_reqeusts[key] = dict(
                user=User.objects.get(username=user_name),
                path=path,
                method=request.method,
                ip_address=request.META.get('REMOTE_ADDR', ''),
                user_agent=request.META.get('HTTP_USER_AGENT', ''),
                requested_at=timezone.now(),
                request_body='',
            )
        except Exception as error:
            logger.error(error)

    def process_response(self, request, response):
        try:

            user = request.user
            if not user:
                return {'message': 'User Not Found'}, 504

            user_name = user.username
            path = request.path

            key = f'{user_name}&&{path}'

            self.user_reqeusts[key].update(
                response_body=json.dumps(response.data),
                response_at=timezone.now(),
            )
            data = self.user_reqeusts.pop(key)
            RequestLog(**data).save()
        except Exception as error:
            logger.error(error)

        return response
