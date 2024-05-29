from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('loginfn',views.loginfn,name='loginfn'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('add_item/',views.add_item,name='add_item'),
    path('itemreg',views.itemreg,name='itemreg'),
    path('add_product',views.add_product,name='add_product'),
    path('productreg',views.productreg,name='productreg'),
    path('view_product',views.view_product,name='view_product'),
    path('pdelete/<int:pk>',views.pdelete,name='pdelete'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('userregg',views.userregg,name='userregg'),
    path('view_users',views.view_users,name='view_users'),
    path('deleteuser/<int:pk>',views.deleteuser,name='deleteuser'),
    path('usernavbar',views.usernavbar,name='usernavbar'),
    path('productuser/<int:pk>',views.productuser,name='productuser'),
    path('add_to_cart/<int:pk>',views.add_to_cart,name='add_to_cart'),
    path('cart_remove/<int:pk>',views.cart_remove,name='cart_remove'),
    path('cart_view',views.cart_view,name='cart_view'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('about',views.about,name='about'),
    path('homenavbar',views.homenavbar,name='homenavbar'),
    path('footer_user',views.footer_user,name='footer_user'),
    path('all_products',views.all_products,name='all_products'),
    path('increment/<int:pk>',views.increment,name='increment'),
    path('decrement/<int:pk>',views.decrement,name='decrement'),
    path('checkout',views.checkout,name='checkout'),
    path('checkout_process',views.checkout_process,name='checkout_process'),
]
