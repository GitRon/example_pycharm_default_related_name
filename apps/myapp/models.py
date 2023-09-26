from django.db import models


class BaseModel(models.Model):
    value = models.IntegerField(default=1)


class RelatedModel(models.Model):
    base_model = models.ForeignKey(BaseModel, on_delete=models.CASCADE)

    class Meta:
        default_related_name = "related_models"
