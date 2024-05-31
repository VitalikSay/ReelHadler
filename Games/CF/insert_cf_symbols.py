from Basic.BasicSettings import Settings
from Basic.Utils.PathHandler import BasicPathHandler
import xml.etree.ElementTree as ET
import numpy as np

handler = BasicPathHandler()
source = "3scat_345_source"
reels_path = handler.GetResultDataFilePath('CF', source+'.xml')
print(reels_path)
settings_xml = ET.parse(reels_path).getroot()

settings = Settings()
settings.ReadSettings_Xml(settings_xml)

trigger_reelset = settings.GetReelsets()[0]

SUB_1 = 11
SUB_2 = 35
SUB_3 = 36

# TRIGGER #######################################################################

# replace_reel_1 = {SUB_1: [32, 11, 11, 11, 11, 11, 11, 12, 13, 18],
#                   SUB_2: [(11,11), (12,11), (11,12), (12,13), (14,11)],
#                   SUB_3: [[11,13,12], [12,11,11], [11,14,11]]}
#
# replace_reel_2 = {SUB_1: [31, 11, 11, 11, 11, 11, 11, 12, 13, 17],
#                   SUB_2: [(11,11), (13,11), (11,12), (12,13), (11,14)]}
#
# replace_reel_3 = {SUB_1: [30, 11, 11, 11, 11, 11, 11, 12, 13, 16],
#                   SUB_2: [(11,11), (12,11), (11,12), (13,11), (14,11)]}
#
# replace_reel_4 = {SUB_1: [19, 11, 11, 11, 11, 11, 11, 12, 13, 15],
#                   SUB_2: [(11,11), (12,11), (11,12), (12,13), (11,13)],
#                   SUB_3: [[13,12,11], [13,11,11], [14,11,11]]}
#
# replace_reel_5 = {SUB_1: [18, 11, 11, 11, 11, 11, 11, 12, 13, 14],
#                   SUB_2: [(11,11), (12,11), (11,12), (13,12), (13,11)]}

#################################################################################

# 3scat_2 | 3scat_3 | 3scat_5 ###################################################

# replace_reel_1 = {SUB_1: [32, 11, 11, 11, 11, 11, 11, 12, 13, 18],
#                   SUB_2: [(11,11), (12,11), (11,12), (12,13), (14,11)],
#                   SUB_3: [[11,13,12], [12,11,11], [11,14,11]]}
#
# replace_reel_2 = {SUB_3: [(31, 15, 17),
#  (17, 32, 19),
#  (31, 16, 32),
#  (16, 11, 14),
#  (32, 15, 12),
#  (14, 32, 12),
#  (17, 12, 30),
#  (11, 18, 11)]}
#
# replace_reel_3 = {SUB_3: [(32, 32, 11),
#  (12, 15, 16),
#  (18, 16, 19),
#  (14, 14, 19),
#  (17, 18, 14),
#  (12, 14, 31),
#  (32, 19, 14),
#  (32, 14, 14)]}
#
# replace_reel_4 = {SUB_1: [19, 11, 11, 11, 11, 11, 11, 12, 13, 15],
#                   SUB_2: [(11,11), (12,11), (11,12), (12,13), (11,13)],
#                   SUB_3: [[13,12,11], [13,11,11], [14,11,11]]}
#
# replace_reel_5 = {SUB_3: [(17, 13, 17),
#  (19, 11, 12),
#  (32, 15, 18),
#  (31, 30, 30),
#  (31, 31, 14),
#  (31, 17, 12),
#  (17, 12, 32),
#  (11, 30, 14)]}

#################################################################################

# 3scat_25 | 3scat_34 ###########################################################

# replace_reel_1 = {SUB_1: [32, 11, 11, 11, 11, 11, 11, 12, 13, 18],
#                   SUB_2: [(11,11), (12,11), (11,12), (12,13), (14,11)],
#                   SUB_3: [[11,13,12], [12,11,11], [11,14,11]]}
#
# replace_reel_2 = {SUB_2: [(19, 18),
#  (32, 13),
#  (18, 15),
#  (16, 12),
#  (18, 32),
#  (11, 32),
#  (12, 18),
#  (31, 14)]}
#
# replace_reel_3 = {SUB_1: [11, 12, 13, 14, 15, 16, 17, 18, 19, 30]}
#
# replace_reel_4 = {SUB_2: [(13, 31),
#  (15, 15),
#  (17, 32),
#  (19, 15),
#  (15, 12),
#  (19, 14),
#  (13, 31),
#  (14, 32)]}
#
# replace_reel_5 = {SUB_1: [11, 12, 13, 14, 15, 16, 17, 18, 19, 32]}

#################################################################################

# 3scat_123 | 3scat_345 #########################################################

replace_reel_1 = {SUB_1: [11, 12, 13, 14, 15, 16, 17, 18, 19, 32]}

replace_reel_2 = {SUB_1: [11, 12, 13, 14, 15, 16, 17, 18, 19, 31]}

replace_reel_3 = {SUB_1: [11, 12, 13, 14, 15, 16, 17, 18, 19, 30]}

replace_reel_4 = {SUB_1: [11, 12, 13, 14, 15, 16, 17, 18, 19, 31]}

replace_reel_5 = {SUB_1: [11, 12, 13, 14, 15, 16, 17, 18, 19, 32]}

#################################################################################

reel_replace = [replace_reel_1,
                replace_reel_2,
                replace_reel_3,
                replace_reel_4,
                replace_reel_5]

skip_steps = 0
for i, reel in enumerate(trigger_reelset.reels):
    for j, symbol in enumerate(reel.symbols):
        if skip_steps:
            skip_steps -= 1
            continue
        if symbol == SUB_1:
            reel.symbols[j] = reel_replace[i][SUB_1].pop(np.random.randint(0, len(reel_replace[i][SUB_1])))
        elif symbol == SUB_2:
            rand_pattern = reel_replace[i][SUB_2].pop(np.random.randint(0, len(reel_replace[i][SUB_2])))
            for k in range(len(rand_pattern)):
                reel.symbols[j+k] = rand_pattern[k]
            skip_steps = 1
        elif symbol == SUB_3:
            rand_pattern = reel_replace[i][SUB_3].pop(np.random.randint(0, len(reel_replace[i][SUB_3])))
            for k in range(len(rand_pattern)):
                reel.symbols[j+k] = rand_pattern[k]
            skip_steps = 2



settings.SaveSettings('CF', source+'_processed.xml')

