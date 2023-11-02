from django.shortcuts import render, redirect
from django.http import Http404
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import User


class SignUpView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class GetUserView(APIView):
    
    def get_user(self, user_id):
        try:
            return User.objects.get(id = user_id)
        except User.DoesNotExist:
            raise Http404
        
    def get(self, request, user_id):
        user = self.get_user(user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)