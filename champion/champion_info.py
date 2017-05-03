import re
import requests
from bs4 import BeautifulSoup

import datetime
from django.utils import timezone
from champion.models import Champion
from django.core.exceptions import ObjectDoesNotExist

def champion_info_from(url):
    def ability_value_of(entry):
        return raw_info.find('span' , class_=entry).string
    def check_diff(champion, attr, stat):
        nonlocal check_update
        if getattr(champion, attr) != stat:
            setattr(champion, attr, stat)
            print(champion.eng_name + " " + attr + " is updated.")
            check_update = True
    url_content = requests.get(url)
    if url_content.status_code == 200:
        raw_info = BeautifulSoup(url_content.text , 'lxml')
        try:
            champion = Champion.objects.get(name = ability_value_of('champion_name'))
        except ObjectDoesNotExist:
            champion = Champion()
        finally:
            check_update = False
            check_diff(champion, 'eng_name'            , ability_value_of('champintro-stats__info-name-en'))
            check_diff(champion, 'name'                , ability_value_of('champion_name'))
            check_diff(champion, 'hp'                  , round(float(ability_value_of('stats_hp')), 3))
            check_diff(champion, 'hpperlevel'          , round(float(ability_value_of('stats_hpperlevel')), 3))
            check_diff(champion, 'hpmax'               , round(champion.hp + 17*champion.hpperlevel, 3))
            check_diff(champion, 'hpregen'             , round(float(ability_value_of('stats_hpregen')), 3))
            check_diff(champion, 'hpregenperlevel'     , round(float(ability_value_of('stats_hpregenperlevel')), 3))
            check_diff(champion, 'hpregenmax'          , round(champion.hpregen + 17*champion.hpregenperlevel, 3))
            check_diff(champion, 'mp'                  , round(float(ability_value_of('stats_mp')), 3))
            check_diff(champion, 'mpperlevel'          , round(float(ability_value_of('stats_mpperlevel')), 3))
            check_diff(champion, 'mpmax'               , round(champion.mp + 17*champion.mpperlevel, 3))
            check_diff(champion, 'mpregen'             , round(float(ability_value_of('stats_mpregen')), 3))
            check_diff(champion, 'mpregenperlevel'     , round(float(ability_value_of('stats_mpregenperlevel')), 3))
            check_diff(champion, 'mpregenmax'          , round(champion.mpregen + 17*champion.mpregenperlevel, 3))
            check_diff(champion, 'movespeed'           , int(ability_value_of('stats_movespeed')))
            check_diff(champion, 'attackdamage'        , round(float(ability_value_of('stats_attackdamage')), 3))
            check_diff(champion, 'attackdamageperlevel', round(float(ability_value_of('stats_attackdamageperlevel')), 3))
            check_diff(champion, 'attackdamagemax'     , round(champion.attackdamage + 17*champion.attackdamageperlevel, 3))
            check_diff(champion, 'attackspeed'         , round(0.625/(1+float(ability_value_of('stats_attackspeedoffset'))), 3))
            check_diff(champion, 'attackspeedperlevel' , round(float(ability_value_of('stats_attackspeedperlevel')), 3))
            check_diff(champion, 'attackrange'         , int(ability_value_of('stats_attackrange')))
            check_diff(champion, 'armor'               , round(float(ability_value_of('stats_armor')), 3))
            check_diff(champion, 'armorperlevel'       , round(float(ability_value_of('stats_armorperlevel')), 3))
            check_diff(champion, 'armormax'            , round(champion.armor + 17*champion.armorperlevel, 3))
            check_diff(champion, 'spellblock'          , round(float(ability_value_of('stats_spellblock')), 3))
            check_diff(champion, 'spellblockperlevel'  , round(float(ability_value_of('stats_spellblockperlevel')), 3))
            check_diff(champion, 'spellblockmax'       , round(champion.spellblock + 17*champion.spellblockperlevel, 3))
            if check_update:
                champion.update_date = timezone.now()
                champion.save()
    else:
        print("Unable to connect the site:" + url)
