from django.shortcuts import render
# Create your views here.
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Task
from .serializers import UserRegisterSerializer, TaskSerializer


# View 1 - Register
class RegisterView(generics.CreateAPIView): #pre built it already know how to create a objects(crud operations)
    queryset = User.objects.all()#tell which objects to work with
    serializer_class = UserRegisterSerializer#tells which serializer is used for this view, we need a serializers to validate incoming data and save it
    permission_classes = [permissions.AllowAny]#any one can access the end point tokens(becuase when new user create they wont have any token)


# View 2 - Login
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        
        return Response(
            {'error': 'Invalid credentials'},
            status=status.HTTP_401_UNAUTHORIZED
        )


# View 3 - List and Create Tasks
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# View 4 - Retrieve, Update, Delete a Task
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):#returns only when task belong to the current user
        return Task.objects.filter(user=self.request.user)
