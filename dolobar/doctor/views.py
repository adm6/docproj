from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from django.shortcuts import render, redirect
from django.views import View
from .models import Article


# Create your views here.
class IndexView(View):
    def get(self, request):
        template = loader.get_template('doctor/index.html')
        articles = Article.objects.all()
        # print(articles[1].image)
        # return HttpResponse(template.render())
        return render(request, 'doctor/index.html', {"articles": articles})


class ArticleView(View):
    def get(self, request, id):
        try:
            article = Article.objects.get(id=id)
            # return HttpResponse(article.title)
            print("URL:   ", article.image)
            return render(request, 'doctor/article.html', {"article": article})
        except Article.DoesNotExist:
            return HttpResponseNotFound()
