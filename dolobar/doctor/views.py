from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from django.shortcuts import render, redirect
from django.views import View
from .models import Article, Marathon, Reception, Consultation, Pedometer


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


class MarathonView(View):
    def get(self, request):
        marathons = Marathon.objects.order_by('-starting_day')
        return render(request, 'doctor/marathons.html', {'marathons': marathons})


class MarathonResultsView(View):
    def get(self, request, id):
        article = Marathon.objects.get(pk=id)
        return render(request, 'doctor/marathon_results.html', {'article': article})


class ReceptionView(View):
    def get(self, request):
        reception = Reception.objects.all()
        reception = reception[0]
        return render(request, 'doctor/reception.html', {'reception': reception})


class ConsultationView(View):
    def get(self, request):
        consultation = Consultation.objects.all()
        consultation = consultation[0]
        return render(request, 'doctor/consultation.html', {'consultation': consultation})


class ArticlesView(View):
    def get(self, request):
        # template = loader.get_template('doctor/articles.html')
        articles = Article.objects.all()
        return render(request, 'doctor/articles.html', {'articles': articles})


class PedometerView(View):
    def get(self, request):
        pedometer = Pedometer.objects.all()
        pedometer = pedometer[0]
        return render(request, 'doctor/pedometer.html', {'pedometer': pedometer})





