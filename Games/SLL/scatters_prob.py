from Basic.BasicSettings import Settings
from Basic.PathHandler import BasicPathHandler
import xml.etree.ElementTree as ET
from collections import defaultdict

handler = BasicPathHandler()
reels_path = handler.GetResultDataFilePath('SLL', 'sll_orig_reels.xml')
print(reels_path)
settings_xml = ET.parse(reels_path).getroot()

settings = Settings()
settings.ReadSettings_Xml(settings_xml)

base_reelsets = settings.GetReelsets(0)
first_reelset = base_reelsets[0]



for i, reel in enumerate(first_reelset.reels):
    prob_10 = defaultdict(int)
    for j in range(reel.Length()):
        window = reel.TakeWindow(j, 3)
        count_10 = (window == 10).sum()
        if count_10 > 0:
            prob_10[count_10] += 1
    for key, val in prob_10.items():
        print(key, ": ",val, '/', reel.weights.sum())
    print()

