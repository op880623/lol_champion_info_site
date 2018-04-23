from re import finditer

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

        # make iterator for champion pages
        pages = map(
            lambda url: requests.get('https://lol.garena.tw' + url.group(1)),
            finditer('href="(/game/champion/\w+)"', content)
        )

        # get champion info from each page
        for page in pages:
            # handle url with problem
            if page.status_code != 200:
                print("Unable to connect the site:" + url)
                return None

            raw_info = BeautifulSoup(page.text, 'lxml')
            stats = {}

            # name
            stats['eng_name'] = value('champintro-stats__info-name-en', num=False)
            stats['name'] = value('champion_name', num=False)

            # hp
            stats['hp'] = value('stats_hp')
            stats['hpperlevel'] = value('stats_hpperlevel')
            stats['hpmax'] = value_max(stats['hp'], stats['hpperlevel'])
            stats['hpregen'] = value('stats_hpregen')
            stats['hpregenperlevel'] = value('stats_hpregenperlevel')
            stats['hpregenmax'] = value_max(stats['hpregen'],
                                            stats['hpregenperlevel'])

            # mp
            stats['mp'] = value('stats_mp')
            stats['mpperlevel'] = value('stats_mpperlevel')
            stats['mpmax'] = value_max(stats['mp'], stats['mpperlevel'])
            stats['mpregen'] = value('stats_mpregen')
            stats['mpregenperlevel'] = value('stats_mpregenperlevel')
            stats['mpregenmax'] = value_max(stats['mpregen'],
                                            stats['mpregenperlevel'])

            # move speed
            stats['movespeed'] = int(value('stats_movespeed', num=False))

            # attack damage
            stats['attackdamage'] = value('stats_attackdamage')
            stats['attackdamageperlevel'] = value('stats_attackdamageperlevel')
            stats['attackdamagemax'] = value_max(stats['attackdamage'],
                                                stats['attackdamageperlevel'])

            # attack speed
            stats['attackspeed'] = round(
                0.625 / (1 + float(value('stats_attackspeedoffset', num=False))),
                3
            )
            stats['attackspeedperlevel'] = value('stats_attackspeedperlevel')
            stats['attackspeedmax'] = round(
                stats['attackspeed']
                * (1 + stats['attackspeedperlevel']
                * 17 / 100),
                3
            )

            # attack range
            stats['attackrange'] = int(value('stats_attackrange', num=False))

            # armor
            stats['armor'] = value('stats_armor')
            stats['armorperlevel'] = value('stats_armorperlevel')
            stats['armormax'] = value_max(stats['armor'], stats['armorperlevel'])

            # spell block
            stats['spellblock'] = value('stats_spellblock')
            stats['spellblockperlevel'] = value('stats_spellblockperlevel')
            stats['spellblockmax'] = value_max(stats['spellblock'],
                                                stats['spellblockperlevel'])

            Champion.get_by_name(stats['name']).update(stats)

        print("Update is finished.")
