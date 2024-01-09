from django.urls import path
from Frontend import views

urlpatterns = [
    path('home_page/', views.home_page, name="home_page"),
    path('rest_view/', views.rest_view, name="rest_view"),
    path('show_cat/<rest_id>', views.show_cat, name="show_cat"),
    path('single_view_rest/<int:code_id>/', views.single_view_rest, name="single_view_rest"),
    path('about_us_page/', views.about_us_page, name="about_us_page"),
    path('services_page/', views.services_page, name="services_page"),
    path('contact_us_page/', views.contact_us_page, name="contact_us_page"),
    path('save_contact/', views.save_contact, name="save_contact"),
    path('reg_page/', views.reg_page, name="reg_page"),
    path('log_page/', views.log_page, name="log_page"),
    path('save_reg/', views.save_reg, name="save_reg"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('cart_page/', views.cart_page, name="cart_page"),
    path('save_cart/', views.save_cart, name="save_cart"),
    path('rem_cart/<int:dataid>/', views.rem_cart, name="rem_cart"),
    path('checkout_page/', views.checkout_page, name="checkout_page"),
    path('save_check/', views.save_check, name="save_check"),
    path('payment/', views.payment, name="payment")



]