from django.http import HttpResponse


def home(request):
    # return HttpResponse('Olá Django')
    # raise ValueError()
    return HttpResponse('<html><body>Olá Django</body></html>')
