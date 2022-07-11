from rest_framework import serializers
from myAPI.models import Writer, Book


class BookNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', ]


class WriterSerializer(serializers.ModelSerializer):
    books = BookNestedSerializer(many=True, read_only=True)

    class Meta:
        model = Writer
        fields = ['id', 'name', 'age', 'books']


class WriterNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = ['id', 'name', 'age']


class BookReadSerializer(serializers.ModelSerializer):
    writer = WriterNestedSerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'


class BookWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class WriterSerializerWithBooksId(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Writer
        fields = ['id', 'name', 'age', 'books']
