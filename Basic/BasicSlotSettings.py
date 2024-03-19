import xml.etree.ElementTree as ET
from Basic.Utils.PathHandler import BasicPathHandler
from Basic.BasicWinlines import Winlines
from Basic.BasicPayTable import PayTable
from Basic.BasicBoard import Board
from Basic.Utils.XMLHandler import PrintXML, WriteXMLtoFile, PrettifyXML
import numpy as np

class SlotSettings:
    def __init__(self):
        self.main_element = ET.Element
        self.path_handler = BasicPathHandler()

    def ReadSettings(self, game_name, file_name, *inner_folders):
        self.main_element = ET.parse(self.path_handler.GetResultDataFilePath(game_name, file_name, *inner_folders)).getroot()

    def GetSimulationSettings(self):
        return self.main_element.find('simulationSettings')

    def GetGeneralSettings(self):
        return self.main_element.find('generalSettings')

    def GetPaytableElement(self):
        return self.GetGeneralSettings().find('WinLinePayTable')

    def GetWinlinesElemment(self):
        return self.GetGeneralSettings().find('WinLines')

if __name__ == "__main__":
    settings = SlotSettings()
    settings.ReadSettings('BBH', 'settings.xml', 'settings')
    # print(settings.GetPaytableElement().attrib['forBet'])

    winlines = Winlines()
    winlines.ReadWinlines(settings.GetWinlinesElemment())
    # print(winlines.winlines)

    paytable = PayTable()
    paytable.ReadPayTable(settings.GetPaytableElement())
    # print(paytable.GetPay(0, 5, 10))

    board = Board()
    board.CreateTable_xml(settings.GetGeneralSettings().find('boardSize'))
    # print(board.board)
