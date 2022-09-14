from .models import Item
from .serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['get'])
def echo(requests):
    instance = Item.objects.all().order_by('?').first()
    # r = model_to_dict(data)
    r = ItemSerializer(instance).data
    return Response(r)