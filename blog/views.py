from django.core import serializers
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

import blog.models
from blog.models import Post


def apphtml(request):
    return render_to_response("app.html", {}, context_instance=RequestContext(request))


def json_response(object):
    """Takes the object, converts it to json, and returns a django http response
    """

    # TODO: Make a better way to serialize a single model object
    if type(object) == blog.models.Post:
        object = [object]

    output = serializers.serialize("json", object)
    return HttpResponse(output, 'text/plain')


def list(request):
    queryset = Post.objects.all()
    return json_response(queryset)


def delete(request,id):
    if request.method == 'GET':
        return HttpResponse('Side-effect method requires HTTP POST', 'text/plain')

    obj = get_object_or_404(Post,pk=id)
    obj.delete()
    return HttpResponse("{'result':'Deleted'}", 'text/plain')


def show(request,id):
    obj = get_object_or_404(Post,pk=id)
    return json_response(obj)
    


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
    

def edit(request):
    if request.method == 'GET':
        return HttpResponse("{'error':'Side-effect method requires HTTP POST'}", 'text/plain')

    id = request.POST['post.id']
    obj = get_object_or_404(Post,pk=id)
    newpost = get_object_or_404(Post,pk=id)
    newpost.title = request.POST['post.title']
    newpost.name = request.POST['post.name']
    newpost.content = request.POST['post.content']
    newpost.save()

    response = serializers.serialize("json", [newpost])
    return HttpResponse(response, 'text/plain')
    
