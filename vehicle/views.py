from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import PurchaseInfo
from .forms import PurchaseInfoForm
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView

from django.http import JsonResponse

from django.db.models import Count, Sum, Avg, F, ExpressionWrapper, DecimalField
from django.contrib.humanize.templatetags.humanize import intcomma
from decimal import Decimal

from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

class LoginView(auth_views.LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    next_page = 'dashboard'

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')

# Related CRUD Views
class RelatedListView(LoginRequiredMixin, ListView):
    model = Related
    template_name = 'settings/related_list.html'
    context_object_name = 'relateds'
    login_url = 'login'

@login_required(login_url='login')
def related_create(request):
    if request.method == 'POST':
        form = RelatedForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'مربوطیت با موفقیت ایجاد شد.')
            return redirect('related-list')
    else:
        form = RelatedForm()
    return render(request, 'settings/related_form.html', {'form': form})

@login_required(login_url='login')
def related_update(request, pk):
    related = get_object_or_404(Related, pk=pk)
    if request.method == 'POST':
        form = RelatedForm(request.POST, instance=related)
        if form.is_valid():
            form.save()
            messages.success(request, 'مربوطیت با موفقیت آپدیت شد.')
            return redirect('related-list')
    else:
        form = RelatedForm(instance=related)
    return render(request, 'settings/related_form.html', {'form': form})

@login_required(login_url='login')
def related_delete(request, pk):
    related = get_object_or_404(Related, pk=pk)
    if request.method == 'POST':
        related.delete()
        messages.success(request, 'مربوطیت با موفقیت حذف شد.')
        return redirect('related-list')
    return render(request, 'settings/related_confirm_delete.html', {'object': related})

# CarMark CRUD Views
class CarMarkListView(LoginRequiredMixin, ListView):
    model = CarMark
    template_name = 'settings/carmark_list.html'
    context_object_name = 'carmarks'
    login_url = 'login'

@login_required(login_url='login')
def carmark_create(request):
    if request.method == 'POST':
        form = CarMarkForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'مارک موتر با موفقیت ایجاد شد.')
            return redirect('carmark-list')
    else:
        form = CarMarkForm()
    return render(request, 'settings/carmark_form.html', {'form': form})

@login_required(login_url='login')
def carmark_update(request, pk):
    carmark = get_object_or_404(CarMark, pk=pk)
    if request.method == 'POST':
        form = CarMarkForm(request.POST, instance=carmark)
        if form.is_valid():
            form.save()
            messages.success(request, 'مارک موتر با موفقیت آپدیت شد.')
            return redirect('carmark-list')
    else:
        form = CarMarkForm(instance=carmark)
    return render(request, 'settings/carmark_form.html', {'form': form})

@login_required(login_url='login')
def carmark_delete(request, pk):
    carmark = get_object_or_404(CarMark, pk=pk)
    if request.method == 'POST':
        carmark.delete()
        messages.success(request, 'مارک موتر با موفقیت حذف شد.')
        return redirect('carmark-list')
    return render(request, 'settings/carmark_confirm_delete.html', {'object': carmark})

# CarType CRUD Views
class CarTypeListView(LoginRequiredMixin, ListView):
    model = CarType
    template_name = 'settings/cartype_list.html'
    context_object_name = 'cartypes'
    login_url = 'login'

@login_required(login_url='login')
def cartype_create(request):
    if request.method == 'POST':
        form = CarTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'نوع موتر با موفقیت ایجاد شد.')
            return redirect('cartype-list')
    else:
        form = CarTypeForm()
    return render(request, 'settings/cartype_form.html', {'form': form})

@login_required(login_url='login')
def cartype_update(request, pk):
    cartype = get_object_or_404(CarType, pk=pk)
    if request.method == 'POST':
        form = CarTypeForm(request.POST, instance=cartype)
        if form.is_valid():
            form.save()
            messages.success(request, 'نوع موتر با موفقیت آپدیت شد.')
            return redirect('cartype-list')
    else:
        form = CarTypeForm(instance=cartype)
    return render(request, 'settings/cartype_form.html', {'form': form})

@login_required(login_url='login')
def cartype_delete(request, pk):
    cartype = get_object_or_404(CarType, pk=pk)
    if request.method == 'POST':
        cartype.delete()
        messages.success(request, 'نوع موتر با موفقیت حذف شد.')
        return redirect('cartype-list')
    return render(request, 'settings/cartype_confirm_delete.html', {'object': cartype})

# ModelYear CRUD Views
class ModelYearListView(LoginRequiredMixin, ListView):
    model = ModelYear
    template_name = 'settings/modelyear_list.html'
    context_object_name = 'modelyears'
    login_url = 'login'

@login_required(login_url='login')
def modelyear_create(request):
    if request.method == 'POST':
        form = ModelYearForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'سال مدل با موفقیت ایجاد شد.')
            return redirect('modelyear-list')
    else:
        form = ModelYearForm()
    return render(request, 'settings/modelyear_form.html', {'form': form})

@login_required(login_url='login')
def modelyear_update(request, pk):
    modelyear = get_object_or_404(ModelYear, pk=pk)
    if request.method == 'POST':
        form = ModelYearForm(request.POST, instance=modelyear)
        if form.is_valid():
            form.save()
            messages.success(request, 'سال مدل با موفقیت آپدیت شد.')
            return redirect('modelyear-list')
    else:
        form = ModelYearForm(instance=modelyear)
    return render(request, 'settings/modelyear_form.html', {'form': form})

@login_required(login_url='login')
def modelyear_delete(request, pk):
    modelyear = get_object_or_404(ModelYear, pk=pk)
    if request.method == 'POST':
        modelyear.delete()
        messages.success(request, 'سال مدل با موفقیت حذف شد.')
        return redirect('modelyear-list')
    return render(request, 'settings/modelyear_confirm_delete.html', {'object': modelyear})

# CarColor CRUD Views
class CarColorListView(LoginRequiredMixin, ListView):
    model = CarColor
    template_name = 'settings/carcolor_list.html'
    context_object_name = 'carcolors'
    login_url = 'login'

@login_required(login_url='login')
def carcolor_create(request):
    if request.method == 'POST':
        form = CarColorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'رنگ موتر با موفقیت ایجاد شد.')
            return redirect('carcolor-list')
    else:
        form = CarColorForm()
    return render(request, 'settings/carcolor_form.html', {'form': form})

@login_required(login_url='login')
def carcolor_update(request, pk):
    carcolor = get_object_or_404(CarColor, pk=pk)
    if request.method == 'POST':
        form = CarColorForm(request.POST, instance=carcolor)
        if form.is_valid():
            form.save()
            messages.success(request, 'رنگ موتر با موفقیت آپدیت شد.')
            return redirect('carcolor-list')
    else:
        form = CarColorForm(instance=carcolor)
    return render(request, 'settings/carcolor_form.html', {'form': form})

@login_required(login_url='login')
def carcolor_delete(request, pk):
    carcolor = get_object_or_404(CarColor, pk=pk)
    if request.method == 'POST':
        carcolor.delete()
        messages.success(request, 'رنگ موتر با موفقیت حذف شد.')
        return redirect('carcolor-list')
    return render(request, 'settings/carcolor_confirm_delete.html', {'object': carcolor})

# CarAction CRUD Views
class CarActionListView(LoginRequiredMixin, ListView):
    model = CarAction
    template_name = 'settings/caraction_list.html'
    context_object_name = 'caractions'
    login_url = 'login'

@login_required(login_url='login')
def caraction_create(request):
    if request.method == 'POST':
        form = CarActionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'آیشن با موفقیت ایجاد شد.')
            return redirect('caraction-list')
    else:
        form = CarActionForm()
    return render(request, 'settings/caraction_form.html', {'form': form})

@login_required(login_url='login')
def caraction_update(request, pk):
    caraction = get_object_or_404(CarAction, pk=pk)
    if request.method == 'POST':
        form = CarActionForm(request.POST, instance=caraction)
        if form.is_valid():
            form.save()
            messages.success(request, 'آیشن با موفقیت آپدیت شد.')
            return redirect('caraction-list')
    else:
        form = CarActionForm(instance=caraction)
    return render(request, 'settings/caraction_form.html', {'form': form})

@login_required(login_url='login')
def caraction_delete(request, pk):
    caraction = get_object_or_404(CarAction, pk=pk)
    if request.method == 'POST':
        caraction.delete()
        messages.success(request, 'آیشن با موفقیت حذف شد.')
        return redirect('caraction-list')
    return render(request, 'settings/caraction_confirm_delete.html', {'object': caraction})

class CarInfoListView(LoginRequiredMixin, ListView):
    model = CarInfo
    template_name = 'carinfo/carinfo_list.html'
    context_object_name = 'cars'
    paginate_by = 20
    login_url = 'login'

@login_required(login_url='login')
def carinfo_create(request):
    if request.method == 'POST':
        form = CarInfoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'معلومات جنس با موفقیت ایجاد شد.')
            return redirect('carinfo-list')
    else:
        form = CarInfoForm()
    return render(request, 'carinfo/carinfo_form.html', {'form': form})

@login_required(login_url='login')
def carinfo_update(request, pk):
    car = get_object_or_404(CarInfo, pk=pk)
    if request.method == 'POST':
        form = CarInfoForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            messages.success(request, 'معلومات جنس با موفقیت آپدیت شد.')
            return redirect('carinfo-list')
    else:
        form = CarInfoForm(instance=car)
    return render(request, 'carinfo/carinfo_form.html', {'form': form})

@login_required(login_url='login')
def carinfo_delete(request, pk):
    car = get_object_or_404(CarInfo, pk=pk)
    if request.method == 'POST':
        car.delete()
        messages.success(request, 'معلومات جنس با موفقیت حذف شد.')
        return redirect('carinfo-list')
    return render(request, 'carinfo/carinfo_confirm_delete.html', {'object': car})

class PurchaseInfoListView(LoginRequiredMixin, ListView):
    model = PurchaseInfo
    template_name = 'purchaseinfo/purchaseinfo_list.html'
    context_object_name = 'purchases'
    ordering = ['-buy_date']
    login_url = 'login'

class PurchaseInfoCreateView(LoginRequiredMixin, CreateView):
    model = PurchaseInfo
    form_class = PurchaseInfoForm
    template_name = 'purchaseinfo/purchaseinfo_form.html'
    success_url = reverse_lazy('purchaseinfo-list')
    login_url = 'login'

    def get_initial(self):
        initial = super().get_initial()
        car_id = self.request.GET.get('car')
        if car_id:
            initial['car'] = car_id
        return initial

class PurchaseInfoUpdateView(LoginRequiredMixin, UpdateView):
    model = PurchaseInfo
    form_class = PurchaseInfoForm
    template_name = 'purchaseinfo/purchaseinfo_form.html'
    success_url = reverse_lazy('purchaseinfo-list')
    login_url = 'login'

class PurchaseInfoDeleteView(LoginRequiredMixin, DeleteView):
    model = PurchaseInfo
    template_name = 'purchaseinfo/purchaseinfo_confirm_delete.html'
    success_url = reverse_lazy('purchaseinfo-list')
    login_url = 'login'








# class ShippingInfoListView(LoginRequiredMixin, ListView):
#     model = ShippingInfo
#     template_name = 'shippinginfo/shippinginfo_list.html'
#     context_object_name = 'shippings'
#     ordering = ['-date_arrived_in_dubai']
#     login_url = 'login'



# class ShippingInfoCreateView(LoginRequiredMixin, CreateView):
#     model = ShippingInfo
#     form_class = ShippingInfoForm
#     template_name = 'shippinginfo/shippinginfo_form.html'
#     success_url = reverse_lazy('shippinginfo-list')
#     login_url = 'login'
    
#     def form_valid(self, form):
#         instance = form.save(commit=False)
        
#         # Set USD currency for total price
#         usd_currency = Currency.objects.get(code='USD')
#         instance.total_price_to_dubai_currency = usd_currency
        
#         # Calculate total price
#         if instance.car and hasattr(instance.car, 'purchase_info'):
#             instance.total_price_to_dubai = instance.computed_total_price_to_dubai
#         else:
#             instance.total_price_to_dubai = instance.mizan_masaref_up_to_dubai
        
#         instance.save()
#         messages.success(self.request, "اطلاعات حمل و نقل با موفقیت ایجاد شد")
#         return super().form_valid(form)
    
#     def get_initial(self):
#         initial = super().get_initial()
#         car_id = self.request.GET.get('car')
#         if car_id:
#             initial['car'] = car_id
            
#             # Set default USD currency for all currency fields if car is specified
#             try:
#                 usd_currency = Currency.objects.get(code='USD')
#                 currency_fields = [f for f in self.form_class().fields if f.endswith('_currency')]
#                 for field in currency_fields:
#                     initial[field] = usd_currency
#             except Currency.DoesNotExist:
#                 pass
                
#         return initial

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['is_create'] = True
#         return context


# class ShippingInfoUpdateView(LoginRequiredMixin, UpdateView):
#     model = ShippingInfo
#     form_class = ShippingInfoForm
#     template_name = 'shippinginfo/shippinginfo_form.html'
#     success_url = reverse_lazy('shippinginfo-list')
#     login_url = 'login'
    
#     def form_valid(self, form):
#         # Update total_price_to_dubai with computed value before saving
#         instance = form.save(commit=False)
#         if instance.car and hasattr(instance.car, 'purchase_info'):
#             instance.total_price_to_dubai = instance.computed_total_price_to_dubai
#         else:
#             instance.total_price_to_dubai = instance.mizan_masaref_up_to_dubai
        
#         instance.save()
#         form.save_m2m()  # in case there are many-to-many fields
        
#         messages.success(self.request, "اطلاعات حمل و نقل با موفقیت آپدیت شد")
#         return super().form_valid(form)
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['is_create'] = False
        
#         # Add calculated properties to context for display
#         obj = self.get_object()
#         context.update({
#             'computed_total_price': obj.computed_total_price_to_dubai,
#             'mizan_invoice_dubai': obj.mizan_invoice_dubai,
#             'dubai_remain_invoice': obj.dubai_remain_invoice,
#             'mizan_masaref_up_to_dubai': obj.mizan_masaref_up_to_dubai,
#         })
#         return context

# class ShippingInfoDeleteView(LoginRequiredMixin, DeleteView):
#     model = ShippingInfo
#     template_name = 'shippinginfo/shippinginfo_confirm_delete.html'
#     success_url = reverse_lazy('shippinginfo-list')
#     login_url = 'login'
    
#     def form_valid(self, form):
#         messages.success(self.request, "اطلاعات حمل و نقل با موفقیت حذف شد")
#         return super().form_valid(form)
    
# class ShippingInfoDetailView(LoginRequiredMixin, DetailView):
#     model = ShippingInfo
#     template_name = 'shippinginfo/shippinginfo_detail.html'
#     context_object_name = 'shipping'
#     login_url = 'login'













class ShippingInfoListView(ListView):
    model = ShippingInfo
    template_name = 'shippinginfo/shippinginfo_list.html'  # make sure this matches your template path
    context_object_name = 'shippings'  # this should match your template variable
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.select_related(
            'car',
            'shipping_currency',
            'towing_currency',
            'red_sea_currency',
            'd_o_currency',
            'duty_vat_currency',
            'clearing_currency',
            'commission_currency',
            'attstion_currency',
            'port_clips_prmi_currency',
            'dubai_paid_invoice_currency',
            'cash_paid_comission_currency'
        ).order_by('-date_arrived_in_dubai')

class ShippingInfoDetailView(DetailView):
    model = ShippingInfo
    template_name = 'shippinginfo/shippinginfo_detail.html'
    context_object_name = 'shipping_info'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context data here
        return context
    

    
class ShippingInfoCreateView(CreateView):
    model = ShippingInfo
    form_class = ShippingInfoForm
    template_name = 'shippinginfo/shippinginfo_form.html'
    success_url = reverse_lazy('shippinginfo-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usd_currency'] = Currency.objects.get(code='USD')  # or your get_usd_currency() function
        return context

class ShippingInfoUpdateView(UpdateView):
    model = ShippingInfo
    form_class = ShippingInfoForm
    template_name = 'shippinginfo/shippinginfo_form.html'
    success_url = reverse_lazy('shippinginfo-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usd_currency'] = Currency.objects.get(code='USD')  # or your get_usd_currency() function
        return context

    def form_valid(self, form):
        # Add any pre-save logic here
        return super().form_valid(form)

class ShippingInfoDeleteView(DeleteView):
    model = ShippingInfo
    template_name = 'shippinginfo/shippinginfo_confirm_delete.html'
    success_url = reverse_lazy('shippinginfo-list')
    context_object_name = 'shipping_info'




















# class WorldExpensesListView(LoginRequiredMixin, ListView):
#     model = WorldExpenses
#     template_name = 'world_expenses/list.html'
#     context_object_name = 'world_expenses'
#     paginate_by = 20
#     login_url = 'login'

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.select_related(
#             'car',
#             'shipiping_price_to_islam_qala_currency',
#             'paid_value_for_shipping_currency',
#             'gomrok_payment_currency',
#             'business_company_comission_currency'
#         )

# class WorldExpensesCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
#     model = WorldExpenses
#     form_class = WorldExpensesForm
#     template_name = 'world_expenses/form.html'
#     success_url = reverse_lazy('world_expenses_list')
#     success_message = "مصارف انتقالات با موفقیت اضافه شد"
#     login_url = 'login'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'اضافه کردن مصارف انتقالات جدید'
#         return context

#     def form_valid(self, form):
#         instance = form.save(commit=False)
        
#         # Set default currencies if not selected
#         if not instance.shipiping_price_to_islam_qala_currency:
#             instance.shipiping_price_to_islam_qala_currency = Currency.objects.get(code='USD')
#         if not instance.paid_value_for_shipping_currency:
#             instance.paid_value_for_shipping_currency = Currency.objects.get(code='USD')
#         if not instance.gomrok_payment_currency:
#             instance.gomrok_payment_currency = Currency.objects.get(code='AFN')
#         if not instance.business_company_comission_currency:
#             instance.business_company_comission_currency = Currency.objects.get(code='AFN')
            
#         # Handle conditional fields
#         if not instance.has_business_company_remain_comission:
#             instance.business_company_remain_comission = 0
#             instance.business_company_remain_comission_date = None
            
#         if not instance.has_gomrok_remain_payment:
#             instance.gomrok_remain_payment = 0
#             instance.gomrok_remain_payment_date = None
            
#         instance.save()
#         return super().form_valid(form)

# class WorldExpensesUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
#     model = WorldExpenses
#     form_class = WorldExpensesForm
#     template_name = 'world_expenses/form.html'
#     success_url = reverse_lazy('world_expenses_list')
#     success_message = "مصارف انتقالات با موفقیت ویرایش شد"
#     login_url = 'login'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'ویرایش مصارف انتقالات'
#         return context

#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         instance = kwargs['instance']
#         kwargs['initial'] = {
#             'expeses_up_to_herat': instance.expeses_up_to_herat,
#             'all_expeses_to_herat': instance.all_expeses_to_herat,
#         }
#         return kwargs

#     def form_valid(self, form):
#         instance = form.save(commit=False)
        
#         # Handle conditional fields
#         if not instance.has_business_company_remain_comission:
#             instance.business_company_remain_comission = 0
#             instance.business_company_remain_comission_date = None
            
#         if not instance.has_gomrok_remain_payment:
#             instance.gomrok_remain_payment = 0
#             instance.gomrok_remain_payment_date = None
            
#         instance.save()
#         return super().form_valid(form)

# class WorldExpensesDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
#     model = WorldExpenses
#     template_name = 'world_expenses/confirm_delete.html'
#     success_url = reverse_lazy('world_expenses_list')
#     success_message = "مصارف انتقالات با موفقیت حذف شد"
#     login_url = 'login'

# class WorldExpensesDetailView(LoginRequiredMixin, DetailView):
#     model = WorldExpenses
#     template_name = 'world_expenses/world_expenses_detail.html'
#     context_object_name = 'expense'
#     login_url = 'login'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['calculated_fields'] = {
#             'expeses_up_to_herat': self.object.expeses_up_to_herat,
#             'all_expeses_to_herat': self.object.all_expeses_to_herat,
#             'amount_of_expeses_to_herat': self.object.amount_of_expeses_to_herat,
#         }
#         return context










class WorldExpensesListView(ListView):
    model = WorldExpenses
    template_name = 'world_expenses/list.html'
    context_object_name = 'world_expenses'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        # Add any filtering or ordering here
        return queryset.select_related('car')

class WorldExpensesCreateView(SuccessMessageMixin, CreateView):
    model = WorldExpenses
    form_class = WorldExpensesForm
    template_name = 'world_expenses/form.html'
    success_message = _("World expenses record created successfully")
    success_url = reverse_lazy('world_expenses_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response

class WorldExpensesUpdateView(SuccessMessageMixin, UpdateView):
    model = WorldExpenses
    form_class = WorldExpensesForm
    template_name = 'world_expenses/form.html'
    success_message = _("World expenses record updated successfully")
    success_url = reverse_lazy('world_expenses_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response

class WorldExpensesDeleteView(SuccessMessageMixin, DeleteView):
    model = WorldExpenses
    template_name = 'world_expenses/confirm_delete.html'
    success_message = _("World expenses record deleted successfully")
    success_url = reverse_lazy('world_expenses_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

class WorldExpensesDetailView(DetailView):
    model = WorldExpenses
    template_name = 'world_expenses/detail.html'
    context_object_name = 'world_expense'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context data here
        return context
























# class KabulExpensesListView(LoginRequiredMixin, ListView):
#     model = KabulExpenses
#     template_name = 'kabul_expenses/list.html'
#     context_object_name = 'kabul_expenses'
#     paginate_by = 20
#     login_url = 'login'

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.select_related(
#             'car',
#             'herat_to_kabul_cost_currency',
#             'usa_to_kabul_cost_currency'
#         )

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context

# class KabulExpensesCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
#     model = KabulExpenses
#     form_class = KabulExpensesForm
#     template_name = 'kabul_expenses/form.html'
#     success_url = reverse_lazy('kabul_expenses_list')
#     success_message = "مصارف کابل با موفقیت اضافه شد"
#     login_url = 'login'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'اضافه کردن مصارف کابل جدید'
#         return context

#     def form_valid(self, form):
#         if not form.cleaned_data.get('has_remaining_price_from_herat_to_kabul'):
#             form.instance.remaining_price_from_herat_to_kabul = 0
#             form.instance.remaining_price_from_herat_to_kabul_date = None
#         return super().form_valid(form)

# class KabulExpensesUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
#     model = KabulExpenses
#     form_class = KabulExpensesForm
#     template_name = 'kabul_expenses/form.html'
#     success_url = reverse_lazy('kabul_expenses_list')
#     success_message = "مصارف کابل با موفقیت ویرایش شد"
#     login_url = 'login'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'ویرایش مصارف کابل'
#         return context

#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         instance = kwargs['instance']
#         kwargs['initial'] = {
#             'total_cost_in_kabul': instance.total_cost_in_kabul,
#             'has_remaining_price_from_herat_to_kabul': bool(instance.remaining_price_from_herat_to_kabul),
#         }
#         return kwargs

#     def form_valid(self, form):
#         if not form.cleaned_data.get('has_remaining_price_from_herat_to_kabul'):
#             form.instance.remaining_price_from_herat_to_kabul = 0
#             form.instance.remaining_price_from_herat_to_kabul_date = None
#         return super().form_valid(form)

# class KabulExpensesDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
#     model = KabulExpenses
#     template_name = 'kabul_expenses/confirm_delete.html'
#     success_url = reverse_lazy('kabul_expenses_list')
#     success_message = "مصارف کابل با موفقیت حذف شد"
#     login_url = 'login'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'حذف مصارف کابل'
#         return context








class KabulExpensesListView(ListView):
    model = KabulExpenses
    template_name = 'kabul_expenses/list.html'
    context_object_name = 'expenses'
    paginate_by = 20

    def get_queryset(self):
        return super().get_queryset().select_related('car', 'herat_to_kabul_cost_currency')

class KabulExpensesCreateView(SuccessMessageMixin, CreateView):
    model = KabulExpenses
    form_class = KabulExpensesForm
    template_name = 'kabul_expenses/form.html'
    success_message = "رکورد مصارف کابل با موفقیت ایجاد شد"
    success_url = reverse_lazy('kabul_expenses_list')

class KabulExpensesUpdateView(SuccessMessageMixin, UpdateView):
    model = KabulExpenses
    form_class = KabulExpensesForm
    template_name = 'kabul_expenses/form.html'
    success_message = "رکورد مصارف کابل با موفقیت ویرایش شد"
    success_url = reverse_lazy('kabul_expenses_list')

class KabulExpensesDeleteView(SuccessMessageMixin, DeleteView):
    model = KabulExpenses
    template_name = 'kabul_expenses/confirm_delete.html'
    success_message = "رکورد مصارف کابل با موفقیت حذف شد"
    success_url = reverse_lazy('kabul_expenses_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

class KabulExpensesDetailView(DetailView):
    model = KabulExpenses
    template_name = 'kabul_expenses/detail.html'
    context_object_name = 'expense'









# class RepairAndOtherExpensesListView(LoginRequiredMixin, ListView):
#     model = RepairAndOtherExpenses
#     template_name = 'repair_expenses/list.html'
#     context_object_name = 'repair_expenses'
#     paginate_by = 20
#     login_url = 'login'

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.select_related('car')

# class RepairAndOtherExpensesCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
#     model = RepairAndOtherExpenses
#     form_class = RepairAndOtherExpensesForm
#     template_name = 'repair_expenses/form.html'
#     success_url = reverse_lazy('repair_expenses_list')
#     success_message = "مصارف ترمیم و سایر هزینه ها با موفقیت اضافه شد"
#     login_url = 'login'

#     def get_initial(self):
#         initial = super().get_initial()
#         if 'car_id' in self.kwargs:
#             initial['car'] = self.kwargs['car_id']
#         return initial

#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         if 'car_id' in self.kwargs:
#             kwargs['car'] = get_object_or_404(CarInfo, pk=self.kwargs['car_id'])
#         return kwargs

#     def form_valid(self, form):
#         if 'car_id' in self.kwargs and not form.instance.car_id:
#             form.instance.car = get_object_or_404(CarInfo, pk=self.kwargs['car_id'])
#         return super().form_valid(form)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'اضافه کردن مصارف ترمیم و سایر هزینه ها'
#         if 'car_id' in self.kwargs:
#             context['car'] = get_object_or_404(CarInfo, pk=self.kwargs['car_id'])
#         return context

# class RepairAndOtherExpensesUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
#     model = RepairAndOtherExpenses
#     form_class = RepairAndOtherExpensesForm
#     template_name = 'repair_expenses/form.html'
#     success_url = reverse_lazy('repair_expenses_list')
#     success_message = "مصارف ترمیم و سایر هزینه ها با موفقیت ویرایش شد"
#     login_url = 'login'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'ویرایش مصارف ترمیم و سایر هزینه ها'
#         return context

#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         instance = kwargs['instance']
#         kwargs['initial'] = {
#             'final_cost': instance.final_cost,
#         }
#         return kwargs

# class RepairAndOtherExpensesDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
#     model = RepairAndOtherExpenses
#     template_name = 'repair_expenses/confirm_delete.html'
#     success_url = reverse_lazy('repair_expenses_list')
#     success_message = "مصارف ترمیم و سایر هزینه ها با موفقیت حذف شد"
#     login_url = 'login'










class RepairAndOtherExpensesListView(LoginRequiredMixin, ListView):
    model = RepairAndOtherExpenses
    template_name = 'repair_expenses/list.html'
    context_object_name = 'repair_expenses'
    paginate_by = 20
    login_url = 'login'

    def get_queryset(self):
        queryset = super().get_queryset()
        # Add search functionality
        if 'search' in self.request.GET:
            search_term = self.request.GET['search']
            queryset = queryset.filter(
                models.Q(car__mark__icontains=search_term) |
                models.Q(car__model__icontains=search_term) |
                models.Q(repair_cost__icontains=search_term) |
                models.Q(palate_cost__icontains=search_term)
        )
        return queryset.select_related(
            'car',
            'repair_cost_currency',
            'palate_cost_currency'
        ).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_term'] = self.request.GET.get('search', '')
        return context

class RepairAndOtherExpensesCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = RepairAndOtherExpenses
    form_class = RepairAndOtherExpensesForm
    template_name = 'repair_expenses/form.html'
    success_url = reverse_lazy('repair_expenses_list')
    success_message = "مصارف ترمیم و سایر هزینه ها با موفقیت اضافه شد"
    login_url = 'login'

    def get_initial(self):
        initial = super().get_initial()
        if 'car_id' in self.kwargs:
            initial['car'] = self.kwargs['car_id']
        return initial

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if 'car_id' in self.kwargs:
            kwargs['car'] = get_object_or_404(CarInfo, pk=self.kwargs['car_id'])
        return kwargs

    def form_valid(self, form):
        if 'car_id' in self.kwargs and not form.instance.car_id:
            form.instance.car = get_object_or_404(CarInfo, pk=self.kwargs['car_id'])
        
        # Set default currency if not provided
        if form.instance.repair_cost and not form.instance.repair_cost_currency:
            form.instance.repair_cost_currency = Currency.objects.get_default()
        if form.instance.palate_cost and not form.instance.palate_cost_currency:
            form.instance.palate_cost_currency = Currency.objects.get_default()
            
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'اضافه کردن مصارف ترمیم و سایر هزینه ها'
        if 'car_id' in self.kwargs:
            context['car'] = get_object_or_404(CarInfo, pk=self.kwargs['car_id'])
        context['is_create'] = True
        return context

class RepairAndOtherExpensesUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = RepairAndOtherExpenses
    form_class = RepairAndOtherExpensesForm
    template_name = 'repair_expenses/form.html'
    success_url = reverse_lazy('repair_expenses_list')
    success_message = "مصارف ترمیم و سایر هزینه ها با موفقیت ویرایش شد"
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ویرایش مصارف ترمیم و سایر هزینه ها'
        context['is_create'] = False
        context['final_cost'] = self.object.final_cost
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        instance = kwargs['instance']
        kwargs['initial'] = {
            'final_cost': instance.final_cost,
        }
        return kwargs

    def form_valid(self, form):
        # Set default currency if not provided
        if form.instance.repair_cost and not form.instance.repair_cost_currency:
            form.instance.repair_cost_currency = Currency.objects.get_default()
        if form.instance.palate_cost and not form.instance.palate_cost_currency:
            form.instance.palate_cost_currency = Currency.objects.get_default()
            
        return super().form_valid(form)

class RepairAndOtherExpensesDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = RepairAndOtherExpenses
    template_name = 'repair_expenses/confirm_delete.html'
    success_url = reverse_lazy('repair_expenses_list')
    success_message = "مصارف ترمیم و سایر هزینه ها با موفقیت حذف شد"
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف مصارف ترمیم و سایر هزینه ها'
        return context















# class SaleInfoListView(LoginRequiredMixin, ListView):
#     model = SaleInfo
#     template_name = 'sale_info/list.html'
#     context_object_name = 'sale_infos'
#     paginate_by = 20
#     login_url = 'login'

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.select_related('car')




# class SaleInfoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
#     model = SaleInfo
#     form_class = SaleInfoForm
#     template_name = 'sale_info/form.html'
#     success_url = reverse_lazy('sale_info_list')
#     success_message = _("اطلاعات فروش با موفقیت اضافه شد")
#     login_url = 'login'

#     def get_initial(self):
#         initial = super().get_initial()
#         car_id = self.request.GET.get('car')
#         if car_id:
#             initial['car'] = car_id
#         return initial

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = _('اضافه کردن اطلاعات فروش جدید')
#         car_id = self.request.GET.get('car')
#         if car_id:
#             context['car'] = get_object_or_404(CarInfo, pk=car_id)
#         return context

# class SaleInfoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
#     model = SaleInfo
#     form_class = SaleInfoForm
#     template_name = 'sale_info/form.html'
#     success_url = reverse_lazy('sale_info_list')
#     success_message = _("اطلاعات فروش با موفقیت ویرایش شد")
#     login_url = 'login'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = _('ویرایش اطلاعات فروش')
#         context['car'] = self.object.car
#         return context

# class SaleInfoDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
#     model = SaleInfo
#     template_name = 'sale_info/confirm_delete.html'
#     success_url = reverse_lazy('sale_info_list')
#     success_message = _("اطلاعات فروش با موفقیت حذف شد")
#     login_url = 'login'

# class SaleInfoDetailView(LoginRequiredMixin, DetailView):
#     model = SaleInfo
#     template_name = 'sale_info/sale_info_detail.html'
#     context_object_name = 'object'
#     login_url = 'login'















# class BuyerCreateView(CreateView):
#     model = Buyer
#     form_class = BuyerForm
#     template_name = 'sale_info/buyer_create.html'
#     success_url = reverse_lazy('buyer_create_success')

#     def form_valid(self, form):
#         response = super().form_valid(form)
#         if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
#             return JsonResponse({
#                 'id': self.object.id,
#                 'name': str(self.object),
#                 'success': True
#             })
#         return response

# def buyer_list_json(request):
#     buyers = Buyer.objects.all().order_by('name')
#     data = [{'id': buyer.id, 'name': str(buyer)} for buyer in buyers]
#     return JsonResponse(data, safe=False)

# def buyer_create_success(request):
#     return JsonResponse({'success': True})




from django.template.loader import render_to_string


class BuyerCreateView(CreateView):
    model = Buyer
    form_class = BuyerForm
    template_name = 'sale_info/buyer_create.html'

    def render_to_response(self, context, **kwargs):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            form = self.get_form()
            return JsonResponse({
                'form_html': render_to_string('vehicle/buyer_form_partial.html', {'form': form}, request=self.request)
            })
        return super().render_to_response(context, **kwargs)

    def form_valid(self, form):
        self.object = form.save()
        return JsonResponse({
            'success': True,
            'buyer_id': self.object.id,
            'name': self.object.name,
            'phone': self.object.phone,
            'address': self.object.address,
            'message': 'Buyer created successfully'
        })

    def form_invalid(self, form):
        return JsonResponse({
            'success': False,
            'errors': form.errors.get_json_data(),
            'message': 'Form validation failed'
        }, status=400)


def buyer_list_json(request):
    """Return JSON list of buyers for AJAX requests"""
    buyers = Buyer.objects.all().values('id', 'name', 'phone')
    return JsonResponse(list(buyers), safe=False)


def buyer_create_success(request):
    # You can customize this template name as needed
    return render(request, 'sale_info/buyer_create_success.html')







# @require_POST
# @csrf_exempt
# def buyer_create_ajax(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             buyer = Buyer.objects.create(
#                 name=data.get('name'),
#                 phone=data.get('phone'),
#                 address=data.get('address'),
#                 national_id=data.get('national_id')
#             )
#             return JsonResponse({
#                 'success': True,
#                 'buyer': {
#                     'id': buyer.id,
#                     'name': buyer.name,
#                     'phone': buyer.phone
#                 }
#             })
#         except Exception as e:
#             return JsonResponse({
#                 'success': False,
#                 'error': str(e)
#             }, status=400)
#     return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)


@require_POST
def buyer_create_ajax(request):
    try:
        # Get data from POST request
        name = request.POST.get('name')
        contact_info = request.POST.get('contact_info')
        address = request.POST.get('address')
        national_id = request.POST.get('national_id')
        additional_info = request.POST.get('additional_info', '')

        if not name:
            return JsonResponse({
                'success': False,
                'error': 'نام خریدار الزامی است'
            }, status=400)

        # Create the buyer
        buyer = Buyer.objects.create(
            name=name,
            contact_info=contact_info,
            address=address,
            national_id=national_id,
            additional_info=additional_info
        )

        return JsonResponse({
            'success': True,
            'buyer': {
                'id': buyer.id,
                'name': buyer.name,
                'contact_info': buyer.contact_info
            }
        })

    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)






class SaleInfoListView(ListView):
    model = SaleInfo
    template_name = 'sale_info/list.html'
    context_object_name = 'sale_infos'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset().select_related('car', 'sale_price_currency')
        # Add any filtering logic here if needed
        return queryset
    

    
# class SaleInfoCreateView(CreateView):
#     model = SaleInfo
#     form_class = SaleInfoForm
#     template_name = 'sale_info/form.html'
#     success_url = reverse_lazy('sale_info_list')

#     def get_initial(self):
#         initial = super().get_initial()
#         car_id = self.kwargs.get('car_id')
        
#         if car_id:
#             car = get_object_or_404(CarInfo, pk=car_id)
#             initial['car'] = car
            
#             # Set initial sale price to repair cost if available
#             if hasattr(car, 'repair_expenses'):
#                 initial['sale_price'] = car.repair_expenses.final_cost
        
#         # Set default values for required fields
#         initial['remaining_price_of_buyer'] = 0  # Default value for باقی خریدار
#         return initial

#     def get_form(self, form_class=None):
#         form = super().get_form(form_class)
#         car_id = self.kwargs.get('car_id')
        
#         # Make car field not required since we're setting it via URL
#         form.fields['car'].required = False
        
#         # Make remaining_price_of_buyer not required
#         form.fields['remaining_price_of_buyer'].required = False
        
#         return form

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         car_id = self.kwargs.get('car_id')
        
#         if car_id:
#             car = get_object_or_404(CarInfo, pk=car_id)
#             context['car'] = car
            
#             # Add repair cost to context for JavaScript calculations
#             if hasattr(car, 'repair_expenses'):
#                 context['repair_final_cost'] = car.repair_expenses.final_cost
        
#         context['title'] = 'افزودن اطلاعات فروش جدید'
#         return context

#     def form_valid(self, form):
#         car_id = self.kwargs.get('car_id')
        
#         if car_id:
#             car = get_object_or_404(CarInfo, pk=car_id)
#             form.instance.car = car
            
#             # For non-sold cars, set sale price to repair cost
#             if form.cleaned_data.get('status') != SaleInfo.STATUS_SOLD:
#                 if hasattr(car, 'repair_expenses'):
#                     form.instance.sale_price = car.repair_expenses.final_cost
        
#         # Set default value for remaining_price_of_buyer if not provided
#         if not form.cleaned_data.get('remaining_price_of_buyer'):
#             form.instance.remaining_price_of_buyer = 0
            
#         return super().form_valid(form)


# class SaleInfoUpdateView(UpdateView):
#     model = SaleInfo
#     form_class = SaleInfoForm
#     template_name = 'sale_info/form.html'
#     success_url = reverse_lazy('sale_info_list')

#     def get_form(self, form_class=None):
#         form = super().get_form(form_class)
#         # Make remaining_price_of_buyer not required
#         form.fields['remaining_price_of_buyer'].required = False
#         return form

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'ویرایش اطلاعات فروش'
#         context['car'] = self.object.car
        
#         # Add repair cost to context if available
#         if hasattr(self.object.car, 'repair_expenses'):
#             context['repair_final_cost'] = self.object.car.repair_expenses.final_cost
        
#         return context

#     def form_valid(self, form):
#         # Set default value for remaining_price_of_buyer if not provided
#         if not form.cleaned_data.get('remaining_price_of_buyer'):
#             form.instance.remaining_price_of_buyer = 0
            
#         return super().form_valid(form)





# class SaleInfoDeleteView(DeleteView):
#     model = SaleInfo
#     template_name = 'sale_info/confirm_delete.html'
#     success_url = reverse_lazy('sale_info_list')





# class SaleInfoDetailView(DetailView):
#     model = SaleInfo
#     template_name = 'sale_info/detail.html'
#     context_object_name = 'sale'  # Changed from 'sale_info' to 'sale'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         sale = self.get_object()  # Also changed variable name here for consistency
        
#         # Add calculated properties to context
#         context['repair_final_cost'] = sale.repair_final_cost
#         context['sale_commission'] = sale.sale_commission
#         context['special_sale_price'] = sale.special_sale_price
#         context['benefit'] = sale.benefit
#         context['benefit_person_1'] = sale.benefit_person_1
#         context['benefit_person_2'] = sale.benefit_person_2
#         context['capital_bound'] = sale.capital_bound
        
#         return context

from django.urls import reverse

from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

class SaleInfoCreateView(CreateView):
    model = SaleInfo
    form_class = SaleInfoForm
    template_name = 'sale_info/form.html'
    
    def get_initial(self):
        initial = super().get_initial()
        if 'car_id' in self.kwargs:
            initial['car'] = self.kwargs['car_id']
        return initial
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if 'car_id' in self.kwargs:
            kwargs.update({'initial': {'car': self.kwargs['car_id']}})
        return kwargs
    
    def form_valid(self, form):
        if 'car_id' in self.kwargs:
            form.instance.car_id = self.kwargs['car_id']
        messages.success(self.request, _("Sale information created successfully!"))
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('sale_info_detail', kwargs={'pk': self.object.pk})


class SaleInfoUpdateView(UpdateView):
    model = SaleInfo
    form_class = SaleInfoForm
    template_name = 'sale_info/form.html'
    
    def get_success_url(self):
        return reverse('sale_info_detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _("Sale information updated successfully!"))
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _("Update Sale Information")
        return context

class SaleInfoDetailView(DetailView):
    model = SaleInfo
    template_name = 'sale_info/detail.html'
    context_object_name = 'sale_info'  # This ensures the object is available as 'sale_info' in template
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sale_info = self.object
        
        # Add calculated properties to context
        context.update({
            'repair_final_cost': sale_info.repair_final_cost,
            'sale_commission': sale_info.sale_commission,
            'special_sale_price': sale_info.special_sale_price,
            'benefit': sale_info.benefit,
            'benefit_person_1': sale_info.benefit_person_1,
            'benefit_person_2': sale_info.benefit_person_2,
            'capital_bound': sale_info.capital_bound,
        })
        return context

class SaleInfoDeleteView(DeleteView):
    model = SaleInfo
    template_name = 'shippinginfo/confirm_delete.html'
    success_url = reverse_lazy('car-list')  # Adjust to your needs
    
    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, _("Sale information deleted successfully!"))
        return response






class CarImagesListView(LoginRequiredMixin, ListView):
    model = CarImages
    template_name = 'car_images/list.html'
    context_object_name = 'images'
    paginate_by = 12
    login_url = 'login'

    def get_queryset(self):
        queryset = super().get_queryset()
        car_id = self.request.GET.get('car')
        if car_id:
            queryset = queryset.filter(car_id=car_id)
        return queryset.select_related('car')

class CarImagesCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = CarImages
    form_class = CarImagesForm
    template_name = 'car_images/form.html'
    success_message = "عکس موتر با موفقیت اضافه شد"
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('car_images_list') + f'?car={self.object.car.id}'

    def get_initial(self):
        initial = super().get_initial()
        car_id = self.request.GET.get('car')
        if car_id:
            initial['car'] = car_id
        return initial

class CarImagesUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CarImages
    form_class = CarImagesForm
    template_name = 'car_images/form.html'
    success_message = "عکس موتر با موفقیت ویرایش شد"
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('car_images_list') + f'?car={self.object.car.id}'

class CarImagesDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = CarImages
    template_name = 'car_images/confirm_delete.html'
    success_message = "عکس موتر با موفقیت حذف شد"
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('car_images_list') + f'?car={self.object.car.id}'




@login_required(login_url='login')
def dashboard(request):
    # Basic counts
    cars_count = CarInfo.objects.count()
    sold_cars_count = CarInfo.objects.filter(sale_info__status=SaleInfo.STATUS_SOLD).count()
    ready_cars_count = CarInfo.objects.filter(sale_info__status=SaleInfo.STATUS_READY).count()
    in_transit_cars_count = CarInfo.objects.filter(sale_info__status=SaleInfo.STATUS_IN_TRANSIT).count()
    
    # Percentages
    sold_percentage = round((sold_cars_count / cars_count) * 100, 1) if cars_count > 0 else 0
    ready_percentage = round((ready_cars_count / cars_count) * 100, 1) if cars_count > 0 else 0
    in_transit_percentage = round((in_transit_cars_count / cars_count) * 100, 1) if cars_count > 0 else 0
    
    # Calculate financial data
    total_sales = Decimal('0')
    total_benefit = Decimal('0')
    total_investment = Decimal('0')
    total_expenses = Decimal('0')
    
    # Get all cars with their related data
    cars = CarInfo.objects.select_related(
        'purchase_info', 'shipping_info', 'world_expenses', 
        'kabul_expenses', 'repair_expenses', 'sale_info'
    ).prefetch_related('images').all()
    
    for car in cars:
        # Calculate total sales and benefits from sold cars
        if hasattr(car, 'sale_info') and car.sale_info.status == SaleInfo.STATUS_SOLD:
            sale_info = car.sale_info
            total_sales += sale_info._convert_to_base(
                sale_info.sale_price,
                'sale_price',
                'sale_date'
            )
            total_benefit += sale_info.benefit
        
        # Calculate total investment (purchase + repair)
        if hasattr(car, 'purchase_info'):
            purchase_info = car.purchase_info
            total_investment += purchase_info._convert_to_base(
                purchase_info.purchase_price,
                'purchase_price',
                'buy_date'
            )
        
        # Calculate total expenses (shipping + world + kabul + repair)
        if hasattr(car, 'shipping_info'):
            shipping_info = car.shipping_info
            total_expenses += shipping_info.mizan_masaref_up_to_dubai
        
        if hasattr(car, 'world_expenses'):
            world_exp = car.world_expenses
            total_expenses += world_exp.amount_of_expeses_to_herat
        
        if hasattr(car, 'kabul_expenses'):
            kabul_exp = car.kabul_expenses
            total_expenses += kabul_exp._convert_to_base(
                kabul_exp.herat_to_kabul_cost,
                'herat_to_kabul_cost',
                'herat_to_kabul_cost_date'
            )
        
        if hasattr(car, 'repair_expenses'):
            repair_exp = car.repair_expenses
            repair_in_base = repair_exp._convert_to_base(
                repair_exp.repair_cost,
                'repair_cost',
                'repair_cost_date'
            )
            palate_in_base = repair_exp._convert_to_base(
                repair_exp.palate_cost,
                'palate_cost',
                'palate_cost_date'
            )
            total_expenses += repair_in_base + palate_in_base
    
    # Calculate averages
    avg_benefit = total_benefit / sold_cars_count if sold_cars_count > 0 else Decimal('0')
    
    # Recent cars
    recent_cars = cars.order_by('-id')[:5]
    
    # Top performing cars (sold cars sorted by benefit)
    sold_cars = [car for car in cars if hasattr(car, 'sale_info') and car.sale_info.status == SaleInfo.STATUS_SOLD]
    sold_cars.sort(key=lambda x: x.sale_info.benefit, reverse=True)
    top_performing_cars = sold_cars[:3]
    
    # Get dashboard settings for currency formatting
    dashboard_settings = DashboardSetting.load()
    base_currency = dashboard_settings.base_currency
    
    context = {
        'cars_count': cars_count,
        'sold_cars_count': sold_cars_count,
        'ready_cars_count': ready_cars_count,
        'in_transit_cars_count': in_transit_cars_count,
        'sold_percentage': sold_percentage,
        'ready_percentage': ready_percentage,
        'in_transit_percentage': in_transit_percentage,
        'total_sales': total_sales,
        'total_benefit': total_benefit,
        'avg_benefit': avg_benefit,
        'total_investment': total_investment,
        'total_expenses': total_expenses,
        'recent_cars': recent_cars,
        'top_performing_cars': top_performing_cars,
        'base_currency': base_currency,
    }
    
    return render(request, 'dashboard.html', context)






class SettingsView(LoginRequiredMixin, ListView):
    model = CarImages
    template_name = 'settings/settings.html'
    context_object_name = 'images'
    paginate_by = 12
    login_url = 'login'





class CurrencyListView(LoginRequiredMixin, ListView):
    model = Currency
    template_name = 'currency/currency_list.html'
    context_object_name = 'currencies'
    paginate_by = 10
    login_url = 'login'  # Replace with your login URL name

class CurrencyCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Currency
    form_class = CurrencyForm
    template_name = 'currency/currency_form.html'
    success_url = reverse_lazy('currency-list')
    success_message = "ارز موفقانه ایجاد شد!"
    login_url = 'login'  # Replace with your login URL name

    def form_valid(self, form):
        # Ensure only one base currency exists
        if form.cleaned_data['is_base']:
            Currency.objects.filter(is_base=True).update(is_base=False)
        return super().form_valid(form)

class CurrencyUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Currency
    form_class = CurrencyForm
    template_name = 'currency/currency_form.html'
    success_url = reverse_lazy('currency-list')
    success_message = "ارز موفقانه آپدیت شد!"
    login_url = 'login'  # Replace with your login URL name

    def form_valid(self, form):
        # Ensure only one base currency exists
        if form.cleaned_data['is_base']:
            Currency.objects.filter(is_base=True).exclude(pk=self.object.pk).update(is_base=False)
        return super().form_valid(form)

class CurrencyDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Currency
    template_name = 'currency/currency_confirm_delete.html'
    success_url = reverse_lazy('currency-list')
    success_message = "ارز موفقانه حذف شد!"
    login_url = 'login'  # Replace with your login URL name











def dashboard_setting_update(request):
    instance = DashboardSetting.load()
    
    if request.method == 'POST':
        form = DashboardSettingForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, _('تنظیمات موفقانه آپدیت شد!'))
            return redirect('dashboard-setting-update')
    else:
        form = DashboardSettingForm(instance=instance)
    
    context = {
        'form': form,
    }
    return render(request, 'dashboard_settings/settings_form.html', context)

















class BuyerListView(ListView):
    model = Buyer
    template_name = 'buyer/buyer_list.html'
    context_object_name = 'buyers'
    paginate_by = 10

class BuyerCreateView(CreateView):
    model = Buyer
    form_class = BuyerForm
    template_name = 'buyer/buyer_form.html'
    success_url = reverse_lazy('buyer_list')

class BuyerUpdateView(UpdateView):
    model = Buyer
    form_class = BuyerForm
    template_name = 'buyer/buyer_form.html'
    success_url = reverse_lazy('buyer_list')

class BuyerDeleteView(DeleteView):
    model = Buyer
    template_name = 'buyer/buyer_confirm_delete.html'
    success_url = reverse_lazy('buyer_list')
