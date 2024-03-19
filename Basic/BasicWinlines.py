import xml.etree.ElementTree as ET
from Basic.Utils.PathHandler import BasicPathHandler
from Basic.Utils.XMLHandler import PrintXML, WriteXMLtoFile, PrettifyXML
import numpy as np


class Winlines:
    def __init__(self):
        self.winlines = np.array([])

    def ReadWinlines(self, winlines_xml: ET.Element):
        lines = []
        for i, winline_el in enumerate(winlines_xml.findall('Line')):
            index = winline_el.attrib['index']
            assert index != i, ValueError("Wrong Lines Sequence !!! i="+str(i)+" index="+str(index))
            line = [int(num) for num in winline_el.attrib['config'].split(',')]
            lines.append(np.array(line))
        self.winlines = np.array(lines)

    def GetWinlines(self):
        return self.winlines

if __name__ == "__main__":
    pass