import xml.etree.ElementTree as ET
from xml.dom import minidom

def WriteXMLtoFile(element, file_path):
    with open(file_path, 'w') as f:
        f.write(ET.tostring(element, encoding='unicode', method='xml'))

def PrintXML(element):
    print(ET.tostring(element).decode())

def PrettifyXML(root_elem: ET.Element):
    for elem in root_elem.iter():
        if elem.text:
            elem.text = elem.text.strip()
        if elem.tail:
            elem.tail = elem.tail.strip()
    rough_string = ET.tostring(root_elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return ET.fromstring(reparsed.toprettyxml(indent="    "))