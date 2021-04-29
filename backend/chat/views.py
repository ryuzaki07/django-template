from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Chatserializer
from .models import Chat


@api_view(['GET'])
def GetChats(request):
    chats = Chat.objects.all()
    serializer = Chatserializer(chats, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def CreateChats(request):
    serializer = Chatserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
