from django.urls import path
from app import views
from django.conf import settings
from django.urls import re_path
from django.views.static import serve
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm, UserPasswordChangeForm, UserPasswordResetForms, UserSetPasswordForm
from django.urls import reverse_lazy
urlpatterns = [
    # path('', views.home),
    path('', views.ProductView.as_view(), name="home"),

    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>/', views.mobile, name='mobile'),

    path('laptop/', views.laptop, name='laptop'),
    path('laptop/<slug:data>/', views.laptop, name='laptop'),

    path('topwear/', views.topwear, name='topwear'),
    path('topwear/<slug:data>/', views.topwear, name='topwear'),

    path('bottomwear/', views.bottomwear, name='bottomwear'),
    path('bottomwear/<slug:data>/', views.bottomwear, name='bottomwear'),

    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=UserLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    path('passwordchange/', auth_views.PasswordChangeView.as_view(success_url='/passwordchangedone/', template_name='app/passwordchange.html', form_class=UserPasswordChangeForm), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=UserPasswordResetForms), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=UserSetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),

    path('checkout/', views.checkout, name='checkout'),
] 


if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
