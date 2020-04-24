import os
from django.http import HttpResponse
from django.views.generic import TemplateView

"""
what Django do
reseice the request object and send the responce file
There are 2 ways to make view file, function or class.
"""

# function based view(普通)
def helloworldfunction(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(__file__)
    returnobject = HttpResponse("<h1<hello world</h1>")
    return returnobject


# calss based view(便利)
class HelloWorldView(TemplateView):
    template_name = "hello.html"  # 持ってくるfileを指定 