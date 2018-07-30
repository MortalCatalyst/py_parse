# from lxml import etree, objectify
import collections
from bs4 import BeautifulSoup

with open('20180728RHIL0.xml', 'rb') as fp:
    soup = BeautifulSoup(fp, "xml")
    # data = f.read()

    for cond in soup.find_all('condition'):
        cond.extract()

    print(soup)

    # parser = etree.XMLParser(remove_comments=True)
    # tree = etree.parse(data, parser=parser)
    # tree = etree.parse(data)
    # root = etree.fromstring(data)
    # children = list(root)
    # # print(root[0].child.getnext())
    # for child in root:
    #     print(root[0].child.getnext())
    # samples = root.xpath('//meeting/race')
    # child_dicts = collections.namedtuple(children)
    # print(child_dicts)

    # parser = objectify.makeparser(remove_comments=True)
    # tree = objectify.parse(f, parser=parser)

    # # print(tree)
    # def recursive_dict(element):
    #     return element.tag, dict(map(recursive_dict, element)) or element.text

    # data_dict = recursive_dict(tree.getroot())

    # print(data_dict)
    # races = soup.findAll("race").findChildren()
    # races = soup.findAll(lambda tag: tag.name ==
    #                      "race" and tag.name == "nomination")
    # races = soup.findAll(["race", "nomination"])
    # print(races[0])
    # a = []
    # for item in soup.findAll("race"):
    #     if item.find("condition") not in item:
    #         a.append(item)
    #         continue

    # # print(a)
    # no_condition = list(
    #     filter(lambda x: x == "condition", races))
    # print(no_condition)

    # outfile = [cond.extract() for cond in soup.find_all("condition")]
    # for cond in soup.find_all('condition'):
    #     print(cond.extract())
    # print(outfile)
