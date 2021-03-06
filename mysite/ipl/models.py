from django.db import models
import csv
from django.shortcuts import render
from json import dumps
# Create your models here.

def bar(request):
    with open('matches.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        win = dict()
        mpy = dict()
        for line in csv_reader:
            mpy[line[1]] = mpy.get(line[1], 0) + 1
            win[line[10]] = win.get(line[10], 0) + 1
        #for i in mpy.keys() and j in mpy.values():
        #  res.append([i,j])
        dataJSON = dumps(mpy.values())
        return render(request, 'js.html', {'data': dataJSON})

class match(models.Model):
    season = models.IntegerField(null=False)
    city = models.CharField(max_length=50)
    winner = models.CharField(max_length=100)
    venue = models.CharField(max_length=250)

    def __unicode__(self):
        return u'%s %s' % (self.season, self.city)
    #def __str__(self):
        #return self.city
