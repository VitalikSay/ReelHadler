from Basic.BasicSettings import Settings
from Basic.Utils.PathHandler import BasicPathHandler
import xml.etree.ElementTree as ET

handler = BasicPathHandler()
reels_path = handler.GetResultDataFilePath('SLL', 'cf_reels_nbn.xml')
print(reels_path)
settings_xml = ET.parse(reels_path).getroot()

settings = Settings()
settings.ReadSettings_Xml(settings_xml)

base_reelsets = settings.GetReelsets()


for reelset in base_reelsets:
    for reel in reelset.reels:
        for i, symbol in enumerate(reel.symbols):
            if symbol > 10:
                reel.symbols[i] = symbol + 3

settings.SaveSettings("SLL", 'cf_reels_result.xml')

