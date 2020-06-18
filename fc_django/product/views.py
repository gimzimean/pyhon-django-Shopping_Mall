from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Product
from .forms import RegisterForm
from order.forms import RegisterForm as OrderForm
#decorator
from django.utils.decorators import method_decorator
from fcuser.decorators import admin_required
# Create your views here.
class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'

@method_decorator(admin_required, name='dispatch')
class ProductCreate(FormView):
    template_name = 'register_product.html'
    context_object_name = 'product_list'
    form_class = RegisterForm
    success_url ='/product/'

class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()   
    context_object_name = 'product'

    def get_context_data(self, **kwargs): # 내가 원하는 데이터를 넣을 수 있는 함수
        context = super().get_context_data(**kwargs) # super() DetailView먼저 실행 

        context['form'] = OrderForm(self.request) # form이라는 변수 추가 
        return context
