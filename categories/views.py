from rest_framework import viewsets
from categories.models import Category
from categories.serializers import CategorySerializer, SpecificPartsSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class OfficePartsViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.filter(name='Bureautique')
	serializer_class = SpecificPartsSerializer

class GamerPartsViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.filter(name='Gamer')
	serializer_class = SpecificPartsSerializer

class ProfessionnalPartsViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.filter(name='Professionnel')
	serializer_class = SpecificPartsSerializer
