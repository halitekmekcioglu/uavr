from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from datetime import datetime, timedelta

class SessionTimeoutMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.user.is_authenticated:
            return

        now = datetime.now()
        last_activity = request.session.get('last_activity')

        if last_activity:
            last_activity_time = datetime.strptime(last_activity, '%Y-%m-%d %H:%M:%S.%f')
            if now - last_activity_time > timedelta(seconds=settings.SESSION_COOKIE_AGE):
                request.session.flush()
                return

        request.session['last_activity'] = now.strftime('%Y-%m-%d %H:%M:%S.%f')
