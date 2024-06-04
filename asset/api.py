from rest_framework import viewsets
from .models import AssetCategory, AssetSubcategory
from .serializers import AssetCategorySerializer, AssetSubcategorySerializer

class AssetCategoryViewSet(viewsets.ModelViewSet):
    queryset = AssetCategory.objects.all()
    serializer_class = AssetCategorySerializer

class AssetSubcategoryViewSet(viewsets.ModelViewSet):
    queryset = AssetSubcategory.objects.all()
    serializer_class = AssetSubcategorySerializer
