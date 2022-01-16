from django.http import HttpResponse
from django.views.generic import TemplateView


def hellofunction(request):
    return HttpResponse('hello')

class HelloWorldClass(TemplateView):
    template_name = 'hello.html'