from django import forms
from .models import Order
from product.models import Product
from fcuser.models import Fcuser
from django.db import transaction

class RegisterForm(forms.Form):
    def __init__(self, request, *args, **kwargs): # request를 form에 전달할 수 있도록 하는 것 # form을 생성할 때 !
        super().__init__(*args, **kwargs)
        self.request = request # 생성자 

    quantity = forms.IntegerField(error_messages={
        'required' : '수량을 입력해주세요'
    }, label='수량'
    )
    product = forms.IntegerField(error_messages={
        'required' : '상품설명을 입력해주세요'
    }, label='상품설명', widget = forms.HiddenInput # 사용자에게 보이진 않음 
    )


    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
        fcuser = self.request.session.get('user') # email을 가져옴

        # user를 들고 오려면 세션에 접근해야함. -> form변경해야함.
        print(self.request.session)
        if quantity and product and fcuser:
            with transaction.atomic(): # 트랜젝션 처리
                prod = Product.objects.get(pk=product)
                order = Order(
                quantity = quantity,
                product = prod,
                fcuser = Fcuser.objects.get(email=fcuser)
                )
                order.save()
                prod.stock -= quantity # 재고 차감
                prod.save()

           
        else:
            self.product = product # redirect할때 값을 넘겨주ㄱ는거
            self.add_error('quantity', '값이 없습니다.')
            self.add_error('product', '값이 없습니다.')


