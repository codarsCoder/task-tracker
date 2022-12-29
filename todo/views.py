from django.shortcuts import get_object_or_404  ## ARKA PLANDA TRT CATC YAPIYOR BAŞARILI DEĞİLSE 404 HATASI VERECEK

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet


from .models import Todo
from .serializers import TodoSerializer


@api_view()
def todo_home(request):
    return Response({'home': 'This is todo home page'})


@api_view(['GET', 'POST'])
def todo_list_create(request):
    if request.method == 'GET':
        todos = Todo.objects.filter(is_done=False)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id)   ## ARKA PLANDA TRT CATC YAPIYOR BAŞARILI DEĞİLSE 404 HATASI VERECEK

    if request.method == 'GET':
        # todo = Todo.objects.get(id=id)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TodoSerializer(data=request.data, instance=todo) ### BURADA VERİYİ SERİALİZE ETTİK VE todo İÇİNE KOYDUK İNSTANCE MEVCUT VERİYİ TUTAR VE GELEN VERİYİ KARŞILAŞTIRMADA KULLANILIR , DEĞİŞİKLİK VAR MI BURADAN ANLAŞILIRKİ UPDATE YAPILABİLSİN
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        todo.delete()
        return Response({'message': 'todo deleted succesfully'})
## yukarıdakı kısım function basic , altta ise class ile tanımlandı  BAZEN KARIŞIK EXTRA İŞLEMLER GEREKTİİNDE CLASS YAPISINI ÇÖZEMEYEBİLİRSİN O ZAMAN YUKARIYI KULLAN

class Todos(ListCreateAPIView):
    # queryset = Todo.objects.filter(is_done=False)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetail(RetrieveUpdateDestroyAPIView):
    # queryset = Todo.objects.filter(is_done=False) #yapılmamışları getirecek
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    # lookup_field = 'id'   burada istersek default olarak endpointte  pk şeklinde okunan id ismini  yada başka bir değişkene çevirebiliriz


class TodoMVS(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
