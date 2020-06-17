from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import RegisterForm


# Create your views here.
class OrderCreate(FormView):
    form_class = RegisterForm
    success_url ='/product/'

    def form_invalid(self, form): # 유효하지 않았을때 돌아가기
        return redirect('/product/'+str(form.product))

    def get_form_kwargs(self, **kwargs): # form을 생성할 때 어떤 인자값을 전달해서 만들것인지 결정하는 함수
        kw= super().get_form_kwargs(**kwargs) # 기존 함수 호출
        kw.update({
            'request': self.request
        })
        return kw  #함께 만들어서 전달하기