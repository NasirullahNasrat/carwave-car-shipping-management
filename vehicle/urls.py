from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Auth URLs
    path('', views.dashboard, name='dashboard'),
    path('login/', views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Logout path (updated)
    path('logout/', auth_views.LogoutView.as_view(
        next_page='login'  # Redirect to login page after logout
    ), name='logout'),
    # Related URLs
    path('related/', views.RelatedListView.as_view(), name='related-list'),
    path('related/create/', views.related_create, name='related-create'),
    path('related/<int:pk>/update/', views.related_update, name='related-update'),
    path('related/<int:pk>/delete/', views.related_delete, name='related-delete'),
    
    # CarMark URLs
    path('carmark/', views.CarMarkListView.as_view(), name='carmark-list'),
    path('carmark/create/', views.carmark_create, name='carmark-create'),
    path('carmark/<int:pk>/update/', views.carmark_update, name='carmark-update'),
    path('carmark/<int:pk>/delete/', views.carmark_delete, name='carmark-delete'),
    
    # CarType URLs
    path('cartype/', views.CarTypeListView.as_view(), name='cartype-list'),
    path('cartype/create/', views.cartype_create, name='cartype-create'),
    path('cartype/<int:pk>/update/', views.cartype_update, name='cartype-update'),
    path('cartype/<int:pk>/delete/', views.cartype_delete, name='cartype-delete'),
    
    # ModelYear URLs
    path('modelyear/', views.ModelYearListView.as_view(), name='modelyear-list'),
    path('modelyear/create/', views.modelyear_create, name='modelyear-create'),
    path('modelyear/<int:pk>/update/', views.modelyear_update, name='modelyear-update'),
    path('modelyear/<int:pk>/delete/', views.modelyear_delete, name='modelyear-delete'),
    
    # CarColor URLs
    path('carcolor/', views.CarColorListView.as_view(), name='carcolor-list'),
    path('carcolor/create/', views.carcolor_create, name='carcolor-create'),
    path('carcolor/<int:pk>/update/', views.carcolor_update, name='carcolor-update'),
    path('carcolor/<int:pk>/delete/', views.carcolor_delete, name='carcolor-delete'),
    
    # CarAction URLs
    path('caraction/', views.CarActionListView.as_view(), name='caraction-list'),
    path('caraction/create/', views.caraction_create, name='caraction-create'),
    path('caraction/<int:pk>/update/', views.caraction_update, name='caraction-update'),
    path('caraction/<int:pk>/delete/', views.caraction_delete, name='caraction-delete'),




    path('carinfo/', views.CarInfoListView.as_view(), name='carinfo-list'),
    path('create/', views.carinfo_create, name='carinfo-create'),
    path('<int:pk>/update/', views.carinfo_update, name='carinfo-update'),
    path('<int:pk>/delete/', views.carinfo_delete, name='carinfo-delete'),



    path('purchaseinfo/', views.PurchaseInfoListView.as_view(), name='purchaseinfo-list'),
    path('purchaseinfo/create/', views.PurchaseInfoCreateView.as_view(), name='purchaseinfo-create'),
    path('purchaseinfo/<int:pk>/edit/', views.PurchaseInfoUpdateView.as_view(), name='purchaseinfo-update'),
    path('purchaseinfo/<int:pk>/delete/', views.PurchaseInfoDeleteView.as_view(), name='purchaseinfo-delete'),



    path('shippinginfo/', views.ShippingInfoListView.as_view(), name='shippinginfo-list'),
    path('shippinginfo/create/', views.ShippingInfoCreateView.as_view(), name='shippinginfo-create'),
    path('shippinginfo/<int:pk>/edit/', views.ShippingInfoUpdateView.as_view(), name='shippinginfo-update'),
    path('shippinginfo/<int:pk>/delete/', views.ShippingInfoDeleteView.as_view(), name='shippinginfo-delete'),
    path('shippinginfo/<int:pk>/', views.ShippingInfoDetailView.as_view(), name='shippinginfo-detail'),


    path('world-expenses/', views.WorldExpensesListView.as_view(), name='world_expenses_list'),
    path('world-expenses/add/', views.WorldExpensesCreateView.as_view(), name='world_expenses_create'),
    path('world-expenses/<int:pk>/edit/', views.WorldExpensesUpdateView.as_view(), name='world_expenses_update'),
    path('world-expenses/<int:pk>/delete/', views.WorldExpensesDeleteView.as_view(), name='world_expenses_delete'),
    path('world-expenses/<int:pk>/', views.WorldExpensesDetailView.as_view(), name='world_expenses_detail'),

    path('kabul-expenses/', views.KabulExpensesListView.as_view(), name='kabul_expenses_list'),
    path('kabul-expenses/add/', views.KabulExpensesCreateView.as_view(), name='kabul_expenses_create'),
    path('kabul-expenses/<int:pk>/edit/', views.KabulExpensesUpdateView.as_view(), name='kabul_expenses_update'),
    path('kabul-expenses/<int:pk>/delete/', views.KabulExpensesDeleteView.as_view(), name='kabul_expenses_delete'),
    path('kabul-expenses/<int:pk>/', views.KabulExpensesDetailView.as_view(), name='kabul_expenses_detail'),



    path('repair-expenses/', views.RepairAndOtherExpensesListView.as_view(), name='repair_expenses_list'),
    path('repair-expenses/add/', views.RepairAndOtherExpensesCreateView.as_view(), name='repair_expenses_create'),
    path('repair-expenses/<int:pk>/edit/', views.RepairAndOtherExpensesUpdateView.as_view(), name='repair_expenses_update'),
    path('repair-expenses/<int:pk>/delete/', views.RepairAndOtherExpensesDeleteView.as_view(), name='repair_expenses_delete'),






   
    # path('buyer/create-ajax/', views.buyer_create_ajax, name='buyer_create_ajax'),
    path('sale-info/', views.SaleInfoListView.as_view(), name='sale_info_list'),
    path('sale-info/add/', views.SaleInfoCreateView.as_view(), name='sale_info_create'),
    path('sale-info/<int:pk>/edit/', views.SaleInfoUpdateView.as_view(), name='sale_info_update'),
    path('sale-info/<int:pk>/delete/', views.SaleInfoDeleteView.as_view(), name='sale_info_delete'),
    path('sale-info/<int:pk>/', views.SaleInfoDetailView.as_view(), name='sale_info_detail'),




    path('car-images/', views.CarImagesListView.as_view(), name='car_images_list'),
    path('car-images/add/', views.CarImagesCreateView.as_view(), name='car_images_create'),
    path('car-images/<int:pk>/edit/', views.CarImagesUpdateView.as_view(), name='car_images_update'),
    path('car-images/<int:pk>/delete/', views.CarImagesDeleteView.as_view(), name='car_images_delete'),
    
    
    
    path('settings/', views.SettingsView.as_view(), name='settings'),


    path('currency-list', views.CurrencyListView.as_view(), name='currency-list'),
    path('currency-create/', views.CurrencyCreateView.as_view(), name='currency-create'),
    path('currency-update/<int:pk>/update/', views.CurrencyUpdateView.as_view(), name='currency-update'),
    path('currency-delete/<int:pk>/delete/', views.CurrencyDeleteView.as_view(), name='currency-delete'),



    path('dashboard-settings/', views.dashboard_setting_update, name='dashboard-setting-update'),





    path('buyer', views.BuyerListView.as_view(), name='buyer_list'),
    path('buyer-create/', views.BuyerCreateView.as_view(), name='buyer_create'),
    path('buyer/<int:pk>/edit/', views.BuyerUpdateView.as_view(), name='buyer_update'),
    path('buyer/<int:pk>/delete/', views.BuyerDeleteView.as_view(), name='buyer_delete'),
]