from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('order/',views.order,name='order'),
    path('customer_details/',views.customer_details,name='customer_details'),
    path('order_review/',views.order_review,name='order_review'),
    path('confirm_order/',views.confirm_order,name='confirm_order'),
    path('order_confirmation/<int:order_id>/',views.order_confirmation,name='order_confirmation')
]