import json

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

from blog.models import *


def apphtml(request):
    return render_to_response("app.html")

def list(request):
    queryset = Post.objects.all()
    objectlist = [x for x in queryset]
    output = json.dumps(objectlist)
    return HttpResponse(output, 'text/plain')


def delete(request,id):
    if request.method == 'GET':
        return HttpResponse('Side-effect method requires HTTP POST', 'text/plain')

    obj = get_object_or_404(Post,pk=id)
    obj.delete()
    return HttpResponse('Deleted', 'text/plain')

