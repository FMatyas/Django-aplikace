from django.shortcuts import render, get_object_or_404
from .models import Tym, Zapas, Hrac

def index(request):
    context = {
        'pocet_tymu': Tym.objects.count(),
        'celkem_zapasu': Zapas.objects.count(),
        'odehrano': Zapas.objects.filter(domaci_goly__gte=0).count(),
        'planovano': Zapas.objects.filter(domaci_goly=-1).count(),
    }
    return render(request, 'turnaj/index.html', context)

def seznam_tymu(request):
    tymy = Tym.objects.all().order_by('jmeno_tymu')
    return render(request, 'turnaj/seznam_tymu.html', {'tymy': tymy})

def detail_tymu(request, tym_id):
    tym = get_object_or_404(Tym.objects.prefetch_related('hraci'), id=tym_id)
    return render(request, 'turnaj/detail_tymu.html', {'tym': tym})

def seznam_zapasu(request):
    zapasy = Zapas.objects.select_related('id_domaci_tym', 'id_hostujici_tym').prefetch_related('strelci__id_hrac').all().order_by('datum_zapasu')
    return render(request, 'turnaj/seznam_zapasu.html', {'zapasy': zapasy})