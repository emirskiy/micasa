from django.shortcuts import render
from .models import User
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserModelSerializer, LoginSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class LoginApi(APIView):
    
    serializer_class = LoginSerializer

    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data = data)
            if serializer.is_valid():
                email = serializer.data['email']
                password = serializer.data['password']


                user = authenticate(email=email, password=password)

                if user is None:

                    return Response({
                        'status': 400,
                        'message': 'invalid password',
                        'data': serializer.errors
                    })
                
                refresh = RefreshToken.for_user(user)

                return {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                }

            return Response({
                        'status': 400,
                        'message': 'something went wrong',
                        'data': serializer.errors
                    })
        
        except Exception as e:
            print(e)
