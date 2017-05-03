from django.shortcuts import render
from django_tables2 import RequestConfig
from django.utils import timezone
import datetime

from .models import Champion
from .tables import ChampionTable

def all_champion(request):
    table = ChampionTable(Champion.objects.all(), exclude = ('id', 'update_date'))
    title = 'Champion Information Table'
    RequestConfig(request, paginate={'per_page': 50}).configure(table)
    return render(request, 'champion/champion_info.html', {'table': table, 'title': title})

def reccent_update(request):
    table = ChampionTable(Champion.objects.filter(update_date__gte=timezone.now()-datetime.timedelta(days=7)), exclude = ('id'), order_by = '-update_date')
    title = 'Reccent Update Champion'
    RequestConfig(request, paginate={'per_page': 50}).configure(table)
    return render(request, 'champion/reccent_update.html', {'table': table, 'title': title})
