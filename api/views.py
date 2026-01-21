
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action

from api.serialize import CarSerializer
from cars.models import Car

# Create your views here.

class CarList(APIView):

    @action(methods=['get'], detail=False)
    def get(self, request, format=None):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    @action(methods=['post'], detail=False)
    def post(self, request, format=None):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarDetail(APIView):
    def get_object(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404

    @action(methods=['get'], detail=False) 
    def get(self, request, pk, format=None):
        car = self.get_object(pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)
    
    @action(methods=['put'], detail=False)
    def put(self, request, pk, format=None):
        car = self.get_object(pk)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['delete'], detail=False)
    def delete(self, request, pk, format=None):
        car = self.get_object(pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)