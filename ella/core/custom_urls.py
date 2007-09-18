from django.http import Http404

ALL = '__ALL__'
ROOT = '__ROOT__'

class DetailDispatcher(object):
    """
    Our custom url dispatcher that allows for custom actions on objects.

    Usage:
        Register your own view function for some specific URL that is appended to object's absolute url.
        This view will then be called when this URL is used. A small dictionary containing the object,
        it's listing, category, content_type and content_type_name will be passed to the view.

    Example:
        dispatcher.register('rate', rate_object)
        will make the rate_object view available under /rate/...

        dispatcher.register('vote', poll_vote, polls.Poll)
        will enable you to vote for polls under their own url
    """
    def __init__(self):
        self.custom_mapping = {}
        self.root_mapping = {}

    def has_custom_detail(self, obj):
        return obj.__class__ in self.root_mapping

    def call_custom_detail(self, request, context):
        model = context['object'].__class__
        if model not in self.root_mapping:
            raise Http404
        return self.root_mapping[model](request, context)

    def register_custom_detail(self, model, view):
        assert model not in self.root_mapping, "You can only register one function for model %r" % model.__name__
        self.root_mapping[model] = view

    def register(self, start, view, model=None):
        """
        Registers a new custom_mapping to view.

        Params:
            start - first word of the url remainder - the key for the view
            view - the view that acts on this signal
            model - optional, only bind to objects of this model

        Raises:
            AssertionError if the key is already used
        """
        if start in self.custom_mapping:
            assert not model or model not in self.custom_mapping[start], "You can only register one function for key %r and model %r" % (start, model.__name__)
            assert model is not None or ALL not in self.custom_mapping, "You can only register one function for key %r" % start

        map = self.custom_mapping.setdefault(start, {})
        if model:
            map[model] = view
        else:
            map[ALL] = view

    def call_view(self, request, bits, context):
        """
        Call the custom view.

        Params:
            request - Django's HttpRequest
            bits - url remainder splitted by '/'
            context - a dictionary containing the object,
                      it's listing, category and content_type name

        Raises:
            Http404 if no view is associated with bits[0] for content_type of the object
        """
        if bits[0] not in self.custom_mapping:
            raise Http404

        model = context['object'].__class__
        map = self.custom_mapping[bits[0]]
        if model in map:
            view = map[model]
        elif ALL in map:
            view = map[ALL]
        else:
            raise Http404

        return view(request, bits[1:], context)

dispatcher = DetailDispatcher()
