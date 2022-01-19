from django.http import HttpResponse


def home(request):
    # return HttpResponse('Olá Django')
    return HttpResponse('<html><body>Olá Django</body></html>')
