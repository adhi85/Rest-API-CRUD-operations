from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer
from . models import Book
# Create your views here.


@api_view(['GET'])
def home(request):
    list = {
        "List-Books : /book-list/",
        'Create : /book-create/',
        'Read : /book-view/<int:pk>/',
        'Update : /book-update/<int:pk>/',
        'Delete : /book-delete/<int:pk>/'
    }

    return Response(list)


# View all books
@api_view(['GET'])
def bookList(request):
    author = request.query_params.get('author', None)
    category = request.query_params.get('category', None)
    books = Book.objects.all().order_by('-id')
    if author:
        books = books.filter(author=author)
    if category:
        books = books.filter(category=category)
    if books:
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    else:
        return Response({})


@api_view(['GET'])
def bookView(request, pk):
    books = Book.objects.get(id=pk)
    serializer = BookSerializer(books, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def bookCreate(request):
    serializer = BookSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def bookUpdate(request, pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(instance=book, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def bookDelete(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()

    return Response("Book is successfully deleted ")
