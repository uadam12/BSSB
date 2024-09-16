from django import forms
from .models import Bank, LGA, Article

class BankForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BankForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Enter Bank Name here...'
        self.fields['code'].widget.attrs['placeholder'] = 'Enter Bank Code here...'
        
    class Meta:
        model = Bank
        fields = ("name", "code")

class LGAForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LGAForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Enter Local Goverment Area Name here...'

    class Meta:
        model = LGA
        fields = ("name",)

class ArticleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['headline'].widget.attrs['placeholder'] = 'Enter article headline here...'
        self.fields['content'].widget.attrs['placeholder'] = 'Enter article content here...'
        
    class Meta:
        model = Article
        fields = ("headline", "headline_image", "content",)
