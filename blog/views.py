from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

from blog.models import *


def apphtml(request):
    return render_to_response("app.html")

def list(request):
    queryset = Post.objects.all()
    output = serializers.serialize("json", queryset)
    return HttpResponse(output, 'text/plain')


def delete(request,id):
    if request.method == 'GET':
        return HttpResponse('Side-effect method requires HTTP POST', 'text/plain')

    obj = get_object_or_404(Post,pk=id)
    obj.delete()
    return HttpResponse('Deleted', 'text/plain')


def create(request):
    return HttpResponse('[1]', 'text/plain')
    
