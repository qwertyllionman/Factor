from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework.exceptions import ValidationError
from rest_framework.fields import ChoiceField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ImageField, Serializer, IntegerField, DecimalField, CharField
from rest_framework.serializers import ModelSerializer

from apps.models import Book, Category, Order, OrderItem, User, DeleteUser, Network


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title', 'author', 'price', 'page', 'vol', 'description', 'amount', 'category_id', 'photo', 'money_type', 'created_at']
        read_only_fields = ['created_at', 'id', 'amount']


class CategorySerializer(ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['name', 'user', 'id', 'books']
        read_only_fields = ['id']

    def validate_name(self, value):
        if Category.objects.filter(name=value).first():
            raise ValidationError("This category is already exists!")
        return value

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user_id', 'payment_status', 'status']
        read_only_fields = ['id']

class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'book_id', 'order_id', 'count']
        read_only_fields = ['id']

class UserSerializer(ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ['created_at', 'updated_at', 'id']

class DeleteUserSerializer(ModelSerializer):
    class Meta:
        model = DeleteUser
        fields = ['id', 'user', 'deleted_at']

class NetworkSerializer(ModelSerializer):
    class Meta:
        model = Network
        fields = ['id', 'title', 'link']
        read_only_fields = ['id']

class OrderDetailSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    order_items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'payment_status', 'user', 'order_items']
        read_only_fields = ['id']

class BookAmountSerializer(Serializer):
    amount = IntegerField()

    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.save()
        return instance

class TrendingCategorySerializer(ModelSerializer):
    book_count = IntegerField(read_only=True)
    class Meta:
        model = Category
        fields = ["id", "name", "book_count"]
        read_only_fields = ["id", "name", "book_count"]