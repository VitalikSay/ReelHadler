from Basic.BasicReelsets import Reelsets
from Basic.Utils.PathHandler import BasicPathHandler
import xml.etree.ElementTree as ET


RTP = 93



handler = BasicPathHandler()
reels_path = handler.GetResultDataFilePath('BBH', 'source_reels_' + str(RTP) + '.xml', 'reels_wisconsin')
print(reels_path)
settings_xml = ET.parse(reels_path).getroot()

settings = Reelsets()
settings.ReadSettings_Xml(settings_xml)

reelsets = settings.GetReelsets()




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

reelset_names    = ['Base Game | Normal No Scat',
                    'Base Game | Blocker, Scat on Reels 2,4',
                    'Base Game | Blocker, Scat on Reels 1,3',
                    'Base Game | Blocker, Scat on Reels 3,4',
                    'Base Game | Only Symbol 0 x5',
                    'Base Game | No Win No Scat',
                    'Base Game | No Win 3 Scat',
                    'Base Game | No Win 4 Scat',
                    'Base Game | No Win 5 Scat',

                    'Free Spins | Special Symbol 0 on 1,3 Reels',
                    'Free Spins | Special Symbol 0 on 2,4 Reels',
                    'Free Spins | Special Symbol 0 on 2,3 Reels',
                    'Free Spins | Special Symbol 0 Regular Wins',
                    'Free Spins | Special Symbol 0 No Win 3 Scat',

                    'Free Spins | Special Symbol 1 on 1,3 Reels',
                    'Free Spins | Special Symbol 1 on 2,4 Reels',
                    'Free Spins | Special Symbol 1 on 2,3 Reels',
                    'Free Spins | Special Symbol 1 Regular Wins',
                    'Free Spins | Special Symbol 1 No Win 3 Scat',

                    'Free Spins | Special Symbol 2 on Reels 1,3,4',
                    'Free Spins | Special Symbol 2 on Reels 2,3,4',
                    'Free Spins | Special Symbol 2 on Reels 1,3,5',
                    'Free Spins | Special Symbol 2 Regular Wins',
                    'Free Spins | Special Symbol 2 No Win 3 Scat',

                    'Free Spins | Special Symbol 3 on Reels 1,3,4',
                    'Free Spins | Special Symbol 3 on Reels 2,3,4',
                    'Free Spins | Special Symbol 3 on Reels 1,3,5',
                    'Free Spins | Special Symbol 3 Regular Wins',
                    'Free Spins | Special Symbol 3 No Win 3 Scat',

                    'Free Spins | Special Symbol 4 on Reels 1,3,4,5',
                    'Free Spins | Special Symbol 4 on Reels 2,3,4,5',
                    'Free Spins | Special Symbol 4 Regular Wins',
                    'Free Spins | Special Symbol 4 No Win 3 Scat',

                    'Free Spins | Special Symbol 5 on Reels 1,3,4,5',
                    'Free Spins | Special Symbol 5 on Reels 2,3,4,5',
                    'Free Spins | Special Symbol 5 Regular Wins',
                    'Free Spins | Special Symbol 5 No Win 3 Scat',

                    'Free Spins | Special Symbol 6 on Reels 1,3,4,5',
                    'Free Spins | Special Symbol 6 on Reels 2,3,4,5',
                    'Free Spins | Special Symbol 6 Regular Wins',
                    'Free Spins | Special Symbol 6 No Win 3 Scat',

                    'Free Spins | Special Symbol 7 on Reels 1,3,4,5',
                    'Free Spins | Special Symbol 7 on Reels 2,3,4,5',
                    'Free Spins | Special Symbol 7 Regular Wins',
                    'Free Spins | Special Symbol 7 No Win 3 Scat',

                    'Free Spins | Special Symbol 8 on Reels 1,3,4,5',
                    'Free Spins | Special Symbol 8 on Reels 2,3,4,5',
                    'Free Spins | Special Symbol 8 Regular Wins',
                    'Free Spins | Special Symbol 8 No Win 3 Scat',

                    'Feature Re-Spin Free Spins | Special Symbol 0 High on Reels 2,3',
                    'Feature Re-Spin Free Spins | Special Symbol 0 High on Reels 1,4',
                    'Feature Re-Spin Free Spins | Special Symbol 0 Low on Reels 1,4',
                    'Feature Re-Spin Free Spins | Special Symbol 0 Low on Reels 2,5',
                    'Feature Re-Spin Free Spins | Special Symbol 0 No Win 3 Scat',

                    'Feature Re-Spin Free Spins | Special Symbol 1 High on Reels 2,3',
                    'Feature Re-Spin Free Spins | Special Symbol 1 High on Reels 1,4',
                    'Feature Re-Spin Free Spins | Special Symbol 1 Low on Reels 1,4',
                    'Feature Re-Spin Free Spins | Special Symbol 1 Low on Reels 2,5',
                    'Feature Re-Spin Free Spins | Special Symbol 1 No Win 3 Scat',

                    'Feature Re-Spin Free Spins | Special Symbol 2 High on Reels 2,3',
                    'Feature Re-Spin Free Spins | Special Symbol 2 High on Reels 1,4',
                    'Feature Re-Spin Free Spins | Special Symbol 2 Low on Reels 1,4',
                    'Feature Re-Spin Free Spins | Special Symbol 2 Low on Reels 2,5',
                    'Feature Re-Spin Free Spins | Special Symbol 2 No Win 3 Scat',

                    'Feature Re-Spin Free Spins | Special Symbol 3 High on Reels 2,3',
                    'Feature Re-Spin Free Spins | Special Symbol 3 High on Reels 1,4',
                    'Feature Re-Spin Free Spins | Special Symbol 3 Low on Reels 1,4',
                    'Feature Re-Spin Free Spins | Special Symbol 3 Low on Reels 2,5',
                    'Feature Re-Spin Free Spins | Special Symbol 3 No Win 3 Scat',

                    'Feature Re-Spin Free Spins | Special Symbol 4 High on Reels 2,4,5',
                    'Feature Re-Spin Free Spins | Special Symbol 4 Low on Reels 1,3',
                    'Feature Re-Spin Free Spins | Special Symbol 4 No Win 3 Scat',

                    'Feature Re-Spin Free Spins | Special Symbol 5 High on Reels 2,4,5',
                    'Feature Re-Spin Free Spins | Special Symbol 5 Low on Reels 1,3',
                    'Feature Re-Spin Free Spins | Special Symbol 5 No Win 3 Scat',

                    'Feature Re-Spin Free Spins | Special Symbol 6 High on Reels 1,2,3,4',
                    'Feature Re-Spin Free Spins | Special Symbol 6 Low on Reels 1,3,5',
                    'Feature Re-Spin Free Spins | Special Symbol 6 No Win 3 Scat',

                    'Feature Re-Spin Free Spins | Special Symbol 7 High on Reels 1,2,3,4',
                    'Feature Re-Spin Free Spins | Special Symbol 7 Low on Reels 1,3,5',
                    'Feature Re-Spin Free Spins | Special Symbol 7 No Win 3 Scat',

                    'Feature Re-Spin Free Spins | Special Symbol 8 High on Reels 1,2,3,4',
                    'Feature Re-Spin Free Spins | Special Symbol 8 Low on Reels 1,3,5',
                    'Feature Re-Spin Free Spins | Special Symbol 8 No Win 3 Scat',

                    'Free Spins No Scatters | Normal',
                    'Free Spins No Scatters | Normal 2',
                    ]

for reelset_index, reelset in enumerate(reelsets):
    section = int(reelset.mainTags['section'])
    reelset.mainTags['reelName'] = '(' + str(reelset_index) + ') ' + reelset_names[reelset_index] + ' | Wisconsin RTP ' + str(RTP)
    reelset.mainTags['sectionName'] = sections[section]
    reelset.mainTags['betsIndices'] = "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14"
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

settings.SaveSettings('BBH', 'processed_reels_'+str(RTP)+'.xml', 'reels_wisconsin')