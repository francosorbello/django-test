from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

from userAPI.serializers import UserSerializer

from .models import User
# Create your views here.

class UserAPIView(APIView):

    serializer_class = UserSerializer

    def get(self,request,format = None,pk=None):
        '''retorna una lista de usuarios o uno especifico cuando se indica su id'''
        if(pk == None):
            usuarios = User.objects.all()
            return Response(list(usuarios.values()))
        else:
            user = User.objects.get(id=pk)
            return Response({
                "id":user.id,
                "nombre":user.nombre,
                "edad":user.edad
            })
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        
        if(serializer.is_valid()):
            postName = serializer.validated_data.get('nombre')
            postAge = serializer.validated_data.get('edad')
            nUser = User(nombre=postName,edad=postAge)
            msg = "Hola " + nUser.nombre
            nUser.save()
            return Response({'message':msg})
        else:
            return Response(serializer.errors)

    def put(self,request,pk=None):
        '''Actualiza un objeto con id pk'''
        user = User.objects.get(id=pk)
        
        msg = "PUT en objeto con nombre "+user.nombre
        return Response({"message":msg})

    def patch(self,request,pk=None):
        '''Actualiza valores de un objeto en vez de por completo'''
        user = User.objects.get(id=pk)
        
        msg = "PATCH en objeto con nombre "+user.nombre
        return Response({"message":msg})

    def delete(self,request,pk=None):

        user = User.objects.get(id=pk)
        user.delete()
        msg = "DELETE en objeto con nombre "+user.nombre
        return Response({"message":msg})