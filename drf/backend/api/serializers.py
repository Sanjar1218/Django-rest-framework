from rest_framework import serializers

from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField(method_name='st')
    
    def st(self, obj):
        return obj.get_discount()

    class Meta:
        model = Item
        fields = ['name', 'dec', 'count']