from django.core import serializers
from django.http import HttpResponse

def json_response(object):
    """Takes the object, converts it to json, and returns a django http response
    """

    # If it's not iterable, put it alone in a list.
    if not getattr(object, '__iter__', False):
        object = [object]

    output = serializers.serialize("json", object)
    return HttpResponse(output, 'text/plain')

