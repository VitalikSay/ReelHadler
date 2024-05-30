from Basic.BasicReelsets import Reelsets
from Basic.Utils.PathHandler import BasicPathHandler
import xml.etree.ElementTree as ET
import numpy as np


handler = BasicPathHandler()
reels_path = handler.GetResultDataFilePath('IW', 'IW_reels_94.xml')
settings_xml = ET.parse(reels_path).getroot()

reels = Reelsets()
reels.ReadSettings_Xml(settings_xml)

base_reelsets = reels.GetReelsets(0)
free_reelsets = reels.GetReelsets(2)

sp_symbols = [*range(13, 19)]

def special_symbol_here(window, sp_symbols):
    for sp_symbol in sp_symbols:
        if sp_symbol in window:
            return True
    return False

for i, reelset in enumerate(free_reelsets):
    rang = [int(n) for n in reelset.mainTags['range'].split()]
    print(reelset.mainTags.get("reelName"), " | weight ", rang[1] - rang[0] + 1)
    for j, reel in enumerate(reelset.reels):
        clover_weight = 0
        for k in range(len(reel.symbols)):
            window = reel.TakeWindow(k, 4)
            if special_symbol_here(window, sp_symbols):
                clover_weight += reel.weights[k]
        print("    Reel", j, clover_weight / np.sum(reel.weights))

