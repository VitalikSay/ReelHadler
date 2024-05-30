from Basic.BasicReelsets import Reelsets
from Basic.Utils.PathHandler import BasicPathHandler
import xml.etree.ElementTree as ET

handler = BasicPathHandler()
reels_path = handler.GetResultDataFilePath('SS', 'reels_93.xml')
print(reels_path)
settings_xml = ET.parse(reels_path).getroot()

settings = Reelsets()
settings.ReadSettings_Xml(settings_xml)

reelsets = settings.GetReelsets()


RTP = 93

sections = ["Base Game"]

reelset_names    = ['No Win | Full Blank',
                    'No Win | Near Miss Blank-Digit-Blank',
                    'No Win | Near Miss Blank-Blank-Digit',
                    'No Win | Near Miss Blank-Digit-Digit',
                    'No Win | Near Miss Blank-Mult-Blank',
                    'Multiplier | Mult on 2 Reel + Digit on 1 Reel',
                    'Multiplier | Mult on 1 Reel',
                    'Multiplier | Mult on 1 Reel + Digit on 2 Reel',
                    'Multiplier | Two Mults',
                    'Digit | Digit on 1 Reel',
                    'Digit | Digit on 1,2 Reels',
                    'Digit | Digit on 1,2,3 Reels',
                    'Digit | x100,x150,x200,x250 win',
                    'Digit | x188 win',
                    'Digit | x999 win']

for reelset_index, reelset in enumerate(reelsets):
    section = int(reelset.mainTags['section'])
    reelset.mainTags['reelName'] = '(' + str(reelset_index) + ') ' + reelset_names[reelset_index] + ' | RTP ' + str(RTP)
    reelset.mainTags['sectionName'] = sections[section]
    reelset.mainTags['betsIndices'] = "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25"
    reelset.mainTags['isRespin'] = 'false'

    if reelset_index < 5:
        reelset.mainTags['isStartScreen'] = 'true'
    else:
        reelset.mainTags['isStartScreen'] = 'false'
    reelset.mainTags['isMainCycle'] = 'true'
    reelset.mainTags['isFreeSpin'] = 'false'
    reelset.mainTags['isFortuneBet'] = 'false'

settings.SaveSettings('SS', 'processed_reels_'+str(RTP)+'.xml')