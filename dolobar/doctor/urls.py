from django.urls import path, include
from . import views
from .views import IndexView, ArticleView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('article/<int:id>', ArticleView.as_view(), name='article')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)