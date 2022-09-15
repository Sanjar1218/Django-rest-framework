from rest_framework import serializers

from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField(method_name='st')
    
    def st(self, obj):
        print(type(obj))
        try:
            return obj.get_discount()
        except:
            return 'error'

    class Meta:
        model = Item
        fields = ['name', 'dec', 'count']