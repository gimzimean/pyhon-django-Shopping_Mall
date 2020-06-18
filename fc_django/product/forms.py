from django import forms
from .models import Product

class RegisterForm(forms.Form):
    name = forms.CharField(error_messages={
        'required' : '상품명을 입력해주세요'
    }, max_length = 64, label='상품명'
    )
    price = forms.IntegerField(error_messages={
        'required' : '상품가격을 입력해주세요'
    }, label='상품가격'
    )
    description = forms.CharField(error_messages={
        'required' : '상품설명을 입력해주세요'
    }, label='상품설명'
    )
    stock = forms.IntegerField(error_messages={
        'required' : '재고를 입력해주세요'
    }, label='재고'
    )


    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        price = cleaned_data.get('price')
        description = cleaned_data.get('description')
        stock = cleaned_data.get('stock')

        if not (name and price and description and stock) :
            self.add_error('name','값이 없습니다.')
            self.add_error('price','값이 없습니다.')
            


class LoginForm(forms.Form):
    email = forms.EmailField(error_messages={
        'required' : '이메일을 입력해주세요'
    }, max_length = 64, label='이메일'
    )

    password = forms.CharField(error_messages={
        'required' : '비밀번호를 입력해주세요'
    }, widget=forms.PasswordInput, label='비밀번호')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                fcuser = Fcuser.objects.get(email= email)
            except Fcuser.DoesNotExist:
                self.add_error('email', '아이디가 없습니다.')
                return
            
            if not check_password(password, fcuser.password):
                self.add_error('password', '비밀번호가 틀렸습니다.')
            else:
                self.email = fcuser.email