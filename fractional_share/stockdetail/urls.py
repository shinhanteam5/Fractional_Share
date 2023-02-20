from django.urls import path
from . import views
from stockdetail.views import buy
urlpatterns = [
    path("/<int:pk>", views.StockDetailView.as_view()),
    # path("/buy",buy),
    path("/buy",views.BuyStockView.as_view()),

]