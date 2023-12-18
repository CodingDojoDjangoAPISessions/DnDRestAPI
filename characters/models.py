from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=100)
    char_class = models.CharField(max_length=100)  # 'class' is a reserved keyword in Python
    level = models.IntegerField(default=1)
    exp = models.IntegerField(default=0)
    str_stat = models.IntegerField(db_column='STR', default=3)
    dex_stat = models.IntegerField(db_column='DEX', default=3)
    con_stat = models.IntegerField(db_column='CON', default=3)
    int_stat = models.IntegerField(db_column='INT', default=3)
    wis_stat = models.IntegerField(db_column='WIS', default=3)
    cha_stat = models.IntegerField(db_column='CHA', default=3)
    background = models.TextField(null=True)
