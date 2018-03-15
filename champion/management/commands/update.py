import requests
from bs4 import BeautifulSoup
from selenium import webdriver

from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError

from champion.models import Champion

class Command(BaseCommand):
    help = "Update all champions"

    def handle(self, *args, **options):
        def value(entry, num=True):
            if num:
                return round(float(raw_info.find('span', class_=entry).string), 3)
            else:
                return raw_info.find('span', class_=entry).string

        def value_max(base, perlv):
            return round(base + 17 * perlv, 3)

        # get page containing champion list
        browser = webdriver.PhantomJS()
        browser.implicitly_wait(5)
        browser.get('https://lol.garena.tw/game/champion')
        content = browser.page_source
        browser.quit()

        # get champion url list
        soup_content = BeautifulSoup(content, 'lxml')
        url_tags = soup_content.find_all('a', class_='champlist-item__link')

        # get champion info from each url
        for url_tag in url_tags:
            url = 'https://lol.garena.tw' + url_tag['href']
            page = requests.get(url)

            # handle url with problem
            if page.status_code != 200:
                print("Unable to connect the site:" + url)
                return None

            raw_info = BeautifulSoup(page.text, 'lxml')
            c = Champion.get_by_name(value('champion_name', num=False))


            # name
            eng_name = value('champintro-stats__info-name-en', num=False)
            c.update('eng_name', eng_name)

            name = value('champion_name', num=False)
            c.update('name', name)


            # hp
            hp = value('stats_hp')
            c.update('hp', hp)

            hpperlevel = value('stats_hpperlevel')
            c.update('hpperlevel', hpperlevel)

            hpmax = value_max(hp, hpperlevel)
            c.update('hpmax', hpmax)

            hpregen = value('stats_hpregen')
            c.update('hpregen', hpregen)

            hpregenperlevel = value('stats_hpregenperlevel')
            c.update('hpregenperlevel', hpregenperlevel)

            hpregenmax = value_max(hpregen, hpregenperlevel)
            c.update('hpregenmax', hpregenmax)


            # mp
            mp = value('stats_mp')
            c.update('mp', mp)

            mpperlevel = value('stats_mpperlevel')
            c.update('mpperlevel', mpperlevel)

            mpmax = value_max(mp, mpperlevel)
            c.update('mpmax', mpmax)

            mpregen = value('stats_mpregen')
            c.update('mpregen', mpregen)

            mpregenperlevel = value('stats_mpregenperlevel')
            c.update('mpregenperlevel', mpregenperlevel)

            mpregenmax = value_max(mpregen, mpregenperlevel)
            c.update('mpregenmax', mpregenmax)

            # movespeed
            movespeed = int(value('stats_movespeed', num=False))
            c.update('movespeed', movespeed)


            # attackdamage
            attackdamage = value('stats_attackdamage')
            c.update('attackdamage', attackdamage)

            attackdamageperlevel = value('stats_attackdamageperlevel')
            c.update('attackdamageperlevel', attackdamageperlevel)

            attackdamagemax = value_max(attackdamage, attackdamageperlevel)
            c.update('attackdamagemax', attackdamagemax)


            # attackspeed
            attackspeed = round(
                0.625 / (1 + float(value('stats_attackspeedoffset', num=False))),
                3
            )
            c.update('attackspeed', attackspeed)

            attackspeedperlevel = value('stats_attackspeedperlevel')
            c.update('attackspeedperlevel', attackspeedperlevel)

            attackspeedmax = round(
                c.attackspeed * (1 + c.attackspeedperlevel * 17 / 100),
                3
            )
            c.update('attackspeedmax', attackspeedmax)


            # special attribute
            attackrange = int(value('stats_attackrange', num=False))
            c.update('attackrange', attackrange)


            # armor
            armor = value('stats_armor')
            c.update('armor', armor)

            armorperlevel = value('stats_armorperlevel')
            c.update('armorperlevel', armorperlevel)

            armormax = value_max(armor, armorperlevel)
            c.update('armormax', armormax)


            # spellblock
            spellblock = value('stats_spellblock')
            c.update('spellblock', spellblock)

            spellblockperlevel = value('stats_spellblockperlevel')
            c.update('spellblockperlevel', spellblockperlevel)

            spellblockmax = value_max(spellblock, spellblockperlevel)
            c.update('spellblockmax', spellblockmax)


            c.save()

        print("Update is finished.")
