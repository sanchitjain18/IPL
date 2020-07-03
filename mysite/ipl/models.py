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
        return render(request, '', {'data': dataJSON})

def send_dictionary(request):
    # create data dictionary
    dataDictionary = {
        'hello': 'World',
        'geeks': 'forgeeks',
        'ABC': 123,
        456: 'abc',
        14000605: 1,
        'list': ['geeks', 4, 'geeks'],
        'dictionary': {'you': 'can', 'send': 'anything', 3: 1}
    }
    # dump data
    dataJSON = dumps(dataDictionary)
    return render(request, 'ipl/js.html', {'data': dataJSON})
