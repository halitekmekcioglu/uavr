from django.urls import reverse
from django.shortcuts import redirect

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if not request.user.is_authenticated and not request.path.startswith(reverse('login')) and not request.path.startswith(reverse('signup')):
            return redirect('login')  # Redirect to the login page if the user is not authenticated
        return response
