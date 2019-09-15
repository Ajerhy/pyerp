# Librerias Django
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.conf.urls import include

# Librerias en carpetas locales
from ..views import (
    ActivateView, AvatarUpdateView, ChangePasswordForm, ChangePasswordView,
    CompanyCreateView, CompanyDetailView, CompanyListView, CompanyUpdateView,
    CustomerListView, DeleteCompany, DeletePartner, DeleteUser,
    DoChangePassword, Install, InstallApps, LogOutModalView, InstallPyERP,
    PartnerAutoComplete, PartnerCreateView, PartnerDetailView,
    PartnerUpdateView, PasswordRecoveryView, ProfileView, ProviderListView,
    SignUpView, UninstallApps, UpdateApps, UpdateBaseConfigView,
    UserCreateView, UserDetailView, UserListView, UserUpdateView, erp_home)


from ..views.app import AppView
from ..views.base_config import LoadData
from ..views.country import (
    CountryCreateView, CountryDetailView, CountryListView, CountryUpdateView,
    DeleteCountry)
from ..views.cron import (
    CronCreateView, CronDetailView, CronListView, CronUpdateView, DeleteCron)
from ..views.currency import (
    CurrencyCreateView, CurrencyDetailView, CurrencyListView,
    CurrencyUpdateView, DeleteCurrency)
from ..views.log import (
    DeleteLog, LogCreateView, LogDetailView, LogListView, LogUpdateView)
from ..views.post import (
    DeletePost, PostCreateView, PostDetailView, PostListView, PostUpdateView)
# from .views.logoutmodal import LogOutModalView
from ..views.product import (
    DeleteProduct, ProductCreateView, ProductDetailView, ProductListView,
    ProductUpdateView)
from ..views.product_category import (
    DeleteProductCategory, ProductCategoryCreateView,
    ProductCategoryDetailView, ProductCategoryListView,
    ProductCategoryUpdateView)
from ..views.product_webcategory import (
    DeleteProductWebCategory, ProductWebCategoryCreateView,
    ProductWebCategoryDetailView, ProductWebCategoryListView,
    ProductWebCategoryUpdateView)
from ..views.website_config import UpdateWebsiteConfigView

app_name = 'base'

urlpatterns = [
    path('', erp_home, name='home'),
    path('install', Install, name='install'),
    path('install-erp', InstallPyERP, name='install-erp'),


    path(
        'logout/',
        auth_views.LogoutView.as_view(template_name='base/login.html'),
        name='logout'
    ),
    # path('logoutmodal/', LogOutModalView.as_view(), name='logout-modal'),
    path('config/<int:pk>', UpdateBaseConfigView.as_view(), name='base-config'),
    path('load-data', LoadData, name='load-data'),

    path('website-config/<int:pk>', UpdateWebsiteConfigView.as_view(), name='website-config'),

    path('update-app', UpdateApps, name='update-app'),
    path('install-app/<int:pk>/', InstallApps, name='install-app'),
    path('uninstall-app/<int:pk>/', UninstallApps, name='uninstall-app'),


    path('users', UserListView.as_view(), name='users'),
    path('user/add/', UserCreateView.as_view(), name='user-add'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user/<int:pk>/update', UserUpdateView.as_view(), name='user-update'),
    path('user/<int:pk>/delete/', DeleteUser, name='user-delete'),
    path('user/change-password/<int:pk>', ChangePasswordForm, name='password-change'),
    path('user/change-password-confirm/<int:pk>', DoChangePassword, name='do-change-password'),

    path('products', ProductListView.as_view(), name='products'),
    path('product/add/', ProductCreateView.as_view(), name='product-add'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('Product/<int:pk>/update', ProductUpdateView.as_view(), name='product-update'),
    path('Product/<int:pk>/delete/', DeleteProduct, name='product-delete'),


    path('countries', CountryListView.as_view(), name='countries'),
    path('country/add/', CountryCreateView.as_view(), name='country-add'),
    path('country/<int:pk>/', CountryDetailView.as_view(), name='country-detail'),
    path('country/<int:pk>/update', CountryUpdateView.as_view(), name='country-update'),
    path('country/<int:pk>/delete/', DeleteCountry, name='country-delete'),

    path('companies', CompanyListView.as_view(), name='companies'),
    path('company/add/', CompanyCreateView.as_view(), name='company-add'),
    path('company/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('company/<int:pk>/update', CompanyUpdateView.as_view(), name='company-update'),
    path('company/<int:pk>/delete/', DeleteCompany, name='company-delete'),

    path('partners', CustomerListView.as_view(), name='partners'),
    path('provider', ProviderListView.as_view(), name='provider'),

    path('partner/add/', PartnerCreateView.as_view(), name='partner-add'),
    path('partner/<int:pk>/', PartnerDetailView.as_view(), name='partner-detail'),
    path('partner/<int:pk>/update', PartnerUpdateView.as_view(), name='partner-update'),
    path('partner/<int:pk>/delete/', DeletePartner, name='partner-delete'),

    path('product-category', ProductCategoryListView.as_view(), name='product-category'),
    path('product-category/add/', ProductCategoryCreateView.as_view(), name='product-category-add'),
    path('product-category/<int:pk>/', ProductCategoryDetailView.as_view(), name='product-category-detail'),
    path('product-category/<int:pk>/update', ProductCategoryUpdateView.as_view(), name='product-category-update'),
    path('product-category/<int:pk>/delete/', DeleteProductCategory, name='product-category-delete'),

    path('product-webcategory', ProductWebCategoryListView.as_view(), name='product-webcategory'),
    path('product-webcategory/add/', ProductWebCategoryCreateView.as_view(), name='product-webcategory-add'),
    path('product-webcategory/<int:pk>/', ProductWebCategoryDetailView.as_view(), name='product-webcategory-detail'),
    path('product-webcategory/<int:pk>/update', ProductWebCategoryUpdateView.as_view(), name='product-webcategory-update'),
    path('product-webcategory/<int:pk>/delete/', DeleteProductWebCategory, name='product-webcategory-delete'),

    path('logs', LogListView.as_view(), name='logs'),
    path('log/add/', LogCreateView.as_view(), name='log-add'),
    path('log/<int:pk>/', LogDetailView.as_view(), name='log-detail'),
    path('log/<int:pk>/update', LogUpdateView.as_view(), name='log-update'),
    path('log/<int:pk>/delete/', DeleteLog, name='log-delete'),

    path('crons', CronListView.as_view(), name='crons'),
    path('cron/add/', CronCreateView.as_view(), name='cron-add'),
    path('cron/<int:pk>/', CronDetailView.as_view(), name='cron-detail'),
    path('cron/<int:pk>/update', CronUpdateView.as_view(), name='cron-update'),
    path('cron/<int:pk>/delete/', DeleteCron, name='cron-delete'),

    path('currencies', CurrencyListView.as_view(), name='currencies'),
    path('currency/add/', CurrencyCreateView.as_view(), name='currency-add'),
    path('currency/<int:pk>/', CurrencyDetailView.as_view(), name='currency-detail'),
    path('currency/<int:pk>/update', CurrencyUpdateView.as_view(), name='currency-update'),
    path('currency/<int:pk>/delete/', DeleteCurrency, name='currency-delete'),

    path('post', PostListView.as_view(), name='post-backend'),
    path('post/add/', PostCreateView.as_view(), name='post-add'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', DeletePost, name='post-delete'),


    path('apps', AppView.as_view(), name='apps'),

    # ====================== Rutas de Auto Completado ====================== #
    path(
        'partner/partner-autocomplete',
        PartnerAutoComplete.as_view(),
        name='partners-autocomplete'
    ),

    # ============================ New URLs ============================ #
    path('', include('apps.base.urls.usercustom')),
    path('shop/', include('apps.base.urls.shop')),
    path('wpayment/', include('apps.base.urls.wpayment')),
    path('faq/', include('apps.base.urls.faq')),
    path('parameter/', include('apps.base.urls.parameter')),
    path('image/', include('apps.base.urls.image')),
    path('tag/', include('apps.base.urls.tag')),
    path('comment/', include('apps.base.urls.comment')),
    path('page/', include('apps.base.urls.page')),
    path('wparameter/', include('apps.base.urls.wparameter')),
    path('meta/', include('apps.base.urls.meta')),
    path('variant/', include('apps.base.urls.variant')),
    path('attribute/', include('apps.base.urls.attribute')),
    path('product_category_uom/', include('apps.base.urls.product_category_uom')),
    path('uom/', include('apps.base.urls.uom')),

]
