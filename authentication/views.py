from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import auth
import jwt
from django.conf import settings
from .models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, force_text, DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage

def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Activate your account'
    email_body = render_to_string('authentication/activate.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
    })

    email = EmailMessage(subject=email_subject, body=email_body,
                         from_email=settings.EMAIL_FROM_USER,
                         to=[user.email]
                         )


    if not settings.TESTING:
        email.send()




class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(email=serializer.data['email'])

            print(user)

            send_activation_email(user, request)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        username = data.get('email', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user:
            serializer = LoginSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        



class VerifyEmail(GenericAPIView):

    def get(self, request,uidb64,token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))

            user = User.objects.get(pk=uid)

        except Exception as e:
            user = None

        if user and generate_token.check_token(user, token):
            user.is_verified = True
            user.save()
            return Response({'detail': 'Email verified'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Token is invalid'}, status=status.HTTP_401_UNAUTHORIZED)
     
