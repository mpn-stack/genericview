from django.urls import path
from . import views

urlpatterns = [
    path('',views.ProductListCreate.as_view()),
    path('<int:pk>',views.ProductRetrieveUpdateDestroy.as_view()),
]