from Basic.BasicSettings import Settings
from Basic.Utils.PathHandler import BasicPathHandler
import xml.etree.ElementTree as ET
import numpy as np

handler = BasicPathHandler()
file_name = 'frenzy_all.xml'
reels_path = handler.GetResultDataFilePath('GE', file_name, 'Frenzy_reels_source')
print(reels_path)
settings_xml = ET.parse(reels_path).getroot()

settings = Settings()
settings.ReadSettings_Xml(settings_xml)

reelsets = settings.GetReelsets()

cf_symbols = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19])
cf_symbols_count = np.array([12, 9, 7, 4, 3, 2, 1, 1, 1]) # 3 reel
# cf_symbols_count = np.array([15, 9, 7, 3, 2, 1, 1, 1, 1]) # 2,4 reels
# cf_symbols_count = np.array([20, 6, 5, 3, 2, 1, 1, 1, 1]) # 1,5, all reels


tmp = [[cf_symbols[i] for _ in range(cf_symbols_count[i])] for i in range(len(cf_symbols))]
all_symbols = []
for el in tmp:
    all_symbols += el
all_symbols = np.array(all_symbols)
np.random.shuffle(all_symbols)

temp_symb = 11

for reelset in reelsets:
    for reel in reelset.reels:
        np.random.shuffle(all_symbols)
        count_temp = np.sum(reel.symbols == temp_symb)
        if count_temp == 0:
            continue
        assert count_temp == all_symbols.size, count_temp + all_symbols.size
        temp_indx = 0
        for i, symbol in enumerate(reel.symbols):
            if symbol == temp_symb:
                reel.symbols[i] = all_symbols[temp_indx]
                temp_indx += 1
settings.SaveSettings('GE', file_name, "Frenzy_reels_processed")

