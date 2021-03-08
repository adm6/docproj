from django.urls import path, include
from . import views
from .views import IndexView, ArticleView, MarathonView, MarathonResultsView, ReceptionView, ConsultationView, \
    ArticlesView, PedometerView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('article/<int:id>', ArticleView.as_view(), name='article'),
    path('articles/', ArticlesView.as_view(), name='articles'),
    path('marathon/', MarathonView.as_view(), name='marathons'),
    path('marathon/<int:id>', MarathonResultsView.as_view(), name='marathonresults'),
    path('reception/', ReceptionView.as_view(), name='reception'),
    path('consultation/', ConsultationView.as_view(), name='consultation'),
    path('pedometer/', PedometerView.as_view(), name='pedometer')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)