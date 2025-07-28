from django import forms
from .models import *
from django_select2.forms import Select2Widget, Select2MultipleWidget
from django.utils.translation import gettext_lazy as _


class RelatedForm(forms.ModelForm):
    class Meta:
        model = Related
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 mt-1 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
            }),
        }

class CarMarkForm(forms.ModelForm):
    class Meta:
        model = CarMark
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 mt-1 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
            }),
        }

class CarTypeForm(forms.ModelForm):
    class Meta:
        model = CarType
        fields = ['mark', 'name']
        widgets = {
            'mark': forms.Select(attrs={
                'class': 'w-full px-4 py-2 mt-1 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
            }),
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 mt-1 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
            }),
        }

class ModelYearForm(forms.ModelForm):
    class Meta:
        model = ModelYear
        fields = ['year']
        widgets = {
            'year': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 mt-1 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
                'placeholder': 'مثال: 2000'
            }),
        }
        labels = {
            'year': 'سال مدل'
        }
        help_texts = {
            'year': 'سال مدل را به عدد وارد کنید'
        }

class CarColorForm(forms.ModelForm):
    class Meta:
        model = CarColor
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 mt-1 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
            }),
        }

class CarActionForm(forms.ModelForm):
    class Meta:
        model = CarAction
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 mt-1 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
            }),
        }


class CarInfoForm(forms.ModelForm):
    class Meta:
        model = CarInfo
        fields = '__all__'
        widgets = {
            'related': Select2Widget(attrs={
                'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
                'data-placeholder': 'مربوطیت را انتخاب کنید'
            }),
            'position': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
                'placeholder': 'موقعیت را وارد کنید'
            }),
            'color': Select2Widget(attrs={
                'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
                'data-placeholder': 'رنگ را انتخاب کنید'
            }),
            'action': Select2Widget(attrs={
                'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
                'data-placeholder': 'آیشن را انتخاب کنید'
            }),
            'model_year': Select2Widget(attrs={
                'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
                'data-placeholder': 'مدل سال را انتخاب کنید'
            }),
            'car_type': Select2Widget(attrs={
                'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
                'data-placeholder': 'نوع را انتخاب کنید'
            }),
            'mark': Select2Widget(attrs={
                'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
                'data-placeholder': 'مارک را انتخاب کنید'
            }),
            'vin': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
                'placeholder': 'VIN را وارد کنید'
            }),
        }





# class PurchaseInfoForm(forms.ModelForm):
#     class Meta:
#         model = PurchaseInfo
#         fields = ['car', 'purchase_price',  'paid_amount', 'buy_date']
#         widgets = {
#             'car': Select2Widget(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                 'data-placeholder': 'موتر را انتخاب کنید'
#             }),
#             'paid_amount': forms.NumberInput(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                 'placeholder': 'مبلغ پرداخت شده'
#             }),
#             'purchase_price': forms.NumberInput(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                 'placeholder': 'قیمت خرید'
#             }),
#             'buy_date': forms.DateTimeInput(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                 'type': 'datetime-local'
#             }),
#         }
#         labels = {
#             'car': 'موتر',
#             'paid_amount': 'مبلغ پرداخت شده',
#             'purchase_price': 'قیمت خرید',
#             'buy_date': 'تاریخ خرید',
#         }






class PurchaseInfoForm(forms.ModelForm):
    payment_status = forms.CharField(
        label="وضعیت پرداخت",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-3 py-2 bg-gray-100 border border-gray-300 rounded-md shadow-sm',
            'readonly': True
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.initial['payment_status'] = self.instance.payment_status_with_icon
        # ... rest of your __init__ code ...

    class Meta:
        model = PurchaseInfo
        fields = ['car', 'purchase_price', 'paid_amount', 'buy_date', 'payment_date', 'payment_status']
        widgets = {
            'car': Select2Widget(attrs={
                'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
                'data-placeholder': 'موتر را انتخاب کنید'
            }),
            'paid_amount': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
                'placeholder': 'مبلغ پرداخت شده'
            }),
            'purchase_price': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
                'placeholder': 'قیمت خرید'
            }),
            'buy_date': forms.DateTimeInput(attrs={
                'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
                'type': 'datetime-local'
            }),
            'payment_date': forms.DateTimeInput(attrs={
                'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
                'type': 'datetime-local'
            }),
        }
        labels = {
            'car': 'موتر',
            'paid_amount': 'مبلغ پرداخت شده',
            'purchase_price': 'قیمت خرید',
            'buy_date': 'تاریخ خرید',
            'payment_date': 'تاریخ پرداخت باقی مانده',
        }















# class ShippingInfoForm(forms.ModelForm):
#     class Meta:
#         model = ShippingInfo
#         fields = '__all__'
#         widgets = {
#             'car': Select2Widget(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                 'data-placeholder': 'موتر را انتخاب کنید'
#             }),
#             'date_arrived_in_dubai': forms.DateInput(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                 'type': 'date'
#             }),
#             'etd_from_usa': forms.DateInput(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                 'type': 'date'
#             }),
#         }
        
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        
#         # Get all currency fields (fields ending with _currency)
#         currency_fields = [f for f in self.fields if f.endswith('_currency')]
        
#         for field_name, field in self.fields.items():
#             # Style decimal fields
#             if isinstance(field, forms.DecimalField):
#                 field.widget.attrs.update({
#                     'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                     'step': '0.01'
#                 })
#             # Style char fields
#             elif isinstance(field, forms.CharField):
#                 field.widget.attrs.update({
#                     'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out'
#                 })
#             # Style currency select fields
#             elif field_name in currency_fields:
#                 field.widget.attrs.update({
#                     'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out'
#                 })
#     def get_currency_fields(self):
#             """Returns a list of tuples (amount_field, currency_field) for paired fields"""
#             currency_pairs = []
#             for field_name, field in self.fields.items():
#                 if field_name.endswith('_currency'):
#                     amount_field_name = field_name.replace('_currency', '')
#                     if amount_field_name in self.fields:
#                         currency_pairs.append((amount_field_name, field_name))
#             return currency_pairs
        
#     def get_regular_fields(self):
#         """Returns non-currency paired fields"""
#         currency_fields = [f[1] for f in self.get_currency_fields()]
#         return [
#             (field_name, field) 
#             for field_name, field in self.fields.items() 
#             if field_name not in currency_fields and not field_name.endswith('_currency')
#         ]            






# class ShippingInfoForm(forms.ModelForm):
#     # List of fields that have associated date fields
#     currency_date_fields = [
#         'shipping', 'towing', 'red_sea', 'd_o', 'duty_vat', 
#         'clearing', 'commission', 'attstion', 'dubai_paid_invoice',
#         'cash_paid_comission', 'port_clips_prmi'
#     ]
    
#     class Meta:
#         model = ShippingInfo
#         fields = '__all__'
#         widgets = {
#             'car': Select2Widget(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                 'data-placeholder': 'موتر را انتخاب کنید'
#             }),
#             'date_arrived_in_dubai': forms.DateInput(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                 'type': 'date'
#             }),
#             'etd_from_usa': forms.DateInput(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                 'type': 'date'
#             }),
#         }
        
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        
#         # Set today's date as default for all date fields when creating new record
#         if not self.instance.pk:
#             today = timezone.now().date()
#             for field in self.currency_date_fields:
#                 date_field = f"{field}_date"
#                 if date_field in self.fields:
#                     self.initial[date_field] = today
        
#         # Style all fields
#         for field_name, field in self.fields.items():
#             if isinstance(field, forms.DecimalField):
#                 field.widget.attrs.update({
#                     'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                     'step': '0.01'
#                 })
#             elif isinstance(field, forms.CharField):
#                 field.widget.attrs.update({
#                     'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out'
#                 })
#             elif field_name.endswith('_currency'):
#                 field.widget.attrs.update({
#                     'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out'
#                 })
#             elif isinstance(field, forms.DateField):
#                 field.widget = forms.DateInput(attrs={
#                     'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                     'type': 'date'
#                 })










class ShippingInfoForm(forms.ModelForm):
    class Meta:
        model = ShippingInfo
        fields = '__all__'
        widgets = {
            'date_arrived_in_dubai': forms.DateInput(attrs={'type': 'date'}),
            'cash_paid_comission_date': forms.DateInput(attrs={'type': 'date'}),
            'dubai_paid_invoice_date': forms.DateInput(attrs={'type': 'date'}),
            'attstion_date': forms.DateInput(attrs={'type': 'date'}),
            'commission_date': forms.DateInput(attrs={'type': 'date'}),
            'clearing_date': forms.DateInput(attrs={'type': 'date'}),
            'duty_vat_date': forms.DateInput(attrs={'type': 'date'}),
            'd_o_date': forms.DateInput(attrs={'type': 'date'}),
            'red_sea_date': forms.DateInput(attrs={'type': 'date'}),
            'towing_date': forms.DateInput(attrs={'type': 'date'}),
            'shipping_date': forms.DateInput(attrs={'type': 'date'}),
            'etd_from_usa': forms.DateInput(attrs={'type': 'date'}),
            'port_clips_prmi_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'car': _('خودرو'),
            'date_arrived_in_dubai': _('تاریخ رسید به امارات'),
            'total_price_to_dubai': _('قیمت تمام شده الی دبی ($)'),
            'cash_paid_comission': _('کمیشن حواله پول'),
            'dubai_paid_invoice': _('مبلغ پرداخت شده انوایس دبی'),
            'attstion': _('ATTSTION INSSPECTION PORTCLIP$PRMI..'),
            'commission': _('COMISSION'),
            'clearing': _('CLEARING'),
            'duty_vat': _('DUTY/VAT'),
            'd_o': _('D/o'),
            'red_sea': _('RED SEA'),
            'towing': _('Towing'),
            'shipping': _('Shipping'),
            'etd_from_usa': _('ETD from USA'),
            'cnt_number': _('Cnt#'),
            'bkg_number': _('Bkg#'),
            'port_clips_prmi': _('PORTCLIPSPRMI'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set currency field querysets
        currency_fields = [f.name for f in self._meta.model._meta.get_fields() 
                          if f.name.endswith('_currency')]
        
        for field in currency_fields:
            self.fields[field].queryset = Currency.objects.all()
            self.fields[field].empty_label = _('انتخاب ارز')



















# class WorldExpensesForm(forms.ModelForm):
#     class Meta:
#         model = WorldExpenses
#         fields = '__all__'
#         widgets = {
#             'car': Select2Widget(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                 'data-placeholder': 'موتر را انتخاب کنید'
#             }),
#             'herat_arrival_date': forms.DateInput(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                 'type': 'date'
#             }),
#             'return_date_from_dubai': forms.DateInput(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                 'type': 'date'
#             }),
#         }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Style all decimal fields consistently
#         for field_name, field in self.fields.items():
#             if isinstance(field, forms.DecimalField):
#                 field.widget.attrs.update({
#                     'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                     'step': '0.01'
#                 })
#             elif isinstance(field, forms.CharField):
#                 field.widget.attrs.update({
#                     'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out'
#                 })

#         # Add readonly fields for calculated properties
#         self.fields['expeses_up_to_herat'] = forms.DecimalField(
#             required=False,
#             disabled=True,
#             label='میزان مصارف الی هرات',
#             widget=forms.NumberInput(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-gray-100 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#             })
#         )
#         self.fields['all_expeses_to_herat'] = forms.DecimalField(
#             required=False,
#             disabled=True,
#             label='تمام شد الی هرات',
#             widget=forms.NumberInput(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-gray-100 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#             })
#         )

#     def clean(self):
#         cleaned_data = super().clean()
#         # You can add custom validation here if needed
#         return cleaned_data






# class WorldExpensesForm(forms.ModelForm):
#     class Meta:
#         model = WorldExpenses
#         fields = '__all__'
#         widgets = {
#             'car': Select2Widget(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                 'data-placeholder': 'موتر را انتخاب کنید'
#             }),
#             'herat_arrival_date': forms.DateInput(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                 'type': 'date'
#             }),
#             'return_date_from_dubai': forms.DateInput(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                 'type': 'date'
#             }),
#         }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        
#         # Style all fields consistently
#         for field_name, field in self.fields.items():
#             if isinstance(field, forms.DecimalField):
#                 field.widget.attrs.update({
#                     'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                     'step': '0.01'
#                 })
#             elif isinstance(field, forms.CharField):
#                 field.widget.attrs.update({
#                     'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out'
#                 })
#             elif isinstance(field, forms.ModelChoiceField):
#                 field.widget.attrs.update({
#                     'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out'
#                 })

#         # Add readonly fields for calculated properties
#         self.fields['expeses_up_to_herat'] = forms.DecimalField(
#             required=False,
#             disabled=True,
#             label='میزان مصارف الی هرات',
#             widget=forms.NumberInput(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-gray-100 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#             })
#         )
#         self.fields['all_expeses_to_herat'] = forms.DecimalField(
#             required=False,
#             disabled=True,
#             label='تمام شد الی هرات',
#             widget=forms.NumberInput(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-gray-100 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#             })
#         )

#     def clean(self):
#         cleaned_data = super().clean()
#         # You can add custom validation here if needed
#         return cleaned_data







# class WorldExpensesForm(forms.ModelForm):
#     class Meta:
#         model = WorldExpenses
#         fields = '__all__'
#         widgets = {
#             'car': Select2Widget(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                 'data-placeholder': 'موتر را انتخاب کنید'
#             }),
#             'herat_arrival_date': forms.DateInput(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                 'type': 'date'
#             }),
#             'return_date_from_dubai': forms.DateInput(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                 'type': 'date'
#             }),
#             'business_company_remain_comission_date': forms.DateInput(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                 'type': 'date'
#             }),
#             'gomrok_remain_payment_date': forms.DateInput(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                 'type': 'date'
#             }),
#         }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        
#         # Style all fields consistently
#         for field_name, field in self.fields.items():
#             if isinstance(field, (forms.DecimalField, forms.IntegerField)):
#                 field.widget.attrs.update({
#                     'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                     'step': '0.01'
#                 })
#             elif isinstance(field, forms.CharField):
#                 field.widget.attrs.update({
#                     'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out'
#                 })
#             elif isinstance(field, forms.ModelChoiceField):
#                 field.widget.attrs.update({
#                     'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out'
#                 })
#             elif isinstance(field, forms.BooleanField):
#                 field.widget.attrs.update({
#                     'class': 'h-4 w-4 text-primary-600 focus:ring-primary-500 border-gray-300 rounded'
#                 })

#         # Add readonly fields for calculated properties
#         self.fields['expeses_up_to_herat'] = forms.DecimalField(
#             required=False,
#             disabled=True,
#             label='میزان مصارف الی هرات',
#             widget=forms.NumberInput(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-gray-100 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#             })
#         )
#         self.fields['all_expeses_to_herat'] = forms.DecimalField(
#             required=False,
#             disabled=True,
#             label='تمام شد الی هرات',
#             widget=forms.NumberInput(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-gray-100 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#             })
#         )

#         # Set initial values for calculated fields if instance exists
#         if self.instance and self.instance.pk:
#             self.initial['expeses_up_to_herat'] = self.instance.expeses_up_to_herat
#             self.initial['all_expeses_to_herat'] = self.instance.all_expeses_to_herat

#     def clean(self):
#         cleaned_data = super().clean()
        
#         # Validate conditional fields
#         has_remain_comission = cleaned_data.get('has_business_company_remain_comission', False)
#         remain_comission = cleaned_data.get('business_company_remain_comission')
#         remain_comission_date = cleaned_data.get('business_company_remain_comission_date')
        
#         if has_remain_comission:
#             if not remain_comission:
#                 self.add_error('business_company_remain_comission', 'مقدار باقی کمیشن شرکت تجارتی باید وارد شود')
#             if not remain_comission_date:
#                 self.add_error('business_company_remain_comission_date', 'تاریخ باقی کمیشن شرکت تجارتی باید وارد شود')
        
#         has_gomrok_remain = cleaned_data.get('has_gomrok_remain_payment', False)
#         gomrok_remain = cleaned_data.get('gomrok_remain_payment')
#         gomrok_remain_date = cleaned_data.get('gomrok_remain_payment_date')
        
#         if has_gomrok_remain:
#             if not gomrok_remain:
#                 self.add_error('gomrok_remain_payment', 'مقدار باقی محصول گمرکی باید وارد شود')
#             if not gomrok_remain_date:
#                 self.add_error('gomrok_remain_payment_date', 'تاریخ باقی محصول گمرکی باید وارد شود')
        
#         return cleaned_data









class WorldExpensesForm(forms.ModelForm):
    class Meta:
        model = WorldExpenses
        fields = '__all__'
        widgets = {
            'herat_arrival_date': forms.DateInput(attrs={'type': 'date'}),
            'business_company_comission_date': forms.DateInput(attrs={'type': 'date'}),
            'business_company_remain_comission_date': forms.DateInput(attrs={'type': 'date'}),
            'gomrok_payment_date': forms.DateInput(attrs={'type': 'date'}),
            'gomrok_remain_payment_date': forms.DateInput(attrs={'type': 'date'}),
            'shipiping_price_to_islam_qala_date': forms.DateInput(attrs={'type': 'date'}),
            'paid_value_for_shipping_date': forms.DateInput(attrs={'type': 'date'}),
            'return_date_from_dubai': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        
        # Validate remain comission fields
        has_remain_comission = cleaned_data.get('has_business_company_remain_comission')
        remain_comission = cleaned_data.get('business_company_remain_comission')
        remain_comission_date = cleaned_data.get('business_company_remain_comission_date')
        
        if has_remain_comission and (not remain_comission or not remain_comission_date):
            if not remain_comission:
                self.add_error('business_company_remain_comission', 'مقدار باقی کمیشن شرکت تجارتی باید وارد شود')
            if not remain_comission_date:
                self.add_error('business_company_remain_comission_date', 'تاریخ باقی کمیشن شرکت تجارتی باید وارد شود')
        
        # Validate remain gomrok fields
        has_remain_gomrok = cleaned_data.get('has_gomrok_remain_payment')
        remain_gomrok = cleaned_data.get('gomrok_remain_payment')
        remain_gomrok_date = cleaned_data.get('gomrok_remain_payment_date')
        
        if has_remain_gomrok and (not remain_gomrok or not remain_gomrok_date):
            if not remain_gomrok:
                self.add_error('gomrok_remain_payment', 'مقدار باقی محصول گمرکی باید وارد شود')
            if not remain_gomrok_date:
                self.add_error('gomrok_remain_payment_date', 'تاریخ باقی محصول گمرکی باید وارد شود')
        
        return cleaned_data
























# class KabulExpensesForm(forms.ModelForm):
#     class Meta:
#         model = KabulExpenses
#         fields = '__all__'
#         widgets = {
#             'car': Select2Widget(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                 'data-placeholder': 'موتر را انتخاب کنید'
#             }),
#             'arrival_date_kabul': forms.DateInput(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                 'type': 'date'
#             }),
#             'remaining_price_from_herat_to_kabul_date': forms.DateInput(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                 'type': 'date'
#             }),
#         }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        
#         # Style all fields consistently
#         for field_name, field in self.fields.items():
#             if isinstance(field, (forms.DecimalField, forms.IntegerField)):
#                 field.widget.attrs.update({
#                     'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                     'step': '0.01'
#                 })
#             elif isinstance(field, forms.CharField):
#                 field.widget.attrs.update({
#                     'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out'
#                 })
#             elif isinstance(field, forms.ModelChoiceField):
#                 field.widget.attrs.update({
#                     'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out'
#                 })
#             elif isinstance(field, forms.BooleanField):
#                 field.widget.attrs.update({
#                     'class': 'h-4 w-4 text-primary-600 focus:ring-primary-500 border-gray-300 rounded'
#                 })

#         # Add readonly field for calculated property
#         self.fields['total_cost_in_kabul'] = forms.DecimalField(
#             required=False,
#             disabled=True,
#             label='قیمت تمام شد در کابل',
#             widget=forms.NumberInput(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-gray-100 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#             })
#         )

#         # Set initial value for has_remaining_price_from_herat_to_kabul
#         if self.instance and self.instance.pk:
#             self.fields['has_remaining_price_from_herat_to_kabul'].initial = bool(
#                 self.instance.remaining_price_from_herat_to_kabul
#             )

#     def clean(self):
#         cleaned_data = super().clean()
        
#         # Validate remaining price fields
#         has_remaining = cleaned_data.get('has_remaining_price_from_herat_to_kabul')
#         remaining_amount = cleaned_data.get('remaining_price_from_herat_to_kabul')
#         remaining_date = cleaned_data.get('remaining_price_from_herat_to_kabul_date')
        
#         if has_remaining:
#             if not remaining_amount or remaining_amount <= 0:
#                 self.add_error(
#                     'remaining_price_from_herat_to_kabul',
#                     'مقدار باقی کرایه باید بیشتر از صفر باشد'
#                 )
#             if not remaining_date:
#                 self.add_error(
#                     'remaining_price_from_herat_to_kabul_date',
#                     'تاریخ باقی کرایه باید مشخص شود'
#                 )
        
#         return cleaned_data




class KabulExpensesForm(forms.ModelForm):
    class Meta:
        model = KabulExpenses
        fields = '__all__'
        widgets = {
            'arrival_date_kabul': forms.DateInput(attrs={'type': 'date'}),
            'herat_to_kabul_cost_date': forms.DateInput(attrs={'type': 'date'}),
            'remaining_price_from_herat_to_kabul_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        
        # Validate remaining price fields
        has_remaining = cleaned_data.get('has_remaining_price_from_herat_to_kabul')
        remaining_price = cleaned_data.get('remaining_price_from_herat_to_kabul')
        remaining_date = cleaned_data.get('remaining_price_from_herat_to_kabul_date')
        
        if has_remaining and (not remaining_price or not remaining_date):
            if not remaining_price:
                self.add_error('remaining_price_from_herat_to_kabul', 'مقدار باقی کرایه باید وارد شود')
            if not remaining_date:
                self.add_error('remaining_price_from_herat_to_kabul_date', 'تاریخ باقی کرایه باید وارد شود')
        
        return cleaned_data




        



class RepairAndOtherExpensesForm(forms.ModelForm):
    class Meta:
        model = RepairAndOtherExpenses
        fields = '__all__'
        widgets = {
            'car': Select2Widget(attrs={
                'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
                'data-placeholder': 'موتر را انتخاب کنید'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Style all fields consistently
        for field_name, field in self.fields.items():
            if isinstance(field, forms.DecimalField):
                field.widget.attrs.update({
                    'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
                    'step': '0.01'
                })
            elif isinstance(field, forms.CharField):
                field.widget.attrs.update({
                    'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out'
                })
            elif isinstance(field, forms.ModelChoiceField):
                field.widget.attrs.update({
                    'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out'
                })

        # Add readonly field for calculated property
        self.fields['final_cost'] = forms.DecimalField(
            required=False,
            disabled=True,
            label='تمام شد نهایی',
            widget=forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 text-gray-700 bg-gray-100 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
            })
        )

    def clean(self):
        cleaned_data = super().clean()
        # You can add custom validation here if needed
        return cleaned_data


        












        



# class SaleInfoForm(forms.ModelForm):
#     class Meta:
#         model = SaleInfo
#         fields = '__all__'
#         widgets = {
#             'car': Select2Widget(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                 'data-placeholder': _('موتر را انتخاب کنید')
#             }),
#             'status': forms.Select(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out'
#             }),
#             'split_50_50': forms.TextInput(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out'
#             }),
#             'buyer_remain_payment_date': forms.DateInput(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                 'type': 'date'
#             }),
#             'sale_date': forms.DateInput(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                 'type': 'date'
#             }),
#             'buyer_info': forms.Textarea(attrs={
#                 'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                 'rows': 3
#             }),
#         }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        
#         # If we have a car in initial data, make the field readonly
#         if 'car' in self.initial:
#             self.fields['car'].disabled = True
#             self.fields['car'].widget.attrs['readonly'] = True
        
#         # Style all decimal fields consistently
#         for field_name, field in self.fields.items():
#             if isinstance(field, forms.DecimalField):
#                 field.widget.attrs.update({
#                     'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out',
#                     'step': '0.01'
#                 })
#             elif isinstance(field, forms.CharField) and not isinstance(field.widget, (forms.Select, forms.Textarea)):
#                 field.widget.attrs.update({
#                     'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out'
#                 })

#         # Add readonly fields for calculated properties
#         calculated_fields = [
#             ('sale_commission', _('کمیشن فروش')),
#             ('special_sale_price', _('قیمت خالص فروش')),
#             ('final_cost', _('قیمت تمام شده')),
#             ('benefit', _('سود خالص')),
#             ('benefit_person_1', _('سود شخص اول')),
#             ('benefit_person_2', _('سود شخص دوم')),
#             ('capital_bound', _('سرمایه بسته شده')),
#         ]
        
#         for field_name, label in calculated_fields:
#             self.fields[field_name] = forms.DecimalField(
#                 required=False,
#                 disabled=True,
#                 label=label,
#                 initial=getattr(self.instance, field_name, Decimal('0')),
#                 widget=forms.NumberInput(attrs={
#                     'class': 'w-full px-3 py-2 text-gray-700 bg-gray-100 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition duration-150 ease-in-out'
#                 })
#             )

#     def clean(self):
#         cleaned_data = super().clean()
#         if not cleaned_data.get('car'):
#             raise forms.ValidationError(_("انتخاب موتر الزامی است"))
        
#         # Auto-calculate fields when sale_price changes
#         sale_price = cleaned_data.get('sale_price', Decimal('0'))
#         cleaned_data['sale_commission'] = (sale_price * Decimal('0.02')) + Decimal('100')
#         cleaned_data['special_sale_price'] = sale_price - cleaned_data['sale_commission']
        
#         return cleaned_data
    








# class SaleInfoForm(forms.ModelForm):
#     # Add these as readonly fields that will be calculated
#     sale_commission = forms.DecimalField(required=False, label="کمیسیون فروش")
#     special_sale_price = forms.DecimalField(required=False, label="قیمت ویژه فروش")
#     benefit = forms.DecimalField(required=False, label="سود")
#     benefit_person_1 = forms.DecimalField(required=False, label="سود شخص اول")
#     benefit_person_2 = forms.DecimalField(required=False, label="سود شخص دوم")
#     capital_bound = forms.DecimalField(required=False, label="سرمایه بسته")

#     class Meta:
#         model = SaleInfo
#         fields = [
#             'car',
#             'status',
#             'split_50_50',
#             'buyer_remain_payment_date',
#             'remaining_price_of_buyer',
#             'buyer_info',
#             'sale_date',
#             'sale_price',
#             'sale_price_currency',
#             'sale_commission',
#             'special_sale_price',
#             'benefit',
#             'benefit_person_1',
#             'benefit_person_2',
#             'capital_bound',
#         ]
#         widgets = {
#             'buyer_remain_payment_date': forms.DateInput(attrs={'type': 'date'}),
#             'sale_date': forms.DateInput(attrs={'type': 'date'}),
#             'buyer_info': forms.Textarea(attrs={'rows': 3}),
#         }

#     def clean(self):
#         cleaned_data = super().clean()
#         status = cleaned_data.get('status')
#         sale_price = cleaned_data.get('sale_price')
#         sale_date = cleaned_data.get('sale_date')

#         if status == SaleInfo.STATUS_SOLD:
#             if not sale_price:
#                 raise forms.ValidationError("برای خودروهای فروخته شده باید قیمت فروش مشخص شود")
#             if sale_price <= 0:
#                 raise forms.ValidationError("قیمت فروش باید بیشتر از صفر باشد")
#             if not sale_date:
#                 raise forms.ValidationError("برای خودروهای فروخته شده باید تاریخ فروش مشخص شود")
        
#         return cleaned_data




# class SaleInfoForm(forms.ModelForm):
#     # Add these as readonly fields that will be calculated
#     sale_commission = forms.DecimalField(
#         required=False,
#         label="کمیسیون فروش",
#         widget=forms.TextInput(attrs={'readonly': 'readonly'})
#     )
#     special_sale_price = forms.DecimalField(
#         required=False,
#         label="قیمت ویژه فروش",
#         widget=forms.TextInput(attrs={'readonly': 'readonly'})
#     )
#     benefit = forms.DecimalField(
#         required=False,
#         label="سود",
#         widget=forms.TextInput(attrs={'readonly': 'readonly'})
#     )
#     benefit_person_1 = forms.DecimalField(
#         required=False,
#         label="سود شخص اول",
#         widget=forms.TextInput(attrs={'readonly': 'readonly'})
#     )
#     benefit_person_2 = forms.DecimalField(
#         required=False,
#         label="سود شخص دوم",
#         widget=forms.TextInput(attrs={'readonly': 'readonly'})
#     )
#     capital_bound = forms.DecimalField(
#         required=False,
#         label="سرمایه بسته",
#         widget=forms.TextInput(attrs={'readonly': 'readonly'})
#     )

#     class Meta:
#         model = SaleInfo
#         fields = [
#             'car',
#             'status',
#             'split_50_50',
#             'buyer_remain_payment_date',
#             'remaining_price_of_buyer',
#             'buyer_info',
#             'sale_date',
#             'sale_price',
#             'sale_price_currency',
#             'sale_commission',
#             'special_sale_price',
#             'benefit',
#             'benefit_person_1',
#             'benefit_person_2',
#             'capital_bound',
#         ]
#         widgets = {
#             'buyer_remain_payment_date': forms.DateInput(attrs={'type': 'date'}),
#             'sale_date': forms.DateInput(attrs={'type': 'date'}),
#             'buyer_info': forms.Textarea(attrs={'rows': 3}),
#         }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Set initial currency if not set
#         if not self.instance.pk and 'sale_price_currency' not in self.initial:
#             self.initial['sale_price_currency'] = get_usd_currency()

#     def clean(self):
#         cleaned_data = super().clean()
#         status = cleaned_data.get('status')
#         sale_price = cleaned_data.get('sale_price')
#         sale_date = cleaned_data.get('sale_date')

#         if status == SaleInfo.STATUS_SOLD:
#             if not sale_price:
#                 raise forms.ValidationError("برای خودروهای فروخته شده باید قیمت فروش مشخص شود")
#             if sale_price <= 0:
#                 raise forms.ValidationError("قیمت فروش باید بیشتر از صفر باشد")
#             if not sale_date:
#                 raise forms.ValidationError("برای خودروهای فروخته شده باید تاریخ فروش مشخص شود")
        
#         return cleaned_data








class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['name', 'contact_info', 'address', 'national_id', 'additional_info']
        widgets = {
            'contact_info': forms.Textarea(attrs={'rows': 3}),
            'address': forms.Textarea(attrs={'rows': 3}),
            'additional_info': forms.Textarea(attrs={'rows': 3}),
        }












# forms.py
class SaleInfoForm(forms.ModelForm):
    class Meta:
        model = SaleInfo
        fields = '__all__'  # or explicitly list all fields including 'car'

        
        widgets = {
            'buyer_remain_payment_date': forms.DateInput(attrs={'type': 'date'}),
            'sale_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'status': _('حالت'),
            'split_50_50': _('مقدار 50/50'),
            'buyer_remain_payment_date': _('تاریخ پرداخت باقیمانده خریدار'),
            'remaining_price_of_buyer': _('باقیمانده قیمت خریدار'),
            'buyer': _('خریدار'),
            'sale_date': _('تاریخ فروش'),
            'sale_price': _('قیمت فروش'),
            'sale_price_currency': _('واحد پول قیمت فروش'),
}

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get('status')
        sale_price = cleaned_data.get('sale_price')
        sale_date = cleaned_data.get('sale_date')
        buyer = cleaned_data.get('buyer')

        if status == SaleInfo.STATUS_SOLD:
            if not sale_price:
                self.add_error('sale_price', ValidationError(_("Sale price must be set for sold cars")))
            if sale_price and sale_price <= 0:
                self.add_error('sale_price', ValidationError(_("Sale price must be positive for sold cars")))
            if not sale_date:
                self.add_error('sale_date', ValidationError(_("Sale date must be set for sold cars")))
            if not buyer:
                self.add_error('buyer', ValidationError(_("Buyer must be specified for sold cars")))

        return cleaned_data












class CarImagesForm(forms.ModelForm):
    class Meta:
        model = CarImages
        fields = ['car', 'image', 'description']
        widgets = {
            'car': Select2Widget(attrs={
                'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500',
                'data-placeholder': 'موتر را انتخاب کنید'
            }),
            'description': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500'
            }),
            'image': forms.FileInput(attrs={
                'class': 'sr-only',
                'accept': 'image/*'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = True
        self.fields['image'].widget.attrs.update({
            'id': 'id_image'
        })

class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = ['code', 'name', 'symbol', 'exchange_rate', 'is_base', 'is_active']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-input'}),
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'symbol': forms.TextInput(attrs={'class': 'form-input'}),
            'exchange_rate': forms.NumberInput(attrs={'class': 'form-input'}),
            'is_base': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }








class DashboardSettingForm(forms.ModelForm):
    class Meta:
        model = DashboardSetting
        fields = ['site_name', 'logo', 'address', 'email', 'phone_number', 'base_currency']
        widgets = {
            'site_name': forms.TextInput(attrs={'class': 'form-input'}),
            'address': forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-input'}),
            'base_currency': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'site_name': _('Site Name'),
            'logo': _('Logo'),
            'address': _('Address'),
            'email': _('Email'),
            'phone_number': _('Phone Number'),
            'base_currency': _('Base Currency'),
        }
        help_texts = {
            'logo': _('Site logo (preferably with transparent background)'),
            'address': _('Full address'),
            'email': _('Contact email'),
            'phone_number': _('Contact phone number'),
            'base_currency': _('The base currency used for all calculations'),
        }






class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['name', 'contact_info', 'address', 'national_id', 'additional_info']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_info': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'national_id': forms.TextInput(attrs={'class': 'form-control'}),
            'additional_info': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }