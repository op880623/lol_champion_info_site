import datetime

from django.db import models
from django.utils import timezone


class Champion(models.Model):
    name                 = models.CharField(max_length=30, default='')
    eng_name             = models.CharField(max_length=30, default='')
    hp                   = models.FloatField(max_length=10, default=0)
    hpperlevel           = models.FloatField(max_length=10, default=0)
    hpmax                = models.FloatField(max_length=10, default=0)
    hpregen              = models.FloatField(max_length=10, default=0)
    hpregenperlevel      = models.FloatField(max_length=10, default=0)
    hpregenmax           = models.FloatField(max_length=10, default=0)
    mp                   = models.FloatField(max_length=10, default=0)
    mpperlevel           = models.FloatField(max_length=10, default=0)
    mpmax                = models.FloatField(max_length=10, default=0)
    mpregen              = models.FloatField(max_length=10, default=0)
    mpregenperlevel      = models.FloatField(max_length=10, default=0)
    mpregenmax           = models.FloatField(max_length=10, default=0)
    movespeed            = models.IntegerField(default=0)
    attackdamage         = models.FloatField(max_length=10, default=0)
    attackdamageperlevel = models.FloatField(max_length=10, default=0)
    attackdamagemax      = models.FloatField(max_length=10, default=0)
    attackrange          = models.IntegerField(default=0)
    armor                = models.FloatField(max_length=10, default=0)
    armorperlevel        = models.FloatField(max_length=10, default=0)
    armormax             = models.FloatField(max_length=10, default=0)
    spellblock           = models.FloatField(max_length=10, default=0)
    spellblockperlevel   = models.FloatField(max_length=10, default=0)
    spellblockmax        = models.FloatField(max_length=10, default=0)
    update_date          = models.DateTimeField('update date')

    attributes = [
        'name',
        'eng_name',
        'hp',
        'hpperlevel',
        'hpmax',
        'hpregen',
        'hpregenperlevel',
        'hpregenmax',
        'mp',
        'mpperlevel',
        'mpmax',
        'mpregen',
        'mpregenperlevel',
        'mpregenmax',
        'movespeed',
        'attackdamage',
        'attackdamageperlevel',
        'attackdamagemax',
        'attackrange',
        'armor',
        'armorperlevel',
        'armormax',
        'spellblock',
        'spellblockperlevel',
        'spellblockmax',
        'update_date'
    ]

    def __str__(self):
        return self.name

    @classmethod
    def get_by_name(cls, name):
        if Champion.objects.filter(name = name).exists():
            return Champion.objects.get(name = name)
        else:
            return cls(name = name)

    def update(self, value):
        for attr in value:
            if getattr(self, attr) != value[attr]:
                setattr(self, attr, value[attr])
                print(self.eng_name + " " + attr + " is updated.")
                self.update_date = timezone.now()
        self.save()

    def to_json(self):
        attrlist=[]
        for attr in self.attributes:
            if isinstance(getattr(self, attr), (int, float)):
                attrlist.append('"' + attr + '": ' + str(getattr(self, attr)) + '')
            else:
                attrlist.append('"' + attr + '": "' + str(getattr(self, attr)) + '"')
        return '{' + ', '.join(attrlist) + '}'
