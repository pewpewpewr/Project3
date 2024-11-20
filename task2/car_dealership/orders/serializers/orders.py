from rest_framework import serializers

from employees.models import orders

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = orders
        fields = ['id', 'customer', 'car', 'order_date', 'price']