# request_logging.py
import json

from django.utils.deprecation import MiddlewareMixin
from django.utils import timezone
from weather.models import RequestLog
from django.contrib.auth.models import User


class RequestLoggingMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        super().__init__(get_response)

        self.user_reqeusts = {}

    def process_request(self, request):
        user = request.user
        if not user:
            return {"message": "User Not Found"}, 504

        user_name = user.username
        path = request.path
        key = f"{user_name}&&{path}"

        if not user_name in self.user_reqeusts:
            self.user_reqeusts[key] = {}

        self.user_reqeusts[key] = dict(
            user=User.objects.get(username=user_name),
            path=path,
            method=request.method,
            ip_address=request.META.get('REMOTE_ADDR', ''),
            user_agent=request.META.get('HTTP_USER_AGENT', ''),
            requested_at=timezone.now(),
            request_body=""
        )

    def process_response(self, request, response):
        try:

            user = request.user
            if not user:
                return {"message": "User Not Found"}, 504

            user_name = user.username
            path = request.path
            key = f"{user_name}&&{path}"

            self.user_reqeusts[key].update(
                response_body=json.dumps(response.data),
                response_at=timezone.now()
            )
            data = self.user_reqeusts.pop(key)
            RequestLog(**data).save()
        except:
            pass
        return response
