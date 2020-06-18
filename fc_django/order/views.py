from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import RegisterForm
from .models import Order
#decorator
from django.utils.decorators import method_decorator
from fcuser.decorators import login_required

#트랜젝션
from django.db import transaction
from product.models import Product
from fcuser.models import Fcuser


# Create your views here.
@method_decorator(login_required, name='dispatch')
class OrderCreate(FormView):
    form_class = RegisterForm
    success_url ='/product/'

    def form_valid(self, form):
        with transaction.atomic(): # 트랜젝션 처리
            prod = Product.objects.get(pk=form.data.get('product'))
            order = Order(
                quantity = form.data.get('quantity'),
                product = prod,
                fcuser = Fcuser.objects.get(email= self.request.session.get('user'))
            )
            order.save()
            prod.stock -= int(form.data.get('quantity')) # 재고 차감
            prod.save()
        return super().form_valid(form)



    def form_invalid(self, form): # 유효하지 않았을때 돌아가기
        return redirect('/product/'+str(form.data.get('product')))



    def get_form_kwargs(self, **kwargs): # form을 생성할 때 어떤 인자값을 전달해서 만들것인지 결정하는 함수
        kw= super().get_form_kwargs(**kwargs) # 기존 함수 호출
        kw.update({
            'request': self.request
        })
        return kw  #함께 만들어서 전달하기
@method_decorator(login_required, name='dispatch')
class OrderList(ListView):
    # model = Order 다른 사람들의 주문들도 볼 수 있기떄문 -> query Set
    template_name = 'order.html'
    context_object_name = 'order_list'

    def get_queryset(self, **kwargs): # 현재 로그인한 사람거만 가져옴.(오버라이딩)
        queryset = Order.objects.filter(fcuser__email = self.request.session.get('user'))
        return queryset
    
    # def dispatch(request, *args, **kwargs)

    # url에 접글했을때 클래스를 호출할땐 dispatcher이 호출됨.


