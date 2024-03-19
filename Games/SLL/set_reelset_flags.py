from Basic.BasicReelsets import Reelsets
from Basic.Utils.PathHandler import BasicPathHandler
import xml.etree.ElementTree as ET

handler = BasicPathHandler()
reels_path = handler.GetResultDataFilePath('SLL', 'all_reels_usual.xml', 'Reels')
print(reels_path)
settings_xml = ET.parse(reels_path).getroot()

settings = Reelsets()
settings.ReadSettings_Xml(settings_xml)

reelsets = settings.GetReelsets()


RTP = 89

bet = {88: 25, 89: 50, 90: 100, 91: 200}
bet_index = {25:0, 50: 1, 100: 2, 200: 3}
sections = ['Base Game',
            'Free Game',
            'Base Re-Spin',
            'Free Re-Spin',
            'Common Feature']
reelset_names_cf = ['Jumbo + FS Trigger',
                    'Cheap Win Symbols 5,6',
                    'Cheap Win Symbols 7,8',
                    'No win',
                    'Only Wilds',
                    'CF Max 3 scatters 1-2-3 reels',
                    'CF Max 3 scatters 3-4-5 reels',
                    'CF Max 3 scatters 2-5 reels',
                    'CF Max 3 scatters 3-4 reels',
                    'CF Max 3 scatters 2 reel',
                    'CF Max 3 scatters 3 reel',
                    'CF Max 3 scatters 5 reel',
                    'CF Max 12 scatters Common trigger',
                    'Jumbo + FS Trigger',
                    'Jumbo 1-2-3',
                    'Jumbo 2-3-4',
                    'Jumbo 3-4-5',
                    'Jumbo 1-2-3-4',
                    'Jumbo 2-3-4-5',
                    'Jumbo 1-2-3-4-5',
                    'Jumbo 1-2-3',
                    'Jumbo 2-3-4',
                    'Jumbo 3-4-5',
                    'Jumbo 1-2-3-4',
                    'Jumbo 2-3-4-5',
                    'Jumbo 1-2-3-4-5',
                    'CF Fictive']
reelset_names_frenzy = ['Jumbo + FS Trigger',
                        'Cheap Win Symbols 5,6',
                        'Cheap Win Symbols 7,8',
                        'No win',
                        'Only Wilds',
                        'Frenzy on 1 Reel',
                        'Frenzy on 2 Reel',
                        'Frenzy on 3 Reel',
                        'Frenzy on 4 Reel',
                        'Frenzy on 5 Reel',
                        'Frenzy on All Reels',
                        'Jumbo + FS Trigger',
                        'Jumbo 1-2-3',
                        'Jumbo 2-3-4',
                        'Jumbo 3-4-5',
                        'Jumbo 1-2-3-4',
                        'Jumbo 2-3-4-5',
                        'Jumbo 1-2-3-4-5',
                        'Jumbo 1-2-3',
                        'Jumbo 2-3-4',
                        'Jumbo 3-4-5',
                        'Jumbo 1-2-3-4',
                        'Jumbo 2-3-4-5',
                        'Jumbo 1-2-3-4-5',
                        'CF Fictive']
start_screen_reelsets = [3]

for reelset_index, reelset in enumerate(reelsets):
    section = int(reelset.mainTags['section'])
    reelset_names = reelset_names_cf if len(reelsets) == len(reelset_names_cf) else reelset_names_frenzy
    reelset.mainTags['reelName'] = '(' + str(reelset_index) + ') ' + sections[section] + ' | ' + reelset_names[reelset_index] + ' | Bet ' + str(bet[RTP]) + ' ' + 'RTP ' + str(RTP)
    reelset.mainTags['sectionName'] = sections[section]
    reelset.mainTags['betsIndices'] = str(bet_index[bet[RTP]])
    reelset.mainTags['isFortuneBet'] = 'false'

    if section in [0, 2]:
        reelset.mainTags['isMainCycle'] = 'true'
    else:
        reelset.mainTags['isMainCycle'] = 'false'

    if section in [1, 3]:
        reelset.mainTags['isFreeSpin'] = 'true'
    else:
        reelset.mainTags['isFreeSpin'] = 'false'

    if section in [2, 3]:
        reelset.mainTags['isRespin'] = 'true'
    else:
        reelset.mainTags['isRespin'] = 'false'

    if reelset_index in start_screen_reelsets:
        reelset.mainTags['isStartScreen'] = 'true'
    else:
        reelset.mainTags['isStartScreen'] = 'false'

    if section == 4:
        reelset.custTags.clear()

settings.SaveSettings('SLL', 'all_reels_frenzy_'+str(RTP)+'.xml', 'Reels')