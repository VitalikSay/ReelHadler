import xml.etree.ElementTree as ET
from Basic.Utils.PathHandler import BasicPathHandler
from Basic.Utils.XMLHandler import PrintXML, WriteXMLtoFile, PrettifyXML
import numpy as np

class Board:
    def __init__(self):
        self.board = np.array([])

    def CreateTable_xml(self, board_xml: ET.Element, default_value=-1, dtype='int32'):
        self.board = np.full((int(board_xml.attrib['height']), int(board_xml.attrib['width'])), default_value, dtype=dtype)

    def CreateTable(self, height, width, default_value=-1, dtype='int32'):
        self.board = np.full((height, width), default_value, dtype=dtype)

    def SetSymbol(self, row, col, value):
        self.board[row, col] = value

    def GetSymbol(self, row, col):
        return self.board[row, col]

if __name__ == "__main__":
    board = Board()
    board.CreateTable(3,5,3)
    print(board.board)