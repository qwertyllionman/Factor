from django.urls import path
from apps.views import CreateBookApiView, CreateCategoryApiView, GetCategoryListApiView, GetCategoryApiView, \
    UpdateCategoryApiView, DeleteCategoryApiView, GetBookListApiView, GetBookApiView, UpdateBookApiView, \
    DeleteBookApiView, GetBookByCategoryApiView, GetBookByMoneyTypeApiView, GetAvailableBookApiView, CreateOrderApiView, \
    ListOrderApiView, GetOrderApiView, UpdateOrderApiView, GetUserOrderApiView, GetOrderByPaymentStatusApiView, \
    CreateOrderItemApiView, ListOrderItemApiView, GetOrderItemApiView, CreateUserApiView, ListUserApiView, \
    GetUserApiView, UpdateUserApiView, DeleteUserApiView, ListDeleteUserApiView, GetDeleteUserApiView, \
    CreateNetworkApiView, GetNetworkApiView, GetSerializerApiView, OrderDetailAPIView, CategoryBookAPIView, \
    ListAdminAPIView, UpdateBookAmountAPIView, SearchBookAPIView, SearchBookAuthorAPIView, SearchUserAPIView, \
    GetOrderedAPIView

urlpatterns = [
    path('api/v1/book/create', CreateBookApiView.as_view()),
]
# ------------------------------ Category -----------------------------
urlpatterns += [
    path('api/v1/category/create', CreateCategoryApiView.as_view()),
    path('api/v1/category/get/list', GetCategoryListApiView.as_view()),
    path('api/v1/category/get/<int:pk>', GetCategoryApiView.as_view()),
    path('api/v1/category/update/<int:pk>', UpdateCategoryApiView.as_view()),
    path('api/v1/category/delete/<int:pk>', DeleteCategoryApiView.as_view()),
]

# ----------------------------- Book -------------------------------------------
urlpatterns += [
    path('api/v1/book/create', CreateBookApiView.as_view()),
    path('api/v1/book/get/list', GetBookListApiView.as_view()),
    path('api/v1/book/get/<int:pk>', GetBookApiView.as_view()),
    path('api/v1/book/update/<int:pk>', UpdateBookApiView.as_view()),
    path('api/v1/book/delete/<int:pk>', DeleteBookApiView.as_view()),
    path('api/v1/book/category/<int:category_id>', GetBookByCategoryApiView.as_view()),
    path('api/v1/book/money_type/<str:money_type>', GetBookByMoneyTypeApiView.as_view()),
    path('api/v1/book/available/', GetAvailableBookApiView.as_view()),
]
# ---------------------------------- Order -------------------------------------------

urlpatterns += [
    path('api/v1/order/create', CreateOrderApiView.as_view()),
    path('api/v1/order/get/list', ListOrderApiView.as_view()),
    path('api/v1/order/get/<int:pk>', GetOrderApiView.as_view()),
    path('api/v1/order/update/<int:pk>', UpdateOrderApiView.as_view()),
    path('api/v1/order/get/user/<int:user_id>', GetUserOrderApiView.as_view()),
    path('api/v1/order/get/payment_status/<str:payment_status>', GetOrderByPaymentStatusApiView.as_view()),
]

# ---------------------------------- Order items-------------------------------------------
urlpatterns += [
    path('api/v1/create/order_item/', CreateOrderItemApiView.as_view()),
    path('api/v1/get/list/order_item/', ListOrderItemApiView.as_view()),
    path('api/v1/get/order_item/<int:pk>', GetOrderItemApiView.as_view()),
]

# ---------------------------------- User -------------------------------------------
urlpatterns += [
    path('api/v1/user/create', CreateUserApiView.as_view()),
    path('api/v1/user/list', ListUserApiView.as_view()),
    path('api/v1/user/get/<int:pk>', GetUserApiView.as_view()),
    path('api/v1/user/update/<int:pk>', UpdateUserApiView.as_view()),
    path('api/v1/user/delete/<int:pk>', DeleteUserApiView.as_view()),
]
# ---------------------------------- User -------------------------------------------
urlpatterns += [
    path('api/v1/delete_users/list', ListDeleteUserApiView.as_view()),      # problem
    path('api/v1/delete_users/get/<int:pk>', GetDeleteUserApiView.as_view()),
]
# -------------------------------- Networks ---------------------------
urlpatterns += [
    path('api/v1/network/create', CreateNetworkApiView.as_view()),
    path('api/v1/network/list', GetNetworkApiView.as_view()),
]
# -------------------------------- Nested Serializers ---------------------------
urlpatterns += [
    path('api/v1/user/<int:user_id>/orders', GetSerializerApiView.as_view()),
    path('api/v1/order/<int:order_id>/details', OrderDetailAPIView.as_view()),
    path('api/v1/category/<int:category_id>/books', CategoryBookAPIView.as_view()),
]
# -------------------------------- Admin  ---------------------------
urlpatterns += [
    path('api/v1/user/admins', ListAdminAPIView.as_view()),
    path('api/v1/book/<int:pk>/amount', UpdateBookAmountAPIView.as_view()),
]
# -------------------------------- Filtering and Searching  ---------------------------
urlpatterns += [
    path("api/v1/book/search/", SearchBookAPIView.as_view()),
    path("api/v1/book/author", SearchBookAuthorAPIView.as_view()),
    path("api/v1/user/lang", SearchUserAPIView.as_view()),
    path("api/v1/user/<int:user_id>/books", GetOrderedAPIView.as_view()),
]