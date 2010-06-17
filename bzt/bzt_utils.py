import json
from django.core import serializers
from django.http import HttpResponse
from django.db import models


#TODO: Deprecate this.  It's not the right way.
def json_response(object):
    """Takes the object, converts it to json, and returns a django http response
    """

    # If it's not iterable, put it alone in a list.
    if not getattr(object, '__iter__', False):
        object = [object]

    output = serializers.serialize("json", object)
    return HttpResponse(output, 'text/plain')


# Note: this class has to exist in an 'app' in django -- if it's in your project's root dir,
# you'll get IndexError: list index out of range when trying to load django.
class SerializableModel(models.Model):
    """A base class for Django models that provides an easy way to serialize to JSON
    including extra information
    """

    class Meta:
        abstract = True

    def to_json(self):
        """Returns a JSON string representing the object.
        It includes all the output of the django.code.serializers and also
        any extra data supplied by the overrideable method extra_json_data
        """

        # First use the default serializer.
        default_serialized_json_string = serializers.serialize("json", [self])

        # Now parse it back into a generic nested-dict object
        # I hate myself when I have to write this kind of code
        serializable_object = json.loads(default_serialized_json_string)[0]

        # Now insert any extra data supplied by sub-classes
        extra_data = self.extra_json_data()
        for key in extra_data.keys():
            serializable_object[key] = extra_data[key]

        # Dump the merged object into JSON
        json_output = json.dumps(serializable_object)
        return json_output



    def extra_json_data(self):
        """Returns a dictionary of extra data to be included in the JSON serialization
        of the object
        """
        return {}
