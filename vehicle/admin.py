from django.contrib import admin
from .models import (
    Related, CarMark, CarType, ModelYear, CarColor, CarAction,
    CarInfo, PurchaseInfo, ShippingInfo, WorldExpenses,
    KabulExpenses, RepairAndOtherExpenses, SaleInfo, CarImages, DashboardSetting, Currency, Buyer
)



admin.site.register(Currency)
admin.site.register(Buyer)


@admin.register(Related)
class RelatedAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(CarMark)
class CarMarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(CarType)
class CarTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'mark', 'name')


@admin.register(ModelYear)
class ModelYearAdmin(admin.ModelAdmin):
    list_display = ('id', 'year')


@admin.register(CarColor)
class CarColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(CarAction)
class CarActionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(CarInfo)
class CarInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'mark', 'model_year', 'vin', 'lot')
    search_fields = ('vin', 'lot')
    list_filter = ('mark', 'model_year', 'color')


@admin.register(PurchaseInfo)
class PurchaseInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'purchase_price', 'paid_amount', 'remain_purchase', 'buy_date')


@admin.register(ShippingInfo)
class ShippingInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'date_arrived_in_dubai', 'total_price_to_dubai', 'dubai_paid_invoice')


@admin.register(WorldExpenses)
class WorldExpensesAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'herat_arrival_date', 'shipiping_price_to_islam_qala', 'gomrok_payment')


@admin.register(KabulExpenses)
class KabulExpensesAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'herat_to_kabul_cost', 'usa_to_kabul_cost', 'arrival_date_kabul')


@admin.register(RepairAndOtherExpenses)
class RepairAndOtherExpensesAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'repair_cost', 'palate_cost')


@admin.register(SaleInfo)
class SaleInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'status', 'sale_price', 'special_sale_price', 'benefit')
    readonly_fields = ('sale_commission', 'special_sale_price', 'benefit', 'capital_bound')
    list_filter = ('status',)




@admin.register(CarImages)
class CarImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'description', 'uploaded_at')
    search_fields = ('car__vin', 'description')
    list_filter = ('uploaded_at',)


@admin.register(DashboardSetting)
class DashboardSettingAdmin(admin.ModelAdmin):
    fieldsets = (
        ('اطلاعات اصلی سیستم', {
            'fields': (
                'site_name',
                'logo',
            ),
            'description': 'تنظیمات اصلی و ظاهری سیستم'
        }),
        ('اطلاعات تماس', {
            'fields': (
                'email',
                'address',
            ),
            'description': 'اطلاعات تماس و آدرس سیستم'
        }),
    )
    
    list_display = ('site_name', 'email')
    list_display_links = ('site_name',)
    
    def has_add_permission(self, request):
        # Only allow one instance
        return False
    
    class Media:
        css = {
            'all': ('admin/css/site_settings.css',)
        }