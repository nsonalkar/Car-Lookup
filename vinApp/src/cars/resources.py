from import_export import resources
from .models import Cars

class CarResource(resources.ModelResource):
    class Meta:
        model = Cars