# from lxml import etree, objectify
import collections
from bs4 import BeautifulSoup

with open('20180728RHIL0.xml', 'rb') as fp:
    soup = BeautifulSoup(fp, "xml")

    for cond in soup.find_all('condition'):
        cond.extract()

    races = soup.findAll('race')

    race_keys = ['id', 'number', 'nomnumber', 'division', 'name', 'mediumname', 'stage', 'distance', 'minweight', 'raisedweight', 'class', 'age', 'grade',
                 'weightcondition', 'owner', 'totalprize', 'first', 'second', 'third', 'time', 'trackcondition', 'timingmethod', 'fastesttime', 'sectionaltime']

    for race_id in races:
        for k in race_keys:
            print("{0} \t:: {1}".format(k, race_id[k]))
            # print("{0} :: {1}".format(race_id.attrs[k], race_id.attrs[v]))

    race_attrs = []
    for attr in soup.race.attrs:
        race_attrs.append(attr)

    # Relevant for processing without comments
    # parser = objectify.makeparser(remove_comments=True)
    # tree = objectify.parse(f, parser=parser)
