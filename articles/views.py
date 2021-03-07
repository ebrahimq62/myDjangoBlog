from django.shortcuts import render
from . import models
def article_lists(request):
    articles=models.Articles.objects.all()
    args={'articles':articles}
    return render(request,'articles/article_lists.html',args)

