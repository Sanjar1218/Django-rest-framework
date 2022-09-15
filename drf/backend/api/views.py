from .models import Item
from .serializers import ItemSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['get'])
def echo(requests):
    instance = Item.objects.all().order_by('?').first()
    # r = model_to_dict(data)
    r = ItemSerializer(instance).data
    return Response(r, status=status.HTTP_200_OK)

@api_view(['post'])
def getting(reqeust):
    
    serializer = ItemSerializer(data=reqeust.data)
    if serializer.is_valid(raise_exception=True):
        # print(serializer.data)
        instance = serializer.save()
        print(instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)