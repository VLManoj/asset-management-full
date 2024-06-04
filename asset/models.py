from django.db import models

class AssetCategory(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.id

class AssetSubcategory(models.Model):
    category_id = models.ForeignKey(AssetCategory, on_delete=models.CASCADE)
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.id