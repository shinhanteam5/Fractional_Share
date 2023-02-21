from django.urls import path
from . import views
from stockdetail.views import submit
urlpatterns = [
    path("/<int:pk>", views.StockDetailView.as_view()),
    path("/<int:pk>/news", views.NewsListView.as_view()),
    path("/submit/<int:stock_code>",submit),
    path("/buy",views.BuyStockView.as_view()),

]