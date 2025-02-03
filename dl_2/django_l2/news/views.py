from django.shortcuts import render
from django.http import HttpResponse

from news.models import Article, Journalist

# Create your views here.

# def home(request):
#     articles = []
#     journalists = []

#     for a in Article.objects.all():
#         articles.append(a.title)
#         articles.append(a.content)
#         articles.append(a.journalist)

#     for j in Journalist.objects.all():
#         journalists.append(j.first_name)
#         journalists.append(j.last_name)

#     response = str(articles) + "<br>" + str(journalists)

#     return HttpResponse({response})

def home(request):
    articles = Article.objects.all()
    journalists = Journalist.objects.all()
    context = {"articles":articles, "journalists":journalists}

    return render(request, "news/homepage.html", context)