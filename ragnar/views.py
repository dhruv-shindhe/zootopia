from django.shortcuts import render
import random
from .models import Quotes

# Create your views here.
def home(request):
    upper_limit = 15
    quote_limit = 30
    q_no = (str)(random.randint(1,quote_limit))
    quote = Quotes.objects.filter(pk=q_no).first
    print(quote)
    no = (str)(random.randint(1,upper_limit))
    img_name = 'img'+no+'.jpg'
    context ={'img_name':img_name, 'quote':quote}
    print(img_name)
    return render(request,'ragnar_t1/home.html',context)
