from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializer import BookSerializer

from .models import Book

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_books(request):
    user = request.user
    book = Book.objects.filter(author=user)
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)
