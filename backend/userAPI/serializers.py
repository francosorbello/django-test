from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    '''Permite pasar de json a model y viceversa'''
    nombre = serializers.CharField(max_length=100)
    edad = serializers.IntegerField()
