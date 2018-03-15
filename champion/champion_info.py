import requests
from bs4 import BeautifulSoup
from django.utils import timezone

from champion.models import Champion

def champion_info_from(url):
    def ability_value_of(entry):
        return raw_info.find('span', class_=entry).string
    url_content = requests.get(url)
    if url_content.status_code == 200:
        raw_info = BeautifulSoup(url_content.text, 'lxml')
        c = Champion.get_by_name(ability_value_of('champion_name'))
        c.update('eng_name', ability_value_of('champintro-stats__info-name-en'))
        c.update('name', ability_value_of('champion_name'))
        c.update('hp', round(float(ability_value_of('stats_hp')), 3))
        c.update('hpperlevel', round(float(ability_value_of('stats_hpperlevel')), 3))
        c.update('hpmax', round(c.hp + 17 * c.hpperlevel, 3))
        c.update('hpregen', round(float(ability_value_of('stats_hpregen')), 3))
        c.update('hpregenperlevel', round(float(ability_value_of('stats_hpregenperlevel')), 3))
        c.update('hpregenmax', round(c.hpregen + 17 * c.hpregenperlevel, 3))
        c.update('mp', round(float(ability_value_of('stats_mp')), 3))
        c.update('mpperlevel', round(float(ability_value_of('stats_mpperlevel')), 3))
        c.update('mpmax', round(c.mp + 17 * c.mpperlevel, 3))
        c.update('mpregen', round(float(ability_value_of('stats_mpregen')), 3))
        c.update('mpregenperlevel', round(float(ability_value_of('stats_mpregenperlevel')), 3))
        c.update('mpregenmax', round(c.mpregen + 17 * c.mpregenperlevel, 3))
        c.update('movespeed', int(ability_value_of('stats_movespeed')))
        c.update('attackdamage', round(float(ability_value_of('stats_attackdamage')), 3))
        c.update('attackdamageperlevel', round(float(ability_value_of('stats_attackdamageperlevel')), 3))
        c.update('attackdamagemax', round(c.attackdamage + 17 * c.attackdamageperlevel, 3))
        c.update('attackspeed', round(0.625 / (1 + float(ability_value_of('stats_attackspeedoffset'))), 3))
        c.update('attackspeedperlevel', round(float(ability_value_of('stats_attackspeedperlevel')), 3))
        c.update('attackspeedmax', round(c.attackspeed * (1 + c.attackspeedperlevel * 17 / 100), 3))
        c.update('attackrange', int(ability_value_of('stats_attackrange')))
        c.update('armor', round(float(ability_value_of('stats_armor')), 3))
        c.update('armorperlevel', round(float(ability_value_of('stats_armorperlevel')), 3))
        c.update('armormax', round(c.armor + 17 * c.armorperlevel, 3))
        c.update('spellblock', round(float(ability_value_of('stats_spellblock')), 3))
        c.update('spellblockperlevel', round(float(ability_value_of('stats_spellblockperlevel')), 3))
        c.update('spellblockmax', round(c.spellblock + 17 * c.spellblockperlevel, 3))
        c.save()
    else:
        print("Unable to connect the site:" + url)
