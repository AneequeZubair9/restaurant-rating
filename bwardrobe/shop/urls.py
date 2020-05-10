from django.urls import path
from.import views


urlpatterns = [
    path('',views.index, name=  "ShopHome"),

    path('about/',views.about, name="About"),
    path('contact/',views.contact, name="Contact"),
    path('sproducts/<int:id>',views.search, name=" search"),
    path('products/<int:id>',views.prodView, name="prodView"),



]
