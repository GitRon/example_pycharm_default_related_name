from apps.myapp.models import BaseModel


def my_view(request):
    # Create test object
    obj, _ = BaseModel.objects.get_or_create(value=1)

    # Fetch object and type-hint it, so we are sure PyCharm knows the type
    obj: BaseModel = BaseModel.objects.all().first()
    # Here you see the warning
    related_models = obj.related_models.all()

    # This shows no warning and is not working (it's the Django default)
    related_models = obj.relatedmodel_set.all()
