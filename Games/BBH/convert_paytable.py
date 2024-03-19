from Basic.BasicReelsets import Reelsets
from Basic.Utils.PathHandler import BasicPathHandler
from Basic.BasicBoard import Board
from Basic.BasicSlotSettings import SlotSettings
from Basic.BasicWinlines import Winlines
from Basic.BasicPayTable import PayTable
import xml.etree.ElementTree as ET
import numpy as np
from itertools import permutations

handler = BasicPathHandler()

settings = SlotSettings()
settings.ReadSettings('BBH', 'settings.xml', 'settings')

paytable = PayTable()
paytable.ReadPayTable(settings.GetPaytableElement())

res = paytable.PrintPayTable_FrontEnd()