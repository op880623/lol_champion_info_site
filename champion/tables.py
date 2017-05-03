import django_tables2 as tables
from .models import Champion


class ChampionTable(tables.Table):
    id                   = tables.Column(verbose_name = "id")
    name                 = tables.Column(verbose_name = "名字")
    eng_name             = tables.Column(verbose_name = "英文")
    hp                   = tables.Column(verbose_name = "生命")
    hpperlevel           = tables.Column(verbose_name = "生命成長")
    hpmax                = tables.Column(verbose_name = "最大生命")
    hpregen              = tables.Column(verbose_name = "生命回復")
    hpregenperlevel      = tables.Column(verbose_name = "生命回復成長")
    hpregenmax           = tables.Column(verbose_name = "最大生命回復")
    mp                   = tables.Column(verbose_name = "魔力")
    mpperlevel           = tables.Column(verbose_name = "魔力成長")
    mpmax                = tables.Column(verbose_name = "最大魔力")
    mpregen              = tables.Column(verbose_name = "魔力回復")
    mpregenperlevel      = tables.Column(verbose_name = "魔力回復成長")
    mpregenmax           = tables.Column(verbose_name = "最大魔力回復")
    movespeed            = tables.Column(verbose_name = "移動速度")
    attackdamage         = tables.Column(verbose_name = "物理攻擊")
    attackdamageperlevel = tables.Column(verbose_name = "物理攻擊成長")
    attackdamagemax      = tables.Column(verbose_name = "最大物理攻擊")
    attackspeed          = tables.Column(verbose_name = "攻擊速度")
    attackspeedperlevel  = tables.Column(verbose_name = "攻擊速度成長")
    attackrange          = tables.Column(verbose_name = "攻擊距離")
    armor                = tables.Column(verbose_name = "物理防禦")
    armorperlevel        = tables.Column(verbose_name = "物理防禦成長")
    armormax             = tables.Column(verbose_name = "最大物理防禦")
    spellblock           = tables.Column(verbose_name = "魔法防禦")
    spellblockperlevel   = tables.Column(verbose_name = "魔法防禦成長")
    spellblockmax        = tables.Column(verbose_name = "最大魔法防禦")
    update_date          = tables.Column(verbose_name = "更新日期")

    class Meta:
        attrs = {'class': 'table_style'}
        order_by = 'eng_name'
        empty_text = "There is no champion match requirements."
