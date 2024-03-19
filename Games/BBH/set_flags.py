from Basic.BasicReelsets import Reelsets
from Basic.Utils.PathHandler import BasicPathHandler
import xml.etree.ElementTree as ET

handler = BasicPathHandler()
reels_path = handler.GetResultDataFilePath('BBH', 'reels.xml', 'reels')
print(reels_path)
settings_xml = ET.parse(reels_path).getroot()

settings = Reelsets()
settings.ReadSettings_Xml(settings_xml)

reelsets = settings.GetReelsets()


RTP = 93

sections = ["Base Game",
            "Free Special 0",
            "Free Special 1",
            "Free Special 2",
            "Free Special 3",
            "Free Special 4",
            "Free Special 5",
            "Free Special 6",
            "Free Special 7",
            "Free Special 8",
            "Re-Spin Special 0",
            "Re-Spin Special 1",
            "Re-Spin Special 2",
            "Re-Spin Special 3",
            "Re-Spin Special 4",
            "Re-Spin Special 5",
            "Re-Spin Special 6",
            "Re-Spin Special 7",
            "Re-Spin Special 8",
            "Free No Scatter",
            "Feature Spin Trigger"]

reelset_names    = ['Base Game | Normal',
                    'Base Game | Blocker 1',
                    'Base Game | Blocker 2',

                    'Free Spins | Special Symbol 0 on 1,5 Reels',
                    'Free Spins | Special Symbol 0 on All Reels',
                    'Free Spins | Special Symbol 0 None in Reels',

                    'Free Spins | Special Symbol 1 High Prob on 2,4 Reels',
                    'Free Spins | Special Symbol 1 High Prob on 1,2 Reels',
                    'Free Spins | Special Symbol 1 High Prob on 3,5 Reels',
                    'Free Spins | Special Symbol 1 Low Prob on All Reels',
                    'Free Spins | Special Symbol 1 None in Reels',

                    'Free Spins | Special Symbol 2 High Prob on 1,2,3 Reels',
                    'Free Spins | Special Symbol 2 High Prob on 1,4,5 Reels',
                    'Free Spins | Special Symbol 2 None in Reels',

                    'Free Spins | Special Symbol 3 High Prob on 1,2,3 Reels',
                    'Free Spins | Special Symbol 3 High Prob on 1,4,5 Reels',
                    'Free Spins | Special Symbol 3 None in Reels',

                    'Free Spins | Special Symbol 4 Prob decreases from the Centre to the outermost Reels',
                    'Free Spins | Special Symbol 4 None in Reels',

                    'Free Spins | Special Symbol 5 Prob decreases from the Centre to the outermost Reels',
                    'Free Spins | Special Symbol 5 None in Reels',

                    'Free Spins | Special Symbol 6 High Prob on 1,3 Reels, Lower Prob on Reels 2,5',
                    'Free Spins | Special Symbol 6 None in Reels',

                    'Free Spins | Special Symbol 7 High Prob on 1,3 Reels, Lower Prob on Reels 2,5',
                    'Free Spins | Special Symbol 7 None in Reels',

                    'Free Spins | Special Symbol 8 High Prob on 1,3 Reels, Lower Prob on Reels 2,5',
                    'Free Spins | Special Symbol 8 None in Reels',

                    'Feature Re-Spin Free Spins | Special Symbol 0 High Prob',
                    'Feature Re-Spin Free Spins | Special Symbol 0 Low Prob',

                    'Feature Re-Spin Free Spins | Special Symbol 1 High Prob',
                    'Feature Re-Spin Free Spins | Special Symbol 1 Low Prob',

                    'Feature Re-Spin Free Spins | Special Symbol 2 High Prob',
                    'Feature Re-Spin Free Spins | Special Symbol 2 Low Prob',

                    'Feature Re-Spin Free Spins | Special Symbol 3 High Prob',
                    'Feature Re-Spin Free Spins | Special Symbol 3 Low Prob',

                    'Feature Re-Spin Free Spins | Special Symbol 4 High Prob',
                    'Feature Re-Spin Free Spins | Special Symbol 4 Low Prob',

                    'Feature Re-Spin Free Spins | Special Symbol 5 High Prob',
                    'Feature Re-Spin Free Spins | Special Symbol 5 Low Prob',

                    'Feature Re-Spin Free Spins | Special Symbol 6 High Prob',
                    'Feature Re-Spin Free Spins | Special Symbol 6 Low Prob',

                    'Feature Re-Spin Free Spins | Special Symbol 7 High Prob',
                    'Feature Re-Spin Free Spins | Special Symbol 7 Low Prob',

                    'Feature Re-Spin Free Spins | Special Symbol 8 High Prob',
                    'Feature Re-Spin Free Spins | Special Symbol 8 Low Prob',

                    'Free Spins No Scatters | Normal',
                    'Free Spins No Scatters | No Special Symbols Type 1',
                    'Free Spins No Scatters | No Special Symbols Type 2',
                    'Free Spins No Scatters | No Special Symbols Type 3',
                    'Free Spins No Scatters | No Special Symbols Type 4']

for reelset_index, reelset in enumerate(reelsets):
    section = int(reelset.mainTags['section'])
    reelset.mainTags['reelName'] = '(' + str(reelset_index) + ') ' + reelset_names[reelset_index] + ' | RTP ' + str(RTP)
    reelset.mainTags['sectionName'] = sections[section]
    reelset.mainTags['betsIndices'] = "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25"
    reelset.mainTags['isFortuneBet'] = 'false'
    reelset.mainTags['isRespin'] = 'false'

    if section in [0]:
        reelset.mainTags['isMainCycle'] = 'true'
        reelset.mainTags['isStartScreen'] = 'true'
    else:
        reelset.mainTags['isMainCycle'] = 'false'

    if section in [*range(1, 20)]:
        reelset.mainTags['isFreeSpin'] = 'true'
    else:
        reelset.mainTags['isFreeSpin'] = 'false'

settings.SaveSettings('BBH', 'processed_reels_'+str(RTP)+'.xml', 'Reels')