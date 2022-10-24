from django import forms

from order.models import OrderItem

from order.models import Order


class MyOrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = [
            "price",
            "product",
            "quantity",
        ]


class MyOrderForm(forms.ModelForm):
    items = MyOrderItemForm(many=True)
    class Meta:
        model = Order
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "om_token",
            "items",
            "paid_amount"
        ]


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = [
            "price",
            "product",
            "quantity",
        ]


class OrderForm(forms.ModelForm):
    items = OrderItemForm(many=True)
    class Meta:
        model = Order
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "om_token",
            "items",
            "paid_amount"
        ]

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)

        return order