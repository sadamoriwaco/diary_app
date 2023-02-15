from django import forms
from django.core.mail import EmailMessage
from .models import Diary
from django.db.models import fields

Zipcode = {
    'zip_code':
        forms.TextInput(
            attrs={'class': 'p-postal-code','placeholder': '記入例：1060022'}, 
            ),
}
class InquiryForm(forms.Form):

    name = forms.CharField(label = 'お名前',max_length=30)
    email = forms.EmailField(label= 'メールアドレス')

    zipcode = forms.RegexField(label='郵便番号(ハイフンなし)',
    regex=r'^[0-9]+$',
    max_length=7,
    widget=forms.TextInput(attrs={'onKeyUp' : "AjaxZip3.zip2addr(this,'','state','city')"}),)
    state = forms.CharField(label='都道府県',max_length=6)
    city = forms.CharField(label='市区町村',max_length=10)
    address_1 = forms.CharField(label='番地',max_length=10)
    address_2 = forms.CharField(label='建物名・部屋番号',max_length=10)


    title = forms.CharField(label='タイトル',max_length=30)
    message = forms.CharField(label='メッセージ',widget=forms.Textarea)

    

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields['name'].widget.attrs['class']='form-control col-9'
        self.fields['name'].widget.attrs['placeholder']='お名前をここに入力してください'

        self.fields['email'].widget.attrs['class']='form-control col-11'
        self.fields['email'].widget.attrs['placeholder']='メールアドレスをここに入力してください'

        self.fields['zipcode'].widget.attrs['class']='form-control col-11'
        self.fields['zipcode'].widget.attrs['placeholder']='例：1600022 '

        self.fields['state'].widget.attrs['class']='form-control col-11'
        self.fields['state'].widget.attrs['placeholder']='都道府県をここに入力してください'

        self.fields['city'].widget.attrs['class']='form-control col-11'
        self.fields['city'].widget.attrs['placeholder']='市区町村をここに入力してください'

        self.fields['address_1'].widget.attrs['class']='form-control col-11'
        self.fields['address_1'].widget.attrs['placeholder']='番地をここに入力してください'

        self.fields['address_2'].widget.attrs['class']='form-control col-11'
        self.fields['address_2'].widget.attrs['placeholder']='建物名・部屋番号をここに入力してください'

        self.fields['title'].widget.attrs['class']='form-control col-11'
        self.fields['title'].widget.attrs['placeholder']='タイトルをここに入力してください'

        self.fields['message'].widget.attrs['class']='form-control col-12'
        self.fields['message'].widget.attrs['placeholder']='内容をここに入力してください'

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        subject = 'お問い合わせ {} '.format(title)
        message = '送信者名：{0} \n メールアドレス：{1} \n メッセージ：{2}'.format(name,email,message)
        from_email = 'admin@example.com'
        to_list = [
            'text@example.com'
        ]
        cc_list = [
            email
        ]

        message = EmailMessage(subject=subject,body=message,from_email=from_email,to=to_list,cc=cc_list)
        message.send()

class DiaryCreateForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('title','content','photo1','photo2','photo3',)
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['class']='form-control'

