from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# 本モデル CRUD API用クラス
from apiv1.serializers import BookSerializer
from shop.models import Book


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
