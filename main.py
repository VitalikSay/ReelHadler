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

print(base_reelsets[14].FindCombination(r'(1[1-9]|2[0-9]|3[0-2]),(1[1-9]|2[0-9]|3[0-2]),(1[1-9]|2[0-9]|3[0-2])',
                                              r'(1[1-9]|2[0-9]|3[0-2]),(1[1-9]|2[0-9]|3[0-2]),(10|[0-9])',
                                              r'(1[1-9]|2[0-9]|3[0-2]),(1[1-9]|2[0-9]|3[0-2]),(10|[0-9])',
                                              r'(1[1-9]|2[0-9]|3[0-2]),(1[1-9]|2[0-9]|3[0-2]),(1[1-9]|2[0-9]|3[0-2])',
                                              r'(1[1-9]|2[0-9]|3[0-2]),(1[1-9]|2[0-9]|3[0-2]),(10|[0-9])', indexes=False))
print(base_reelsets[14].mainTags['range'])