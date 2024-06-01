from django.urls import path
from . import views

urlpatterns = [
    # главные экраны
    path('', views.home, name='home'),
    path('sales/', views.sales, name='sales'),
    path('supplies/', views.supplies, name='supplies'),
    path('reports/', views.reports, name='reports'),

    # поиск
    path('search/<str:search_type>/', views.search, name='search'),
    # получение информации по номеру при поиске
    path('supplies/<int:supply_number>/', views.supply_detail, name='supply_detail'),
    path('get_supply/', views.get_supply, name='get_supply'),
    path('sales/<int:sale_number>/', views.sale_detail, name='sale_detail'),
    path('get_sale/', views.get_sale, name='get_sale'),

    # товары
    path('product/add/', views.product_add, name='product_add'),
    path('product/list/', views.product_list, name='product_list'),
    # продажи
    path('sales/add/', views.sales_add, name='sales_add'),
    path('sales/list/', views.sales_list, name='sales_list'),
    # поставщики
    path('supplies/supplier/add/', views.supplier_add, name='supplier_add'),
    path('supplies/supplier/list/', views.supplier_list, name='supplier_list'),
    # поставки
    path('supplies/add/', views.supplies_add, name='supplies_add'),
    path('supplies/list/', views.supplies_list, name='supplies_list'),
    path('supplies/collect/<int:supply_id>', views.supply_collect, name='supply_collect'),
    # содержания поставок
    # отгрузки
    path('shipment/add/', views.shipment_add, name='shipment_add'),
    path('shipment/list/', views.shipment_list, name='shipment_list'),
    # содержания отгрузок
    path('shipment/content/add/', views.content_of_shipment_add, name='content_of_shipment_add'),
    path('shipment/content/list/', views.content_of_shipment_list, name='content_of_shipment_list'),
    # место хранение товара
    path('product_locations/add/', views.product_locations_add, name='product_locations_add'),
    path('product_locations/list/', views.product_locations_list, name='product_locations_list'),

    # отчёты
    path('reports/needful/', views.report_needful_stuff, name='report_needful_stuff'),
    path('reports/sold/', views.report_sold_stuff, name='report_sold_stuff'),
    path('reports/stored/', views.report_stored_stuff, name='report_stored_stuff'),

    #удаление (для дебага)
    path('clear', views.debug_deleted, name='debug_deleted'),
    path('clear/all', views.all_clear, name='all_clear'),
    path('clear/product', views.product_clear, name='product_clear'),
    path('clear/sale_clear', views.sale_clear, name='sale_clear'),
    path('clear/supplier_clear', views.supplier_clear, name='supplier_clear'),
    path('clear/supply_clear', views.supply_clear, name='supply_clear'),
    path('clear/content_of_supply_clear', views.content_of_supply_clear, name='content_of_supply_clear'),
    path('clear/shipment_clear', views.shipment_clear, name='shipment_clear'),
    path('clear/content_of_shipment_clear', views.content_of_shipment_clear, name='content_of_shipment_clear'),
    path('clear/product_locations_clear', views.product_locations_clear, name='product_locations_clear')
]
