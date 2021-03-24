"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
# from django.conf import url
from django.conf.urls import url
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth import views as auth_views
# from allauth.account.views import confirm_email
from allauth.account.views import ConfirmEmailView
from dj_rest_auth.registration.views import VerifyEmailView, RegisterView



urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')), # new

    
    url(r'^signup/$', TemplateView.as_view(template_name="signup.html"),
        name='signup'),
    url(r'^email-verification/$',
        TemplateView.as_view(template_name="email_verification.html"),
        name='email-verification'),
    url(r'^login/$', TemplateView.as_view(template_name="login.html"),
        name='login'),
    url(r'^logout/$', TemplateView.as_view(template_name="logout.html"),
        name='logout'),
    url(r'^password-reset/$',
        TemplateView.as_view(template_name="password_reset.html"),
        name='password-reset'),
    url(r'^password-reset/confirm/$',
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name='password-reset-confirm'),

    url(r'^user-details/$',
        TemplateView.as_view(template_name="user_details.html"),
        name='user-details'),
    url(r'^password-change/$',
        TemplateView.as_view(template_name="password_change.html"),
        name='password-change'),
    
    
     # this url is used to generate email content
    path('password-reset/confirm/<uidb64>/<token>',
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name='password_reset_confirm'),

    
    path('api-auth/', include('rest_framework.urls')), # new
    # path('password-reset/<uidb64>/<token>/', empty_view, name='password_reset_confirm'),
    # path('', include('django.contrib.auth.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')), # new

    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    # url(r'^api/v1/dj-rest-auth/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
    # path('confirm-email/<str:key>/', ConfirmEmailView.as_view(),
    #      name='account_confirm_email'),
    re_path(r'^account-confirm-email/', VerifyEmailView.as_view(),
     name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(),
     name='account_confirm_email'),


    # url(r'^', include('django.contrib.auth.urls')),
    # path('password-reset/confirm/<uidb64>/<token>',
    #     TemplateView.as_view(template_name="password_reset_confirm.html"),
#     name='password_reset_confirm'),
    # path('reset_password/', auth_views.PasswordResetView.as_view(), name ='reset_password'),
    # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name ='password_reset_done'),
    # path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name ='password_reset_confirm'),
    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name ='password_reset_complete'),
]
