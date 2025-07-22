from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, TextChoices, DateTimeField, BooleanField, ForeignKey, CASCADE, Model, \
    SmallIntegerField, DecimalField, TextField, ImageField, SET_NULL
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework.relations import PrimaryKeyRelatedField


class User(AbstractUser):
    class LanguageType(TextChoices):
        ENGLISH = 'english', 'English'
        UZBEK = 'uzbek', 'Uzbek'

    username = CharField(max_length=255, unique=True)
    first_name = None
    last_name = None
    fullname = CharField(max_length=255, null=True, blank=True)
    lang = CharField(choices=LanguageType, max_length=255, default=LanguageType.ENGLISH)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    is_admin = BooleanField(default=False)
    is_online = BooleanField(default=False)
    last_message = TextField(null=True, blank=True)
    last_message_time = DateTimeField(auto_now=True)
    phone_number = CharField(max_length=255, null=True, blank=True)


class DeleteUser(Model):
    user= ForeignKey('apps.User', on_delete=SET_NULL, null=True, related_name="delete_users")
    deleted_at = DateTimeField(auto_now_add=True)


class Network(Model):
    title = CharField(max_length=255, null=True, blank=True)
    link = CharField(max_length=255, null=True, blank=True)


class Category(Model):
    name = CharField(max_length=255)
    user = ForeignKey('apps.User', CASCADE, related_name='categories')


class Order(Model):
    class StatusType(TextChoices):
        PENDING = 'pending', 'Pending'
        APPROVED = 'approved', 'Approved'

    class PaymentStatusType(TextChoices):
        PENDING = 'pending', 'Pending'
        APPROVED = 'approved', 'Approved'
        CANCELED = 'canceled', 'Canceled'

    user_id = ForeignKey('apps.User', CASCADE, related_name='orders')
    status = CharField(max_length=255, choices=StatusType, default=StatusType.PENDING)
    payment_status = CharField(max_length=255, choices=PaymentStatusType, default=PaymentStatusType.PENDING)


class Book(Model):
    class VolType(TextChoices):
        SOFT = 'soft', 'Soft'
        HARD = 'hard', 'Hard'
    class MoneyType(TextChoices):
        SUM = 'sum', 'Sum'
        DOLLAR = 'dollar', 'Dollar'
    title = CharField(max_length=255, null=True, blank=True)
    author = CharField(max_length=255)
    page = SmallIntegerField()
    vol = CharField(max_length=255, choices=VolType, default=VolType.SOFT)
    price = DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    description = TextField(null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    amount = SmallIntegerField(default=1)
    category_id = ForeignKey('apps.Category', CASCADE, related_name='books')
    photo = ImageField(upload_to='books/')
    money_type = CharField(max_length=255, choices=MoneyType, default=MoneyType.SUM)

class OrderItem(Model):
    book_id = ForeignKey('apps.Book', CASCADE, related_name='order_items')
    count = SmallIntegerField(default=1)
    order_id = ForeignKey('apps.Order', CASCADE, related_name='order_items')



