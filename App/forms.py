from .models import Callback, News
from django.forms import ModelForm



class CallbackForm(ModelForm):
    class Meta:
        model = Callback
        fields = ['name', 'phone']

        def __init__(self, *args, **kwargs):
            super(CallbackForm, self).__init__(*args, **kwargs)

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['text']

        def __init__(self, *args, **kwargs):
            super(NewsForm, self).__init__(*args, **kwargs)

class EventsForm(ModelForm):
    class Meta:
        model = News
        fields = ['text']

        def __init__(self, *args, **kwargs):
            super(EventsForm, self).__init__(*args, **kwargs)

