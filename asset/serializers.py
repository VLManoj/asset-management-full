from rest_framework import serializers
from .models import AssetCategory,AssetSubcategory

class AssetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetCategory
        fields = '__all__'

class AssetSubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetSubcategory
        fields = '__all__'