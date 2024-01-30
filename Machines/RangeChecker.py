from Basic.BasicSettings import Settings
import xml.etree.ElementTree as ET

xml_head = ET.parse(r'D:\Games Files\Games Files\#1 SPBR DIGITAL\#20 Bier Haus Frenzy\Reels\reels_usual_90.xml').getroot()
settings = Settings()
settings.ReadSettings_Xml(xml_head)
settings.CheckRanges()
settings.SaveSettings()
