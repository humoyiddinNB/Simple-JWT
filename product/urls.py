from django.urls import path

from product.views import ProductCreate, ProductUpdateView, ProductDeleteView, ProductListView, ProductDetailView

urlpatterns = [
    path("create/", ProductCreate.as_view(), name='create'),
    path("update/<int:pk>/", ProductUpdateView.as_view(), name='update'),
    path("delete/<int:pk>/", ProductDeleteView.as_view(), name='delete'),
    path("list/", ProductListView.as_view(), name='list'),
    path("detail/<int:pk>/", ProductDetailView.as_view(), name='detail')
]