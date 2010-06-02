from django.core import serializers
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

from blog.models import Post


def apphtml(request):
    return render_to_response("app.html", {}, context_instance=RequestContext(request))

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
    if request.method == 'GET':
        return HttpResponse("{'error':'Side-effect method requires HTTP POST'}", 'text/plain')

    newpost = Post()
    newpost.title = request.POST['post.title']
    newpost.name = request.POST['post.name']
    newpost.content = request.POST['post.content']
    newpost.save()

    response = serializers.serialize("json", [newpost])
    return HttpResponse(response, 'text/plain')
    
