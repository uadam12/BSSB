from app import render
from app.views import details_view, update_view, delete_view
from .forms import (
    Bank, BankForm,
    LGA, LGAForm,
    Article, ArticleForm
)


def index(request):
    return render(request, 'main/index')

def news(request):
    return render(request, 'main/news')

def about(request):
    return render(request, 'main/about')

def contact(request):
    return render(request, 'main/contact')

# Banks
def banks(request):
    return details_view(
        request, BankForm, 
        header="Bank",
        data_template='main/banks.html',
        banks = Bank.objects.order_by('name')
    )

def update_bank(request, id):
    bank = Bank.objects.get(id=id)
    
    return update_view(
        request, 
        model=bank, 
        form_class=BankForm, 
        success_url='main:banks', 
        header='Bank'
    )
    
def delete_bank(request, id):
    bank = Bank.objects.get(id=id)
    
    return delete_view(
        request, 
        model=bank,
        success_url='main:banks', 
        header='Bank'
    )

# Local Government Area(LGA)
def lgas(request):
    return details_view(
        request, LGAForm, 
        header="Local Government Area",
        data_template='main/lgas.html',
        lgas = LGA.objects.order_by('name')
    )

def update_lga(request, id):
    lga = LGA.objects.get(id=id)
    
    return update_view(
        request, 
        model=lga, 
        form_class=LGAForm, 
        success_url='main:lgas', 
        header='Local Government Area'
    )
    
def delete_lga(request, id):
    lga = LGA.objects.get(id=id)
    
    return delete_view(
        request, 
        model=lga,
        success_url='main:lgas', 
        header='Local Government Area'
    )
    
# Articles
def articles(request):
    return details_view(
        request, ArticleForm, 
        header="Article",
        data_template='main/articles.html',
        articles = Article.objects.order_by('-publish_on')
    )

def update_article(request, id):
    article = Article.objects.get(id=id)
    
    return update_view(
        request, 
        model=article, 
        form_class=ArticleForm, 
        success_url='main:articles', 
        header='Article'
    )
    
def delete_article(request, id):
    article = Article.objects.get(id=id)
    
    return delete_view(
        request, 
        model=article,
        success_url='main:articles', 
        header='Local Government Area'
    )