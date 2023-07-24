from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .Serializers import *
# from django.http import HttpResponse
# from django.template import loader

# Create your views here.
def home(request):
    return render(request, template_name="Ibiteramo.html")
# def members(request):
#   template = loader.get_template('myfirst.html')
#   return HttpResponse(template.render())


class IbiteramoViewset(viewsets.ModelViewSet):
    queryset= Ibiteramo.objects.all()
    SerializerS_class = IbiteramoSerializer

class ItikeViewset(viewsets.ModelViewSet):
    queryset= Itike.objects.all()
    Serializers_class =ItikeSerializer
