from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Mi primera web con DJango")

    
