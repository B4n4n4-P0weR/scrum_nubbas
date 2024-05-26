from django.urls import path
from . import views

urlpatterns = [
    #главные экраны
    path('', views.home, name='home'),
    path('sales/', views.sales, name='sales'),
    path('supplies/', views.supplies, name='supplies'),
    path('reports/', views.reports, name='reports'),
    #поиск
    path('search/<str:search_type>/', views.search, name='search'),
    #получение информации по номеру при поиске
    path('supplies/<int:supply_number>/', views.supply_detail, name='supply_detail'),
    path('get_supply/', views.get_supply, name='get_supply'),
    path('sales/<int:sale_number>/', views.sale_detail, name='sale_detail'),
    path('get_sale/', views.get_sale, name='get_sale'),
    #списки поставок и заказов
    path('sales/list/', views.sales_list, name='sales_list'),
    path('supplies/list/', views.supplies_list, name='supplies_list'),
    #добавление поставок и заказов
    path('sales/add/', views.sales_add, name='sales_add'),
    path('supplies/add/', views.supplies_add, name='supplies_add'),
    #заявки поставщику
    path('supplier_requests/', views.supplier_requests, name='supplier_requests'),
    #отчёты
    path('reports/needful/', views.report_needful_stuff, name='report_needful_stuff'),
    path('reports/sold/', views.report_sold_stuff, name='report_sold_stuff'),
    path('reports/stored/', views.report_stored_stuff, name='report_stored_stuff')
]