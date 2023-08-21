from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import AppUserSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from breweries.middleware import CustomJWTAuthenticationMiddleware
from rest_framework_simplejwt.authentication import JWTAuthentication
import requests

from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from .models import AppUser

@api_view(['POST'])
def register(request):
    """
    Registers the user by username and password.
    """
    if request.method == 'POST':
        try:
            # Deserialize data.
            serializer = AppUserSerializer(data=request.data)

            try:
                # Check if the user with the same username already exists.
                existing_user = AppUser.objects.get(username=request.data.get('username'))
                return Response({'error': 'User with this username already exists.'}, status=status.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                # User does not exist, continue with registration
                pass  

            if serializer.is_valid():
                # Save user
                user = serializer.save()  
                return Response({'user': user.username}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            print(e)
            return Response({'error': 'An error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def login(request):
    """
    Returns JWT if the username and password exist and match.
    """
    if request.method == 'POST':
        try:

            username = request.data.get('username')
            password = request.data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                return Response({'token': access_token}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            print(e)
            return Response({'error': 'Problem'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def breweries(request):
    """
    Sends request to the api.openbrewerydb if user is authenticated.
    """
    if request.method == 'GET':
        query_param = request.GET.get('query')
        if query_param:
            url = f'https://api.openbrewerydb.org/breweries/search?query={query_param}'
        else:
            url = 'https://api.openbrewerydb.org/breweries'

        response = requests.get(url)
        data = response.json()
        return Response(data)
