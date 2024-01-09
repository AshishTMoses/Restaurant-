from django.urls import path
from Restaurantapp import views

urlpatterns = [
    path('intro_index_page/', views.intro_index_page, name="intro_index_page"),
    path('add_restaurant_page/', views.add_restaurant_page, name="add_restaurant_page"),
    path('save_restaurant/', views.save_restaurant, name="save_restaurant"),
    path('display_restaurant/', views.display_restaurant, name="display_restaurant"),
    path('edit_restaurant/<int:dataid>/', views.edit_restaurant, name="edit_restaurant"),
    path('update_restaurant/<int:dataid>/', views.update_restaurant, name="update_restaurant"),
    path('remv_restaurant/<int:dataid>/', views.remv_restaurant, name="remv_restaurant"),
    path('add_rest_det/', views.add_rest_det, name="add_rest_det"),
    path('save_rest_det/', views.save_rest_det, name="save_rest_det"),
    path('disp_rest_list/', views.disp_rest_list, name="disp_rest_list"),
    path('edit_rest/<int:res_id>/', views.edit_rest, name="edit_rest"),
    path('update_rest/<int:dataid>/', views.update_rest, name="update_rest"),
    path('remv_rest/<int:dataid>/', views.remv_rest, name="remv_rest"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
    path('user_details/', views.user_details, name="user_details"),
    path('user_details/', views.user_details, name="user_details"),
    path('cnc_det/<int:dlid>/', views.cnc_det, name="cnc_det"),



]