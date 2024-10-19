from django.http import HttpResponse

def htop_view(request):
    return HttpResponse("Your htop data goes here")
