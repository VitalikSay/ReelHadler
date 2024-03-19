from Basic.BasicReelsets import Reelsets
from Basic.Utils.PathHandler import BasicPathHandler
import xml.etree.ElementTree as ET
from collections import defaultdict
import numpy as np

handler = BasicPathHandler()
reels_path = handler.GetResultDataFilePath('TUNA', 'bier_reels.xml')
print(reels_path)
settings_xml = ET.parse(reels_path).getroot()

settings = Reelsets()
settings.ReadSettings_Xml(settings_xml)

reelsets = settings.GetReelsets()

# bier += 2
# collection = 22
# wild = 23
# picture = 0-5
# royals = 18-20


for i, reelset in enumerate(reelsets):
    print(reelset.mainTags['reelName'])
    for j, reel in enumerate(reelset.reels):
        common_indexes = []
        for k, symbol in enumerate(reel.symbols):
            if symbol in range(4, 16):
                reel.symbols[k] += 2
            elif symbol in [0,1,2,3,16,17,18,19,20]:
                common_indexes.append(k)
                reel.symbols[k] = np.random.choice([0,1,2,3,4,5,18,19,20])
        wild_indexes = np.random.choice(common_indexes, 2, replace=False)
        while(wild_indexes[1] in [wild_indexes[0]+l for l in range(-3,4)]):
            wild_indexes[1] = np.random.choice(common_indexes)
        for p in wild_indexes:
            reel.symbols[p] = 23
settings.SaveSettings('TUNA', 'Free_spin_reels.xml')


