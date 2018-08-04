# from lxml import etree, objectify
import collections
from bs4 import BeautifulSoup
import numpy as np
with open('20180721RAND0.xml', 'rb') as fp:
    soup = BeautifulSoup(fp, "xml")

    for cond in soup.find_all('condition'):

        cond.extract()

    # races = soup.findAll('race')

    # race_keys = ['id', 'number', 'nomnumber', 'division', 'name', 'mediumname', 'stage', 'distance', 'minweight', 'raisedweight', 'class', 'age', 'grade',
    #              'weightcondition', 'owner', 'totalprize', 'first', 'second', 'third', 'time', 'trackcondition', 'timingmethod', 'fastesttime', 'sectionaltime']

    # for race_id in races:
    #     for k in race_keys:
    #         print("{0} \t:: {1}".format(k, race_id[k]))
    #         # print("{0} :: {1}".format(race_id.attrs[k], race_id.attrs[v]))

    # Discover what attrs are keys in the element
    # race_attrs = []
    # for attr in soup.race.attrs:
    #     race_attrs.append(attr)
    def gen_attr(element):
        for e in soup.find_all(element):
            yield e.attrs

    raceAttr = list(gen_attr('race'))
    npraceAttr = np.array(raceAttr)
    a = raceAttr[0]
    print(a)

    # attrKey(race)
    # noms = soup.findAll('nomination')
    # nom_attrs = []
    # for attr in soup.nomination.attrs:
    #     nom_attrs.append(attr)

    nom_keys = ['number', 'saddlecloth', 'horse', 'id', 'idnumber', 'regnumber', 'blinkers', 'trainernumber', 'trainersurname', 'trainerfirstname', 'trainertrack', 'rsbtrainername', 'jockeynumber', 'jockeysurname', 'jockeyfirstname', 'barrier', 'weight', 'rating', 'description', 'colours', 'owners',
                'dob', 'age', 'sex', 'career', 'thistrack', 'thisdistance', 'goodtrack', 'heavytrack', 'slowtrack', 'deadtrack', 'fasttrack', 'firstup', 'secondup', 'mindistancewin', 'maxdistancewin', 'finished', 'weightvariation', 'variedweight', 'decimalmargin', 'penalty', 'pricestarting', 'bonusindicator']
    # nomination = soup.race.findChildren('nomination', recursive=False)
    # print(noms)

    # nomination_keys = []
    # for k in nomination.attrs:
    #     print(k)
    #     nomination_keys.append(attr)

    # print(list(nomination_keys))

    # Relevant for processing without comments
    # parser = objectify.makeparser(remove_comments=True)
    # tree = objectify.parse(f, parser=parser)
