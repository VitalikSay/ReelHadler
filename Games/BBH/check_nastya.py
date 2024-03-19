from Basic.BasicReelsets import Reelsets
from Basic.Utils.PathHandler import BasicPathHandler
from Basic.BasicBoard import Board
from Basic.BasicSlotSettings import SlotSettings
from Basic.BasicWinlines import Winlines
from Basic.BasicPayTable import PayTable
import xml.etree.ElementTree as ET
import numpy as np
from itertools import permutations
from collections import defaultdict

handler = BasicPathHandler()
reels_path = handler.GetResultDataFilePath('BBH', 'cf_reels.xml', 'free_reelsets')
print(reels_path)
reelsets_xml = ET.parse(reels_path).getroot()
reelsets = Reelsets()
reelsets.ReadSettings_Xml(reelsets_xml)


for reelset in reelsets.GetReelsets():
    weight_symb = defaultdict(int)
    for i, symbol in enumerate(reelset.reels[0].symbols):
        if reelset.reels[0].weights[i] != 0:
            weight_symb[symbol] += reelset.reels[0].weights[i]
    print(reelset.mainTags['reelName'])
    for key, val in weight_symb.items():
        print(key, " : ", val)