from rest_framework_simplejwt.authentication import JWTAuthentication

class CustomJWTAuthenticationMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        user = JWTAuthentication().authenticate(request)
        if user is not None:
            request.user = user

        response = self.get_response(request)

        return response
