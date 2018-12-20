from django.urls import path
from . import views
from django_pdfkit import PDFView

urlpatterns = [
    path('', views.index, name='index'),
    path('iframe', views.iframe, name='iframe'),
    path('downlaodPDF', views.downlaodPDF, name='downlaodPDF')
]