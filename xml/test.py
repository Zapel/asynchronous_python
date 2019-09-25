import xml.etree.cElementTree as ET
import re

def parse_xml(path, filename):
    xml_file = path+filename
    try:
        tree = ET.ElementTree(file=xml_file)
    except IOError as e:
        print('nERROR - cant find file: %sn' % e)
    root = tree.getroot()
    for child_of_root in root:
        return child_of_root.attrib['DETAILSOFPAYMENT']
    raise Exception('Not found!')

def parse_str(str):
    inner_dic = {}
    sum = re.search(r'Сум.\d+.\d+', str).group(0).replace('Сум', '')
    com = re.search(r'Ком.\d+.\d+', str).group(0).replace('Ком', '')
    ref = re.search(r'Реф=.\d+.', str).group(0).replace('Реф=', '')
    inner_dic.update({'sum': sum, 'com': com, 'ref': ref})
    print(inner_dic)
    return inner_dic


if __name__ == "__main__":
    path = '/home/oleg/git/asynchronous_python/xml/xml/'
    filename = 'payoutua19-09-25_18_19_24.xml'

    str = parse_xml(path, filename)
    print(str)
    parse_str(str)

