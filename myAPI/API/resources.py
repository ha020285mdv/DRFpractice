from django.db.models import QuerySet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from myAPI.API.serializers import WriterSerializer, BookReadSerializer, BookWriteSerializer, WriterSerializerWithBooksId
from myAPI.models import Writer, Book


class WriterViewSet(ModelViewSet):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.request.method == 'GET':
            book_name = self.request.query_params.get('book_name')
        if book_name:
            queryset = queryset.filter(books__title__icontains=book_name).distinct()
        else:
            queryset = queryset.all()
        return queryset

    @action(methods=['get'], detail=True)
    def with_books_id(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = WriterSerializerWithBooksId(instance)
        return Response(serializer.data)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookReadSerializer
        return BookWriteSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.request.method == 'GET':
            author_age = self.request.query_params.get('author_age')
        queryset = queryset.filter(writer__age__gte=int(author_age)) if author_age else queryset.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(title=serializer.validated_data.get('title') + '!')
