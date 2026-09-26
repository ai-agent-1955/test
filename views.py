from django.http import HttpResponse

def hello(request):
    return HttpResponse('سلام')

# Add the following lines to your urls.py to route to this view:
# from django.urls import path
# from .views import hello
# urlpatterns = [
#     path('hello/', hello),
# ]