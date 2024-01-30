from Basic.BasicSettings import Settings
from Basic.PathHandler import BasicPathHandler
import xml.etree.ElementTree as ET

handler = BasicPathHandler()
reels_path = handler.GetResultDataFilePath('NBN', 'usual_93.xml')
print(reels_path)
settings_xml = ET.parse(reels_path).getroot()

settings = Settings()
settings.ReadSettings_Xml(settings_xml)

base_reelsets = settings.GetReelsets(0)
base_respin_reelsets = settings.GetReelsets(2)

print(base_reelsets[3].FindCombination(r'\d{1,2},\d{1,2},9',
                                              r'\d{1,2},\d{1,2},9',
                                              r'\d{1,2},\d{1,2},9',
                                              r'\d{1,2},\d{1,2},9',
                                              r'\d{1,2},\d{1,2},9', indexes=False))