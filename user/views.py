import os
from django.shortcuts import render
from django.http import HttpResponse
from . import views
from django.template.loader import get_template 
from django.template import Context
import pdfkit

# Create your views here.
def index(request):
    return render(request, 'views/index.html')

def iframe(request):
    return render(request, 'includes/iframe.html')
    
def downlaodPDF(request):
    template = get_template('invoice/test.html')
    context = {"data": "Welcome to Knimbus"}  # data is the context data that is sent to the html file to render the output. 
    html = template.render(context)  # Renders the template with the context data.
    pdfkit.from_string(html, 'out.pdf')
    
    with open("out.pdf", 'rb') as f:
        contents = f.read()
    response = HttpResponse(contents, content_type='application/pdf')  # Generates the response as pdf response.
    response['Content-Disposition'] = 'attachment; filename=out.pdf'
    
    return response