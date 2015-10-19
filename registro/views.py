from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader


from .models import Incidencia


def index(request):
    ultimas_incidencias = Incidencia.objects.order_by('-incidencia_fecha')[:5]
    context = {'ultimas_incidencias': ultimas_incidencias}
    return render(request, 'registro/index.html', context)

def detail(request, inci_id):
    inci = get_object_or_404(Incidencia, pk=inci_id)
    return render(request, 'registro/detail.html', {'inci': inci})
