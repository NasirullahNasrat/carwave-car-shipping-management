from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
import uuid
from django.utils.translation import gettext_lazy as _
from django.core.files.storage import FileSystemStorage
from decimal import Decimal
from django.core.exceptions import ValidationError


# ====================== UTILITY FUNCTIONS ======================

def get_usd_currency():
    """Helper function to get or create USD currency"""
    from .models import Currency  # Import here to avoid circular imports
    try:
        return Currency.objects.get(code='USD')
    except Currency.DoesNotExist:
        return Currency.objects.create(
            code='USD',
            name='US Dollar',
            symbol='$',
            exchange_rate=1,
            is_base=True,
            is_active=True
        )


# ====================== CURRENCY CORE MODELS ======================

class ExchangeRateHistory(models.Model):
    """Model to track historical exchange rates"""
    currency = models.ForeignKey('Currency', on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=15, decimal_places=6)
    date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Exchange Rate History"
        verbose_name_plural = "Exchange Rate Histories"
        ordering = ['-date', '-created_at']
        indexes = [
            models.Index(fields=['currency', 'date']),
        ]

    def __str__(self):
        return f"{self.currency.code} @ {self.rate} on {self.date}"


class Currency(models.Model):
    """Model to store different currencies and their exchange rates"""
    code = models.CharField(max_length=3, unique=True, verbose_name="Currency Code")
    name = models.CharField(max_length=50, verbose_name="Currency Name")
    symbol = models.CharField(max_length=5, verbose_name="Currency Symbol")
    exchange_rate = models.DecimalField(
        max_digits=15, 
        decimal_places=6,
        verbose_name="Current Exchange Rate to Base Currency",
        help_text="1 unit of this currency equals how much in base currency"
    )
    is_base = models.BooleanField(default=False, verbose_name="Is Base Currency")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"
        ordering = ['code']

    def __str__(self):
        return f"{self.name} ({self.code})"

    def save(self, *args, **kwargs):
        # Create history record when exchange rate changes
        if self.pk:
            orig = Currency.objects.get(pk=self.pk)
            if orig.exchange_rate != self.exchange_rate:
                ExchangeRateHistory.objects.create(
                    currency=self,
                    rate=self.exchange_rate,
                    date=timezone.now().date()
                )
        super().save(*args, **kwargs)

    def get_rate_at_date(self, date):
        """Get the historical rate for a specific date"""
        if not date:
            return self.exchange_rate
            
        rate = ExchangeRateHistory.objects.filter(
            currency=self,
            date__lte=date
        ).order_by('-date', '-created_at').first()
        return rate.rate if rate else self.exchange_rate


class CurrencyAmountField(models.DecimalField):
    """Custom field to handle currency amounts with historical rates"""
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_digits', 15)
        kwargs.setdefault('decimal_places', 2)
        super().__init__(*args, **kwargs)


class CurrencyModelMixin:
    """Mixin for models that need currency conversion functionality"""
    
    def _convert_to_base(self, amount, currency_field_name, date_field_name=None):
        """
        Convert amount to base currency using historical rates if available
        """
        if amount is None:
            return Decimal('0')
        
        # Get the currency field
        currency = getattr(self, f"{currency_field_name}_currency")
        if currency is None or currency.is_base:
            return amount
        
        # Get the appropriate date for historical rate
        date = None
        if date_field_name:
            date = getattr(self, date_field_name)
        
        # Get the exchange rate (historical if date available)
        rate = currency.get_rate_at_date(date)
        return amount * Decimal(str(rate))


# ====================== REFERENCE TABLES ======================

class Related(models.Model):
    name = models.CharField(max_length=100, verbose_name="مربوطیت")
    
    class Meta:
        verbose_name = "مربوطیت"
        verbose_name_plural = "مربوطیت ها"
    
    def __str__(self):
        return self.name


class CarMark(models.Model):
    name = models.CharField(max_length=100, verbose_name="مارک")
    
    class Meta:
        verbose_name = "مارک موتر"
        verbose_name_plural = "مارک های موتر"
    
    def __str__(self):
        return self.name


class CarType(models.Model):
    mark = models.ForeignKey(CarMark, on_delete=models.CASCADE, verbose_name="مارک")
    name = models.CharField(max_length=100, verbose_name="نوع موتر")
    
    class Meta:
        verbose_name = "نوع موتر"
        verbose_name_plural = "انواع موتر"
    
    def __str__(self):
        return f"{self.mark} - {self.name}"


class ModelYear(models.Model):
    year = models.CharField(max_length=4, verbose_name="سال مدل")
    
    class Meta:
        verbose_name = "سال مدل"
        verbose_name_plural = "سال های مدل"
    
    def __str__(self):
        return self.year


class CarColor(models.Model):
    name = models.CharField(max_length=50, verbose_name="رنگ")
    
    class Meta:
        verbose_name = "رنگ موتر"
        verbose_name_plural = "رنگ های موتر"
    
    def __str__(self):
        return self.name


class CarAction(models.Model):
    name = models.CharField(max_length=100, verbose_name="آیشن")
    
    class Meta:
        verbose_name = "آیشن"
        verbose_name_plural = "آیشن ها"
    
    def __str__(self):
        return self.name


# ====================== MAIN CAR INFO ======================

class CarInfo(models.Model):
    """بخش اول - معلومات جنس (Vehicle Information)"""
    related = models.ForeignKey(Related, on_delete=models.SET_NULL, verbose_name="مربوطیت", null=True, blank=True)
    position = models.CharField(max_length=100, verbose_name="موقعیت", blank=True)
    color = models.ForeignKey(CarColor, on_delete=models.SET_NULL, verbose_name="رنگ", null=True, blank=True)
    action = models.ForeignKey(CarAction, on_delete=models.SET_NULL, verbose_name="آیشن", null=True, blank=True)
    model_year = models.ForeignKey(ModelYear, on_delete=models.SET_NULL, verbose_name="مدل سال", null=True, blank=True)
    car_type = models.ForeignKey(CarType, on_delete=models.SET_NULL, verbose_name="نوع", null=True, blank=True)
    mark = models.ForeignKey(CarMark, on_delete=models.SET_NULL, verbose_name="MARK", null=True, blank=True)
    vin = models.CharField(max_length=100, verbose_name="VIN#", blank=True)
    lot = models.CharField(max_length=100, verbose_name="LOT#", blank=True, unique=True, editable=False)
    
    class Meta:
        verbose_name = "معلومات جنس"
        verbose_name_plural = "معلومات جنس"
    
    def __str__(self):
        return f"{self.mark} - {self.model_year} - {self.vin}"
    
    def save(self, *args, **kwargs):
        if not self.lot:
            self.lot = f"LOT-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)


# ====================== PURCHASE INFORMATION ======================

# class PurchaseInfo(models.Model, CurrencyModelMixin):
#     """بخش دوم - معلومات خرید (Purchase Information)"""
#     car = models.OneToOneField(
#         CarInfo, 
#         on_delete=models.CASCADE, 
#         related_name="purchase_info",
#         verbose_name="وسیله نقلیه"
#     )

#     # Dollar Entry
#     paid_amount = CurrencyAmountField(
#         verbose_name="مبلغ پرداخت شده قیمت خرید ($)", 
#         validators=[MinValueValidator(0)],
#         default=0,
#         help_text="مبلغی که برای خرید این وسیله پرداخت شده است"
#     ) 
    
#     # Dollar Entry
#     purchase_price = CurrencyAmountField(
#         verbose_name="قیمت خرید ($)", 
#         validators=[MinValueValidator(0)],
#         default=0,
#         help_text="قیمت کامل خرید وسیله به دالر"
#     )

#     remain_purchase = CurrencyAmountField(
#         verbose_name="باقی انوایس خرید ($)",
#         editable=False,
#         default=0
#     )
    
#     buy_date = models.DateTimeField(
#         verbose_name="تاریخ و زمان خرید", 
#         default=timezone.now,
#         help_text="تاریخ و زمانی که وسیله خریداری شده است"
#     )
    
#     # Currency fields for purchase (default to USD)
#     paid_amount_currency = models.ForeignKey(
#         Currency,
#         on_delete=models.PROTECT,
#         related_name='+',
#         default=get_usd_currency,
#         verbose_name="Currency for مبلغ پرداخت شده"
#     )
    
#     purchase_price_currency = models.ForeignKey(
#         Currency,
#         on_delete=models.PROTECT,
#         related_name='+',
#         default=get_usd_currency,
#         verbose_name="Currency for قیمت خرید"
#     )
    
#     class Meta:
#         verbose_name = "معلومات خرید"
#         verbose_name_plural = "معلومات خرید"
    
#     def __str__(self):
#         return f"Purchase #{self.id} - {self.car.mark}"
    
#     def save(self, *args, **kwargs):
#         """Calculate remaining amount before saving"""
#         # Convert both amounts to base currency first
#         paid_in_base = self._convert_to_base(self.paid_amount, 'paid_amount', 'buy_date')
#         purchase_in_base = self._convert_to_base(self.purchase_price, 'purchase_price', 'buy_date')
        
#         self.remain_purchase = purchase_in_base - paid_in_base
#         super().save(*args, **kwargs)
    
#     @property
#     def formatted_remain_purchase(self):
#         """Helper property to display formatted remaining amount"""
#         return f"{self.remain_purchase:,.2f} $"
    
#     @property
#     def payment_status(self):
#         """Returns the payment status as text"""
#         if self.remain_purchase == 0:
#             return "کامل پرداخت شده"
#         elif self.remain_purchase == self.purchase_price:
#             return "پرداخت نشده"
#         else:
#             return "ناقص پرداخت شده"







from django.utils.safestring import mark_safe



class PurchaseInfo(models.Model, CurrencyModelMixin):
    """بخش دوم - معلومات خرید (Purchase Information)"""
    car = models.OneToOneField(
        CarInfo, 
        on_delete=models.CASCADE, 
        related_name="purchase_info",
        verbose_name="وسیله نقلیه"
    )

    # Dollar Entry
    paid_amount = CurrencyAmountField(
        verbose_name="مبلغ پرداخت شده قیمت خرید ($)", 
        validators=[MinValueValidator(0)],
        default=0,
        help_text="مبلغی که برای خرید این وسیله پرداخت شده است"
    ) 
    
    # Dollar Entry
    purchase_price = CurrencyAmountField(
        verbose_name="قیمت خرید ($)", 
        validators=[MinValueValidator(0)],
        default=0,
        help_text="قیمت کامل خرید وسیله به دالر"
    )

    remain_purchase = CurrencyAmountField(
        verbose_name="باقی انوایس خرید ($)",
        editable=False,
        default=0
    )
    
    buy_date = models.DateTimeField(
        verbose_name="تاریخ و زمان خرید", 
        default=timezone.now,
        help_text="تاریخ و زمانی که وسیله خریداری شده است"
    )
    
    payment_date = models.DateTimeField(
        verbose_name="تاریخ پرداخت باقی مانده",
        null=True,
        blank=True,
        help_text="تاریخی که باقی مانده پرداخت خواهد شد"
    )
    
    # Currency fields for purchase (default to USD)
    paid_amount_currency = models.ForeignKey(
        Currency,
        on_delete=models.PROTECT,
        related_name='+',
        default=get_usd_currency,
        verbose_name="Currency for مبلغ پرداخت شده"
    )
    
    purchase_price_currency = models.ForeignKey(
        Currency,
        on_delete=models.PROTECT,
        related_name='+',
        default=get_usd_currency,
        verbose_name="Currency for قیمت خرید"
    )
    
    class Meta:
        verbose_name = "معلومات خرید"
        verbose_name_plural = "معلومات خرید"
    
    def __str__(self):
        return f"Purchase #{self.id} - {self.car.mark}"
    
    def save(self, *args, **kwargs):
        """Calculate remaining amount before saving"""
        # Convert both amounts to base currency first
        paid_in_base = self._convert_to_base(self.paid_amount, 'paid_amount', 'buy_date')
        purchase_in_base = self._convert_to_base(self.purchase_price, 'purchase_price', 'buy_date')
        
        self.remain_purchase = purchase_in_base - paid_in_base
        
        # Automatically clear payment_date if fully paid
        if self.remain_purchase <= 0:
            self.payment_date = None
            
        super().save(*args, **kwargs)
    
    @property
    def formatted_remain_purchase(self):
        """Helper property to display formatted remaining amount"""
        return f"{self.remain_purchase:,.2f} $"
    
    @property
    def payment_status_with_icon(self):
        """Returns the payment status with icon and date if paid"""
        if self.remain_purchase == 0:
            return mark_safe(
                f'<span class="text-green-600">✓ پرداخت کامل'
                f'<span class="text-xs text-gray-500 block">تاریخ پرداخت: {self.buy_date.strftime("%Y-%m-%d") if self.buy_date else "---"}</span>'
                f'</span>'
            )
        elif self.remain_purchase == self.purchase_price:
            return mark_safe('<span class="text-red-600">✗ پرداخت نشده</span>')
        else:
            return mark_safe(
                f'<span class="text-yellow-600">↻ پرداخت ناقص'
                f'<span class="text-xs text-gray-500 block">باقی مانده: {self.formatted_remain_purchase}</span>'
                f'</span>'
            )














# ====================== SHIPPING INFORMATION ======================

class ShippingInfo(models.Model, CurrencyModelMixin):
    """بخش سوم - اطلاعات حمل و نقل و گمرکات"""
    car = models.OneToOneField(CarInfo, on_delete=models.CASCADE, related_name="shipping_info")
    date_arrived_in_dubai = models.DateField(verbose_name="تاریخ رسید به امارات", null=True, blank=True)
    
    # Total price to Dubai - stored in USD by default
    total_price_to_dubai = CurrencyAmountField(
        verbose_name="قیمت تمام شده الی دبی ($)",
        blank=True, null=True
    )
    total_price_to_dubai_currency = models.ForeignKey(
        Currency,
        on_delete=models.PROTECT,
        related_name='+',
        default=get_usd_currency,
        verbose_name="Currency for قیمت تمام شده الی دبی"
    )

    # Fields that can be in different currencies
    cash_paid_comission = CurrencyAmountField(verbose_name="کمیشن حواله پول", blank=True, null=True)
    cash_paid_comission_currency = models.ForeignKey(
        Currency, 
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name="Currency for کمیشن حواله پول",
        blank=True, 
        null=True
    )
    cash_paid_comission_date = models.DateField(
        verbose_name="تاریخ پرداخت کمیشن حواله پول",
        null=True,
        blank=True
    )
    
    dubai_paid_invoice = CurrencyAmountField(verbose_name="مبلغ پرداخت شده انوایس دبی", blank=True, null=True)
    dubai_paid_invoice_currency = models.ForeignKey(
        Currency, 
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name="Currency for مبلغ پرداخت شده انوایس دبی",
        blank=True, 
        null=True
    )
    dubai_paid_invoice_date = models.DateField(
        verbose_name="تاریخ پرداخت انوایس دبی",
        null=True,
        blank=True
    )
    
    attstion = CurrencyAmountField(verbose_name="ATTSTION INSSPECTION PORTCLIP$PRMI..", blank=True, null=True)
    attstion_currency = models.ForeignKey(
        Currency, 
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name="Currency for ATTSTION",
        blank=True, 
        null=True
    )
    attstion_date = models.DateField(
        verbose_name="تاریخ ATTSTION",
        null=True,
        blank=True
    )
    
    commission = CurrencyAmountField(verbose_name="COMISSION", blank=True, null=True)
    commission_currency = models.ForeignKey(
        Currency, 
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name="Currency for COMISSION",
        blank=True, 
        null=True
    )
    commission_date = models.DateField(
        verbose_name="تاریخ COMISSION",
        null=True,
        blank=True
    )
    
    clearing = CurrencyAmountField(verbose_name="CLEARING", blank=True, null=True)
    clearing_currency = models.ForeignKey(
        Currency, 
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name="Currency for CLEARING",
        blank=True, 
        null=True
    )
    clearing_date = models.DateField(
        verbose_name="تاریخ CLEARING",
        null=True,
        blank=True
    )
    
    duty_vat = CurrencyAmountField(verbose_name="DUTY/VAT", blank=True, null=True)
    duty_vat_currency = models.ForeignKey(
        Currency, 
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name="Currency for DUTY/VAT",
        blank=True, 
        null=True
    )
    duty_vat_date = models.DateField(
        verbose_name="تاریخ DUTY/VAT",
        null=True,
        blank=True
    )
    
    d_o = CurrencyAmountField(verbose_name="D/o", blank=True, null=True)
    d_o_currency = models.ForeignKey(
        Currency, 
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name="Currency for D/o",
        blank=True, 
        null=True
    )
    d_o_date = models.DateField(
        verbose_name="تاریخ D/o",
        null=True,
        blank=True
    )
    
    red_sea = CurrencyAmountField(verbose_name="RED SEA", blank=True, null=True)
    red_sea_currency = models.ForeignKey(
        Currency, 
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name="Currency for RED SEA",
        blank=True, 
        null=True
    )
    red_sea_date = models.DateField(
        verbose_name="تاریخ RED SEA",
        null=True,
        blank=True
    )
    
    towing = CurrencyAmountField(verbose_name="Towing", blank=True, null=True)
    towing_currency = models.ForeignKey(
        Currency, 
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name="Currency for Towing",
        blank=True, 
        null=True
    )
    towing_date = models.DateField(
        verbose_name="تاریخ Towing",
        null=True,
        blank=True
    )
    
    shipping = CurrencyAmountField(verbose_name="Shipping", blank=True, null=True)
    shipping_currency = models.ForeignKey(
        Currency, 
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name="Currency for Shipping",
        blank=True, 
        null=True
    )
    shipping_date = models.DateField(
        verbose_name="تاریخ Shipping",
        null=True,
        blank=True
    )
    
    etd_from_usa = models.DateField(verbose_name="ETD from USA", null=True, blank=True)
    cnt_number = models.CharField(max_length=100, verbose_name="Cnt#", blank=True)
    bkg_number = models.CharField(max_length=100, verbose_name="Bkg#", blank=True)
    
    port_clips_prmi = CurrencyAmountField(verbose_name="PORTCLIPSPRMI", blank=True, null=True)
    port_clips_prmi_currency = models.ForeignKey(
        Currency, 
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name="Currency for PORTCLIPSPRMI",
        blank=True, 
        null=True
    )
    port_clips_prmi_date = models.DateField(
        verbose_name="تاریخ PORTCLIPSPRMI",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "اطلاعات حمل و نقل"
        verbose_name_plural = "اطلاعات حمل و نقل"

    def __str__(self):
        return f"Shipping #{self.id} - {self.car.mark}"

    @property
    def mizan_invoice_dubai(self):
        """مجموع هزینه‌ها تا ATTSTION (converted to base currency)"""
        return sum([
            self._convert_to_base(self.commission, 'commission', 'commission_date'),
            self._convert_to_base(self.clearing, 'clearing', 'clearing_date'),
            self._convert_to_base(self.duty_vat, 'duty_vat', 'duty_vat_date'),
            self._convert_to_base(self.d_o, 'd_o', 'd_o_date'),
            self._convert_to_base(self.red_sea, 'red_sea', 'red_sea_date'),
            self._convert_to_base(self.towing, 'towing', 'towing_date'),
            self._convert_to_base(self.shipping, 'shipping', 'shipping_date'),
            self._convert_to_base(self.port_clips_prmi, 'port_clips_prmi', 'port_clips_prmi_date'),
            self._convert_to_base(self.attstion, 'attstion', 'attstion_date'),
        ])

    @property
    def dubai_remain_invoice(self):
        """میزان انوایس دبی attstion - مبلغ پرداخت شده (converted to base currency)"""
        paid_in_base = self._convert_to_base(self.dubai_paid_invoice, 'dubai_paid_invoice', 'dubai_paid_invoice_date')
        return self.mizan_invoice_dubai - paid_in_base

    @property
    def mizan_masaref_up_to_dubai(self):
        """مجموع مصارف تا دبی = مجموع هزینه‌ها + کمیشن نقدی (converted to base currency)"""
        comission_in_base = self._convert_to_base(self.cash_paid_comission, 'cash_paid_comission', 'cash_paid_comission_date')
        return self.mizan_invoice_dubai + comission_in_base

    @property
    def computed_total_price_to_dubai(self):
        """قیمت تمام شده تا دبی = قیمت خرید + مجموع مصارف تا دبی"""
        if self.car and hasattr(self.car, 'purchase_info'):
            purchase_info = self.car.purchase_info
            purchase_in_base = purchase_info._convert_to_base(
                purchase_info.purchase_price, 
                'purchase_price',
                'buy_date'
            )
            return purchase_in_base + self.mizan_masaref_up_to_dubai
        return self.mizan_masaref_up_to_dubai  # fallback if no purchase info


# ====================== WORLD EXPENSES ======================












class WorldExpenses(models.Model, CurrencyModelMixin):
    """بخش چهارم - معمارف مصارف انتقالات (World Expenses)"""
    car = models.OneToOneField(CarInfo, on_delete=models.CASCADE, related_name="world_expenses")
    herat_arrival_date = models.DateField(verbose_name="تاریخ رسید به هرات", null=True, blank=True)
    
    # Currency fields for Afghan entries
    business_company_comission = CurrencyAmountField(
        verbose_name="کمیشن شرکت تجارتی", 
        default=0
    )
    business_company_comission_currency = models.ForeignKey(
        Currency,
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name="Currency for کمیشن شرکت تجارتی",
        blank=True,
        null=True
    )
    business_company_comission_date = models.DateField(
        verbose_name="تاریخ پرداخت کمیشن شرکت تجارتی",
        null=True,
        blank=True
    )
    
    has_business_company_remain_comission = models.BooleanField(
        verbose_name="پرداخت باقی کمیشن تجاری",
        default=False
    )
    business_company_remain_comission = CurrencyAmountField(
        verbose_name="باقی کمیشن شرکت تجارتی", 
        default=0,
        blank=True
    )
    business_company_remain_comission_date = models.DateField(
        verbose_name="تاریخ باقی کمیشن شرکت تجارتی",
        null=True,
        blank=True
    )
    
    gomrok_payment = CurrencyAmountField(
        verbose_name="محصول گمرکی", 
        default=0
    )
    gomrok_payment_currency = models.ForeignKey(
        Currency,
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name="Currency for محصول گمرکی",
        blank=True,
        null=True
    )
    gomrok_payment_date = models.DateField(
        verbose_name="تاریخ پرداخت محصول گمرکی",
        null=True,
        blank=True
    )
    
    has_gomrok_remain_payment = models.BooleanField(
        verbose_name="پرداخت باقی محصول گمرکی",
        default=False
    )
    gomrok_remain_payment = CurrencyAmountField(
        verbose_name="باقی محصول گمرکی", 
        default=0,
        blank=True
    )
    gomrok_remain_payment_date = models.DateField(
        verbose_name="تاریخ باقی محصول گمرکی",
        null=True,
        blank=True
    )
    
    shipiping_price_to_islam_qala = CurrencyAmountField(
        verbose_name="قیمت شیپنگ به اسلام قلعه", 
        default=0
    )
    shipiping_price_to_islam_qala_currency = models.ForeignKey(
        Currency,
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name="Currency for قیمت شیپنگ",
        blank=True,
        null=True
    )
    shipiping_price_to_islam_qala_date = models.DateField(
        verbose_name="تاریخ پرداخت شیپنگ",
        null=True,
        blank=True
    )
    
    paid_value_for_shipping = CurrencyAmountField(
        verbose_name="مبلغ پرداخت شده شیپنګ", 
        default=0
    )
    paid_value_for_shipping_currency = models.ForeignKey(
        Currency,
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name="Currency for مبلغ پرداخت شده شیپنګ",
        blank=True,
        null=True
    )
    paid_value_for_shipping_date = models.DateField(
        verbose_name="تاریخ پرداخت شیپنګ",
        null=True,
        blank=True
    )
    
    remain_shipping_for_islam_qala = CurrencyAmountField(
        verbose_name="باقی شیپینک به اسلام قلعه", 
        default=0,
        editable=False
    )
    
    return_date_from_dubai = models.DateField(
        verbose_name="تاریخ بارگیری از دبی", 
        null=True, blank=True
    )

    class Meta:
        verbose_name = "مصارف انتقالات"
        verbose_name_plural = "مصارف انتقالات"

    def __str__(self):
        return f"World Expenses #{self.id} - {self.car.mark}"

    @property
    def amount_of_expeses_to_herat(self):
        """میزان مصارف الی هرات = قیمت شیپنگ به اسلام قلعه + محصول گمرکی + کمیشن شرکت تجارتی"""
        return (
            self._convert_to_base(self.shipiping_price_to_islam_qala, 'shipiping_price_to_islam_qala', 'shipiping_price_to_islam_qala_date') +
            self._convert_to_base(self.gomrok_payment, 'gomrok_payment', 'gomrok_payment_date') +
            self._convert_to_base(self.business_company_comission, 'business_company_comission', 'business_company_comission_date')
        )

    @property
    def expeses_up_to_herat(self):
        """مصارف تا هرات = قیمت شیپنگ به اسلام قلعه + محصول گمرکی + باقی محصول گمرکی"""
        return (
            self._convert_to_base(self.shipiping_price_to_islam_qala, 'shipiping_price_to_islam_qala', 'shipiping_price_to_islam_qala_date') +
            self._convert_to_base(self.gomrok_payment, 'gomrok_payment', 'gomrok_payment_date') +
            self._convert_to_base(self.business_company_comission, 'business_company_comission', 'business_company_comission_date')
        )

    @property
    def all_expeses_to_herat(self):
        """تمامی مصارف الی هرات = قیمت تمام شده تا دبی + مصارف تا هرات"""
        shipping_info = getattr(self.car, 'shipping_info', None)
        total_price_to_dubai = shipping_info.computed_total_price_to_dubai if shipping_info else Decimal('0')
        return total_price_to_dubai + self.expeses_up_to_herat

    def save(self, *args, **kwargs):
        # Calculate remaining shipping amount in base currency
        shipping_paid_in_base = self._convert_to_base(
            self.paid_value_for_shipping, 
            'paid_value_for_shipping',
            'paid_value_for_shipping_date'
        )
        shipping_total_in_base = self._convert_to_base(
            self.shipiping_price_to_islam_qala,
            'shipiping_price_to_islam_qala',
            'shipiping_price_to_islam_qala_date'
        )
        self.remain_shipping_for_islam_qala = shipping_total_in_base - shipping_paid_in_base
        
        # Clear remain comission fields if not applicable
        if not self.has_business_company_remain_comission:
            self.business_company_remain_comission = 0
            self.business_company_remain_comission_date = None
            
        # Clear remain gomrok fields if not applicable
        if not self.has_gomrok_remain_payment:
            self.gomrok_remain_payment = 0
            self.gomrok_remain_payment_date = None
            
        super().save(*args, **kwargs)

    def clean(self):
        super().clean()
        # Validate that if remain comission is yes, both value and date must be provided
        if self.has_business_company_remain_comission:
            if not self.business_company_remain_comission:
                raise ValidationError({
                    'business_company_remain_comission': 'مقدار باقی کمیشن شرکت تجارتی باید وارد شود'
                })
            if not self.business_company_remain_comission_date:
                raise ValidationError({
                    'business_company_remain_comission_date': 'تاریخ باقی کمیشن شرکت تجارتی باید وارد شود'
                })
                
        # Validate that if remain gomrok is yes, both value and date must be provided
        if self.has_gomrok_remain_payment:
            if not self.gomrok_remain_payment:
                raise ValidationError({
                    'gomrok_remain_payment': 'مقدار باقی محصول گمرکی باید وارد شود'
                })
            if not self.gomrok_remain_payment_date:
                raise ValidationError({
                    'gomrok_remain_payment_date': 'تاریخ باقی محصول گمرکی باید وارد شود'
                })

















# ====================== KABUL EXPENSES ======================

class KabulExpenses(models.Model, CurrencyModelMixin):
    """بخش پنجم - مصارف از هرات الى کابل (Kabul Expenses)"""
    car = models.OneToOneField(CarInfo, on_delete=models.CASCADE, related_name="kabul_expenses")
    
    herat_to_kabul_cost = CurrencyAmountField(
        verbose_name="کرایه از هرات الی کابل", 
        default=0
    )
    herat_to_kabul_cost_currency = models.ForeignKey(
        Currency,
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name="Currency for کرایه از هرات الی کابل",
        blank=True,
        null=True
    )
    herat_to_kabul_cost_date = models.DateField(
        verbose_name="تاریخ پرداخت کرایه",
        null=True,
        blank=True
    )
    
    has_remaining_price_from_herat_to_kabul = models.BooleanField(
        verbose_name="پرداخت باقی کرایه از هرات الی کابل",
        default=False
    )
    remaining_price_from_herat_to_kabul = CurrencyAmountField(
        verbose_name="باقی کرایه از هرات الی کابل", 
        default=0,
        blank=True
    )
    remaining_price_from_herat_to_kabul_date = models.DateField(
        verbose_name="تاریخ پرداخت",
        null=True,
        blank=True
    )
    
    arrival_date_kabul = models.DateField(
        verbose_name="تاریخ رسید به کابل", 
        null=True, 
        blank=True
    )

    class Meta:
        verbose_name = "مصارف کابل"
        verbose_name_plural = "مصارف کابل"

    def __str__(self):
        return f"Kabul Expenses #{self.id} - {self.car.mark}"

    @property
    def usa_to_kabul_cost(self):
        """میزان مصارف از امریکا الى کابل = مصارف الی هرات + کرایه هرات به کابل"""
        world_exp = getattr(self.car, 'world_expenses', None)
        amount_to_herat = world_exp.amount_of_expeses_to_herat if world_exp else Decimal('0')
        herat_to_kabul_in_base = self._convert_to_base(
            self.herat_to_kabul_cost,
            'herat_to_kabul_cost',
            'herat_to_kabul_cost_date'
        )
        return amount_to_herat + herat_to_kabul_in_base

    @property
    def total_cost_in_kabul(self):
        """قیمت تمام شد در کابل = تمام مصارف الی هرات + کرایه هرات به کابل"""
        world_exp = getattr(self.car, 'world_expenses', None)
        all_expenses = world_exp.all_expeses_to_herat if world_exp else Decimal('0')
        herat_to_kabul_in_base = self._convert_to_base(
            self.herat_to_kabul_cost,
            'herat_to_kabul_cost',
            'herat_to_kabul_cost_date'
        )
        return all_expenses + herat_to_kabul_in_base

    def save(self, *args, **kwargs):
        # Calculate remaining price in base currency
        herat_to_kabul_in_base = self._convert_to_base(
            self.herat_to_kabul_cost,
            'herat_to_kabul_cost',
            'herat_to_kabul_cost_date'
        )
        usa_to_kabul_in_base = self.usa_to_kabul_cost
        
        self.remaining_price_from_herat_to_kabul = (
            herat_to_kabul_in_base - usa_to_kabul_in_base
        )
        
        # Clear remaining price fields if not applicable
        if not self.has_remaining_price_from_herat_to_kabul:
            self.remaining_price_from_herat_to_kabul = 0
            self.remaining_price_from_herat_to_kabul_date = None
            
        super().save(*args, **kwargs)

    def clean(self):
        super().clean()
        # Validate that if remaining price is yes, both value and date must be provided
        if self.has_remaining_price_from_herat_to_kabul:
            if not self.remaining_price_from_herat_to_kabul:
                raise ValidationError({
                    'remaining_price_from_herat_to_kabul': 'مقدار باقی کرایه از هرات الی کابل باید وارد شود'
                })
            if not self.remaining_price_from_herat_to_kabul_date:
                raise ValidationError({
                    'remaining_price_from_herat_to_kabul_date': 'تاریخ پرداخت باید وارد شود'
                })


# ====================== REPAIR AND OTHER EXPENSES ======================

class RepairAndOtherExpenses(models.Model, CurrencyModelMixin):
    """بخش ششم - مصارف ترمیم و سایر هزینه ها (Repair and Other Expenses)"""
    car = models.OneToOneField(CarInfo, on_delete=models.CASCADE, related_name="repair_expenses")
    
    repair_cost = CurrencyAmountField(
        verbose_name="مصارف ترمیم", 
        default=0
    )
    repair_cost_currency = models.ForeignKey(
        Currency,
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name="Currency for مصارف ترمیم",
        blank=True,
        null=True
    )
    repair_cost_date = models.DateField(
        verbose_name="تاریخ پرداخت ترمیم",
        null=True,
        blank=True
    )
    
    remaining_repair_cost = CurrencyAmountField(
        verbose_name="باقی مصارف ترمیم", 
        default=0,
        help_text="This should be set manually and not automatically calculated"
    )
    
    palate_cost = CurrencyAmountField(
        verbose_name="مصارف پلیت", 
        default=0
    )
    palate_cost_currency = models.ForeignKey(
        Currency,
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name="Currency for مصارف پلیت",
        blank=True,
        null=True
    )
    palate_cost_date = models.DateField(
        verbose_name="تاریخ پرداخت پلیت",
        null=True,
        blank=True
    )
    
    palate_remaining_const = CurrencyAmountField(
        verbose_name="باقی مصارف پلیت", 
        default=0,
        help_text="This should be set manually and not automatically calculated"
    )

    class Meta:
        verbose_name = "مصارف ترمیم و سایر هزینه ها"
        verbose_name_plural = "مصارف ترمیم و سایر هزینه ها"

    def __str__(self):
        return f"Repair & Other #{self.id} - {self.car.mark}"

    @property
    def final_cost(self):
        """تمام شد نهایی = مصارف ترمیم + مصارف پلیت + مصارف کابل"""
        kabul_exp = getattr(self.car, 'kabul_expenses', None)
        kabul_total = kabul_exp.total_cost_in_kabul if kabul_exp else Decimal('0')
        
        repair_in_base = self._convert_to_base(self.repair_cost, 'repair_cost', 'repair_cost_date')
        palate_in_base = self._convert_to_base(self.palate_cost, 'palate_cost', 'palate_cost_date')
        
        return repair_in_base + palate_in_base + kabul_total










# # ====================== SALE INFORMATION ======================

# class SaleInfo(models.Model):
#     """بخش هفتم - اطلاعات فروش (Sale Information)"""
#     STATUS_READY = 'آماده فروش'
#     STATUS_SOLD = 'فروخته شده'
#     STATUS_IN_TRANSIT = 'در راه'

#     STATUS_CHOICES = [
#         (STATUS_READY, 'آماده فروش'),
#         (STATUS_SOLD, 'فروخته شده'),
#         (STATUS_IN_TRANSIT, 'در راه'),
#     ]

#     car = models.OneToOneField(CarInfo, on_delete=models.CASCADE, related_name="sale_info")
#     status = models.CharField(
#         max_length=20,
#         verbose_name="حالت",
#         choices=STATUS_CHOICES,
#         default=STATUS_READY
#     )
#     split_50_50 = models.CharField(max_length=100, verbose_name="50/50 مقدار", blank=True)
#     buyer_remain_payment_date = models.DateField(verbose_name="تاریخ پرداخت باقی خریدار", null=True, blank=True)
#     remaining_price_of_buyer = CurrencyAmountField(verbose_name="باقی خریدار", default=0)
#     buyer_info = models.TextField(verbose_name="شهریت خریدار", blank=True)
#     sale_date = models.DateField(verbose_name="تاریخ فروش", null=True, blank=True)

#     sale_price = CurrencyAmountField(
#         verbose_name="قیمت فروش", 
#         default=0,
#         help_text="For sold cars, enter the sale price manually. For unsold cars, it will be automatically set to the repair and other expenses final cost."
#     )
#     sale_price_currency = models.ForeignKey(
#         Currency,
#         on_delete=models.PROTECT,
#         related_name='+',
#         default=get_usd_currency,
#         verbose_name="Currency for قیمت فروش"
#     )

#     class Meta:
#         verbose_name = "اطلاعات فروش"
#         verbose_name_plural = "اطلاعات فروش"

#     def __str__(self):
#         return f"Sale #{self.id} - {self.car.mark} - {self.get_status_display()}"

#     def clean(self):
#         """Custom validation"""
#         super().clean()
        
#         if self.status == self.STATUS_SOLD:
#             if not self.sale_price:
#                 raise ValidationError("Sale price must be set for sold cars")
#             if not self.sale_date:
#                 raise ValidationError("Sale date must be set for sold cars")
#             if self.sale_price <= 0:
#                 raise ValidationError("Sale price must be positive for sold cars")

#     def save(self, *args, **kwargs):
#         # For non-sold cars, set sale_price to RepairAndOtherExpenses.final_cost
#         if self.status != self.STATUS_SOLD:
#             repair_expenses = getattr(self.car, 'repair_expenses', None)
#             if repair_expenses:
#                 self.sale_price = repair_expenses.final_cost
#             else:
#                 self.sale_price = Decimal('0')
                
#         super().save(*args, **kwargs)

#     @property
#     def repair_final_cost(self):
#         """Direct reference to RepairAndOtherExpenses.final_cost"""
#         repair_expenses = getattr(self.car, 'repair_expenses', None)
#         return repair_expenses.final_cost if repair_expenses else Decimal('0')

#     @property
#     def sale_commission(self):
#         """Calculate 2% commission + 100 fixed fee (only for sold cars)"""
#         if self.status != self.STATUS_SOLD:
#             return Decimal('0')
        
#         # Convert sale price to base currency first
#         sale_in_base = CurrencyModelMixin()._convert_to_base(
#             self.sale_price,
#             'sale_price',
#             'sale_date'
#         )
#         return (sale_in_base * Decimal('0.02')) + Decimal('100')

#     @property
#     def special_sale_price(self):
#         """Sale price minus commission (only for sold cars)"""
#         if self.status != self.STATUS_SOLD:
#             return Decimal('0')
            
#         sale_in_base = CurrencyModelMixin()._convert_to_base(
#             self.sale_price,
#             'sale_price',
#             'sale_date'
#         )
#         return sale_in_base - self.sale_commission

#     @property
#     def benefit(self):
#         """Calculate benefit (only for sold cars)"""
#         if self.status != self.STATUS_SOLD:
#             return Decimal('0')
#         return self.special_sale_price - self.repair_final_cost

#     @property
#     def benefit_person_1(self):
#         """50% of benefit for person 1 (only for sold cars)"""
#         return self.benefit / 2 if self.status == self.STATUS_SOLD else Decimal('0')

#     @property
#     def benefit_person_2(self):
#         """50% of benefit for person 2 (only for sold cars)"""
#         return self.benefit / 2 if self.status == self.STATUS_SOLD else Decimal('0')

#     @property
#     def capital_bound(self):
#         """Capital bound is 0 for sold cars, otherwise repair_final_cost"""
#         return Decimal('0') if self.status == self.STATUS_SOLD else self.repair_final_cost




# class SaleInfo(models.Model, CurrencyModelMixin):
#     """بخش هفتم - اطلاعات فروش (Sale Information)"""
#     STATUS_READY = 'آماده فروش'
#     STATUS_SOLD = 'فروخته شده'
#     STATUS_IN_TRANSIT = 'در راه'

#     STATUS_CHOICES = [
#         (STATUS_READY, 'آماده فروش'),
#         (STATUS_SOLD, 'فروخته شده'),
#         (STATUS_IN_TRANSIT, 'در راه'),
#     ]

#     car = models.OneToOneField('CarInfo', on_delete=models.CASCADE, related_name="sale_info")
#     status = models.CharField(
#         max_length=20,
#         verbose_name="حالت",
#         choices=STATUS_CHOICES,
#         default=STATUS_READY
#     )
#     split_50_50 = models.CharField(max_length=100, verbose_name="50/50 مقدار", blank=True)
#     buyer_remain_payment_date = models.DateField(verbose_name="تاریخ پرداخت باقی خریدار", null=True, blank=True)
#     remaining_price_of_buyer = models.DecimalField(
#         verbose_name="باقی خریدار",
#         max_digits=12,
#         decimal_places=2,
#         default=0
#     )
#     buyer_info = models.TextField(verbose_name="شهریت خریدار", blank=True)
#     sale_date = models.DateField(verbose_name="تاریخ فروش", null=True, blank=True)

#     sale_price = models.DecimalField(
#         verbose_name="قیمت فروش",
#         max_digits=12,
#         decimal_places=2,
#         default=0,
#         help_text="For sold cars, enter the sale price manually. For unsold cars, it will be automatically set to the repair and other expenses final cost."
#     )
#     sale_price_currency = models.ForeignKey(
#         'Currency',
#         on_delete=models.PROTECT,
#         related_name='+',
#         default=get_usd_currency,
#         verbose_name="Currency for قیمت فروش"
#     )

#     class Meta:
#         verbose_name = "اطلاعات فروش"
#         verbose_name_plural = "اطلاعات فروش"

#     def __str__(self):
#         return f"Sale #{self.id} - {self.car.mark} - {self.get_status_display()}"

#     def clean(self):
#         """Custom validation"""
#         super().clean()
        
#         if self.status == self.STATUS_SOLD:
#             if not self.sale_price:
#                 raise ValidationError("Sale price must be set for sold cars")
#             if not self.sale_date:
#                 raise ValidationError("Sale date must be set for sold cars")
#             if self.sale_price <= 0:
#                 raise ValidationError("Sale price must be positive for sold cars")

#     def save(self, *args, **kwargs):
#         # For non-sold cars, set sale_price to RepairAndOtherExpenses.final_cost
#         if self.status != self.STATUS_SOLD:
#             repair_expenses = getattr(self.car, 'repair_expenses', None)
#             if repair_expenses:
#                 self.sale_price = repair_expenses.final_cost
#             else:
#                 self.sale_price = Decimal('0')
                
#         super().save(*args, **kwargs)

#     def _get_currency_field(self, field_name):
#         """Helper method to get the currency field for a given amount field"""
#         if field_name == 'sale_price':
#             return self.sale_price_currency
#         return None

#     @property
#     def repair_final_cost(self):
#         """Direct reference to RepairAndOtherExpenses.final_cost"""
#         repair_expenses = getattr(self.car, 'repair_expenses', None)
#         return repair_expenses.final_cost if repair_expenses else Decimal('0')

#     @property
#     def sale_commission(self):
#         """Calculate 2% commission + 100 fixed fee (only for sold cars)"""
#         if self.status != self.STATUS_SOLD:
#             return Decimal('0')
        
#         sale_in_base = self._convert_to_base(
#             self.sale_price,
#             'sale_price',
#             self.sale_date
#         )
#         return (sale_in_base * Decimal('0.02')) + Decimal('100')

#     @property
#     def special_sale_price(self):
#         """Sale price minus commission (only for sold cars)"""
#         if self.status != self.STATUS_SOLD:
#             return Decimal('0')
            
#         sale_in_base = self._convert_to_base(
#             self.sale_price,
#             'sale_price',
#             self.sale_date
#         )
#         return sale_in_base - self.sale_commission

#     @property
#     def benefit(self):
#         """Calculate benefit (only for sold cars)"""
#         if self.status != self.STATUS_SOLD:
#             return Decimal('0')
#         return self.special_sale_price - self.repair_final_cost

#     @property
#     def benefit_person_1(self):
#         """50% of benefit for person 1 (only for sold cars)"""
#         return self.benefit / 2 if self.status == self.STATUS_SOLD else Decimal('0')

#     @property
#     def benefit_person_2(self):
#         """50% of benefit for person 2 (only for sold cars)"""
#         return self.benefit / 2 if self.status == self.STATUS_SOLD else Decimal('0')

#     @property
#     def capital_bound(self):
#         """Capital bound is 0 for sold cars, otherwise repair_final_cost"""
#         return Decimal('0') if self.status == self.STATUS_SOLD else self.repair_final_cost







class Buyer(models.Model):
    """Model to store buyer information"""
    name = models.CharField(max_length=255, verbose_name="نام خریدار")
    contact_info = models.TextField(verbose_name="اطلاعات تماس", blank=True)
    address = models.TextField(verbose_name="آدرس", blank=True)
    national_id = models.CharField(max_length=20, verbose_name="نمبر تذکره", blank=True)
    additional_info = models.TextField(verbose_name="اطلاعات اضافی", blank=True)

    class Meta:
        verbose_name = "خریدار"
        verbose_name_plural = "خریداران"

    def __str__(self):
        return self.name


class SaleInfo(models.Model, CurrencyModelMixin):
    """بخش هفتم - اطلاعات فروش (Sale Information)"""
    STATUS_READY = 'آماده فروش'
    STATUS_SOLD = 'فروخته شده'
    STATUS_IN_TRANSIT = 'در راه'

    STATUS_CHOICES = [
        (STATUS_READY, 'آماده فروش'),
        (STATUS_SOLD, 'فروخته شده'),
        (STATUS_IN_TRANSIT, 'در راه'),
    ]

    car = models.OneToOneField('CarInfo', on_delete=models.CASCADE, related_name="sale_info")
    status = models.CharField(
        max_length=20,
        verbose_name="حالت",
        choices=STATUS_CHOICES,
        default=STATUS_READY
    )
    # split_50_50 = models.CharField(max_length=100, verbose_name="50/50 مقدار", blank=True)
    buyer_remain_payment_date = models.DateField(verbose_name="تاریخ پرداخت باقی خریدار", null=True, blank=True)
    remaining_price_of_buyer = models.DecimalField(
        verbose_name="باقی خریدار",
        max_digits=12,
        decimal_places=2,
        default=0
    )
    buyer = models.ForeignKey(
        Buyer,
        on_delete=models.SET_NULL,
        verbose_name="خریدار",
        null=True,
        blank=True
    )
    sale_date = models.DateField(verbose_name="تاریخ فروش", null=True, blank=True)

    sale_price = models.DecimalField(
        verbose_name="قیمت فروش",
        max_digits=12,
        decimal_places=2,
        default=0,
        help_text="For sold cars, enter the sale price manually. For unsold cars, it will be automatically set to the repair and other expenses final cost."
    )
    sale_price_currency = models.ForeignKey(
        'Currency',
        on_delete=models.PROTECT,
        related_name='+',
        default=get_usd_currency,
        verbose_name="Currency for قیمت فروش"
    )

    class Meta:
        verbose_name = "اطلاعات فروش"
        verbose_name_plural = "اطلاعات فروش"

    def __str__(self):
        return f"Sale #{self.id} - {self.car.mark} - {self.get_status_display()}"

    def clean(self):
        """Custom validation"""
        super().clean()
        
        if self.status == self.STATUS_SOLD:
            if not self.sale_price:
                raise ValidationError("Sale price must be set for sold cars")
            if not self.sale_date:
                raise ValidationError("Sale date must be set for sold cars")
            if self.sale_price <= 0:
                raise ValidationError("Sale price must be positive for sold cars")
            if not self.buyer:
                raise ValidationError("Buyer must be specified for sold cars")

    def save(self, *args, **kwargs):
        # For non-sold cars, set sale_price to RepairAndOtherExpenses.final_cost
        if self.status != self.STATUS_SOLD:
            repair_expenses = getattr(self.car, 'repair_expenses', None)
            if repair_expenses:
                self.sale_price = repair_expenses.final_cost
            else:
                self.sale_price = Decimal('0')
                
        super().save(*args, **kwargs)

    def _get_currency_field(self, field_name):
        """Helper method to get the currency field for a given amount field"""
        if field_name == 'sale_price':
            return self.sale_price_currency
        return None

    @property
    def repair_final_cost(self):
        """Direct reference to RepairAndOtherExpenses.final_cost"""
        repair_expenses = getattr(self.car, 'repair_expenses', None)
        return repair_expenses.final_cost if repair_expenses else Decimal('0')

    @property
    def sale_commission(self):
        """Calculate 2% commission + 100 fixed fee (only for sold cars)"""
        if self.status != self.STATUS_SOLD:
            return Decimal('0')
        
        sale_in_base = self._convert_to_base(
            self.sale_price,
            'sale_price',
            self.sale_date
        )
        return (sale_in_base * Decimal('0.02')) + Decimal('100')

    @property
    def special_sale_price(self):
        """Sale price minus commission (only for sold cars)"""
        if self.status != self.STATUS_SOLD:
            return Decimal('0')
            
        sale_in_base = self._convert_to_base(
            self.sale_price,
            'sale_price',
            self.sale_date
        )
        return sale_in_base - self.sale_commission

    @property
    def benefit(self):
        """Calculate benefit (only for sold cars)"""
        if self.status != self.STATUS_SOLD:
            return Decimal('0')
        return self.special_sale_price - self.repair_final_cost

    @property
    def benefit_person_1(self):
        """50% of benefit for person 1 (only for sold cars)"""
        return self.benefit / 2 if self.status == self.STATUS_SOLD else Decimal('0')

    @property
    def benefit_person_2(self):
        """50% of benefit for person 2 (only for sold cars)"""
        return self.benefit / 2 if self.status == self.STATUS_SOLD else Decimal('0')

    @property
    def capital_bound(self):
        """Capital bound is 0 for sold cars, otherwise repair_final_cost"""
        return Decimal('0') if self.status == self.STATUS_SOLD else self.repair_final_cost












# ====================== CAR IMAGES ======================

class CarImages(models.Model):
    car = models.ForeignKey(CarInfo, on_delete=models.CASCADE, related_name="images", verbose_name="موتر")
    image = models.ImageField(upload_to='car_images/', verbose_name="عکس موتر")
    description = models.CharField(max_length=255, blank=True, verbose_name="توضیحات")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="زمان آپلود")

    class Meta:
        verbose_name = "عکس موتر"
        verbose_name_plural = "عکس‌های موتر"

    def __str__(self):
        return f"عکس از {self.car} - {self.description or _('بدون توضیح')}"


# ====================== DASHBOARD SETTINGS ======================

class DashboardSetting(models.Model):
    """
    Simple site settings model
    """
    site_name = models.CharField(
        verbose_name=_('Site Name'), 
        max_length=100,
        default='سیستم من',
        blank=True,
        null=True
    )
    
    logo = models.ImageField(
        verbose_name=_('Logo'),
        upload_to='site_logos/',
        blank=True,
        null=True,
        help_text='لوگوی سیستم (ترجیحاً با پسزمینه شفاف)'
    )
    
    address = models.TextField(
        verbose_name=_('Address'),
        blank=True,
        null=True,
        help_text='آدرس کامل'
    )
    
    email = models.EmailField(
        verbose_name=_('Email'),
        blank=True,
        null=True,
        help_text='ایمیل تماس'
    )
    
    phone_number = models.CharField(
        verbose_name=_('Phone Number'),
        max_length=20,
        blank=True,
        null=True,
        help_text='شماره تماس'
    )
    
    base_currency = models.ForeignKey(
        Currency,
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name="Base Currency",
        help_text="The base currency used for all calculations",
        blank=True,
        null=True,
        default=get_usd_currency
    )
    
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Last Updated'))

    # Singleton pattern implementation
    def save(self, *args, **kwargs):
        # Ensure this is the only instance
        self.pk = 1
        super().save(*args, **kwargs)
    
    @classmethod
    def load(cls):
        """Load the single settings instance, creating it if necessary"""
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
    
    class Meta:
        verbose_name = _('Site Settings')
        verbose_name_plural = _('Site Settings')
    
    def __str__(self):
        return self.site_name or "Site Settings"