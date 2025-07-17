from django.db.models.aggregates import Count, Sum
from drf_spectacular.utils import extend_schema
from rest_framework import generics, filters, status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    get_object_or_404
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.models import Book, Category, Order, OrderItem, User, DeleteUser, Network
from apps.serializers import BookSerializer, CategorySerializer, OrderSerializer, OrderItemSerializer, UserSerializer, \
    DeleteUserSerializer, NetworkSerializer, OrderDetailSerializer, BookAmountSerializer, TrendingCategorySerializer


# ------------------------------- Book -------------------------------------
@extend_schema(tags=['Book'])
class CreateBookApiView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    parser_classes = [MultiPartParser, JSONParser, FormParser]


@extend_schema(tags=['Book'])
class GetBookListApiView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@extend_schema(tags=['Book'])
class GetBookApiView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@extend_schema(tags=['Book'])
class UpdateBookApiView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = False
        return super().get_serializer(*args, **kwargs)


@extend_schema(tags=['Book'])
class DeleteBookApiView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@extend_schema(tags=['Book'])
class GetBookByCategoryApiView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Book.objects.filter(category_id=category_id)


@extend_schema(tags=['Book'])
class GetBookByMoneyTypeApiView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        money_type = self.kwargs['money_type']
        return Book.objects.filter(money_type=money_type)


@extend_schema(tags=['Book'])
class GetAvailableBookApiView(ListAPIView):
    queryset = Book.objects.filter(amount__gt=0)
    serializer_class = BookSerializer


# ------------------------ Category -------------------------------------------
@extend_schema(tags=['Category'])
class CreateCategoryApiView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@extend_schema(tags=['Category'])
class GetCategoryListApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@extend_schema(tags=['Category'])
class GetCategoryApiView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_url_kwarg = 'pk'


@extend_schema(tags=['Category'])
class UpdateCategoryApiView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_url_kwarg = 'pk'

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super().get_serializer(*args, **kwargs)


@extend_schema(tags=['Category'])
class DeleteCategoryApiView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_url_kwarg = 'pk'


# ------------------------ Order --------------------------------

@extend_schema(tags=['Order'])
class CreateOrderApiView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@extend_schema(tags=['Order'])
class ListOrderApiView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@extend_schema(tags=['Order'])
class GetOrderApiView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@extend_schema(tags=['Order'])
class UpdateOrderApiView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super().get_serializer(*args, **kwargs)


@extend_schema(tags=['Order'])
class GetUserOrderApiView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Order.objects.filter(user_id=user_id)


@extend_schema(tags=['Order'])
class GetOrderByPaymentStatusApiView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        payment_status = self.kwargs['payment_status']
        return Order.objects.filter(payment_status=payment_status)


# ----------------------------------------- Order Item ------------------------------------------
@extend_schema(tags=['Order Item'])
class CreateOrderItemApiView(CreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


@extend_schema(tags=['Order Item'])
class ListOrderItemApiView(ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


@extend_schema(tags=['Order Item'])
class GetOrderItemApiView(RetrieveAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


# ---------------------------------- User -------------------------------------------
@extend_schema(tags=['User'])
class CreateUserApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@extend_schema(tags=['User'])
class ListUserApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@extend_schema(tags=['User'])
class GetUserApiView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@extend_schema(tags=['User'])
class UpdateUserApiView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super().get_serializer(*args, **kwargs)


@extend_schema(tags=['User'])
class DeleteUserApiView(DestroyAPIView):
    queryset = User.objects.all()

    def perform_destroy(self, instance):
        DeleteUser.objects.create(user=instance)
        instance.delete()


# -------------------------------- Delete User ---------------------------
@extend_schema(tags=['Delete User'])
class ListDeleteUserApiView(ListAPIView):
    queryset = DeleteUser.objects.all().order_by('-deleted_at')  # problem > user = Null
    serializer_class = DeleteUserSerializer


@extend_schema(tags=['Delete User'])
class GetDeleteUserApiView(RetrieveAPIView):
    queryset = DeleteUser.objects.all()
    serializer_class = DeleteUserSerializer


# -------------------------------- Networks ---------------------------
@extend_schema(tags=['Network'])
class CreateNetworkApiView(CreateAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer


@extend_schema(tags=['Network'])
class GetNetworkApiView(ListAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer


# -------------------------------- Nested Serializers ---------------------------
@extend_schema(tags=['Nested Serializers'])
class GetSerializerApiView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = 'user_id'


@extend_schema(tags=['Nested Serializers'])
class OrderDetailAPIView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer
    lookup_url_kwarg = 'order_id'


@extend_schema(tags=['Nested Serializers'])
class CategoryBookAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_url_kwarg = 'category_id'


# -------------------------------- Admin  ---------------------------
@extend_schema(tags=['Admin'])
class ListAdminAPIView(ListAPIView):
    queryset = User.objects.filter(is_admin=True)
    serializer_class = UserSerializer


@extend_schema(tags=['Admin'])
class UpdateBookAmountAPIView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookAmountSerializer
    lookup_url_kwarg = 'pk'

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super().get_serializer(*args, **kwargs)


# -------------------------------- Filtering and Searching  ---------------------------

@extend_schema(tags=['Filtering and Searching'])
class SearchBookAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


@extend_schema(tags=['Filtering and Searching'])
class SearchBookAuthorAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['author']


@extend_schema(tags=['Filtering and Searching'])
class SearchUserAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['lang']


@extend_schema(tags=['Filtering and Searching'])
class GetOrderedAPIView(APIView):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        categories = Category.objects.filter(user=user)
        books = Book.objects.filter(category_id__in=categories)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# ---------------------------------- Statistics --------------------------------------------

@extend_schema(tags=['Statistics'])
class BookStatsAPIView(APIView):
    def get(self, request):
        total_books = Book.objects.aggregate(total_books=Count('id'))['total_books']
        pages = Book.objects.aggregate(Sum('page'))['page__sum']
        average_pages = pages / total_books
        most_common_category = Book.objects.values('category_id__name').annotate(Count('id')).order_by(
            '-id__count').first()
        most_common_category = most_common_category['category_id__name']
        data = {"average_pages": average_pages, "total_books": total_books,
                "most_common_category": most_common_category}
        return Response(data, status=status.HTTP_200_OK)


@extend_schema(tags=['Statistics'])
class OrderStatsAPIView(APIView):
    def get(self, request):
        total_orders = Order.objects.aggregate(total_orders=Count('id'))['total_orders']
        paid_orders = len(Order.objects.filter(payment_status='approved'))
        pending_orders = len(Order.objects.filter(status="pending"))
        data = {
            "total_orders" : total_orders,
            "paid_orders" : paid_orders,
            "pending_orders" : pending_orders
        }
        return Response(data, status=status.HTTP_200_OK)
