from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import authentication, permissions, status, generics
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import User
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import signals as log_signals
from django_jwt_auth.settings import JWT_AUTH



class CreateUserAPIView(APIView):

    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserRetriveUpdateAPIView(generics.RetrieveUpdateAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):

        serializer = self.serializer_class(request.data)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):

        serializer_data = request.data.get('user', {})

        serializer = UserSerializer(request.user, data=serializer_data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.AllowAny, ])
def authenticate_user(request):

    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    try:
        email = request.data['email']
        password = request.data['password']

        user = User.objects.get(email=email, password=password)

        if user:
            try:
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                user_details = {}
                user_details['name'] = "%s %s" % (user.first_name, user.last_name)
                user_details['token'] = token
                log_signals.user_logged_in.send(sender=user.__class__, request=request, user=user)

                return Response(user_details, status=status.HTTP_200_OK)
            
            except Exception as e:
                raise e
        else:
            res = {
                'error': 'can not authenticate with given credentials or account has been deactivated'
            }

            return Response(res, status=status.HTTP_403_FORBIDDEN)

    except KeyError:
        res = {'error': 'please provide an email and a password'}
        return Response(res)