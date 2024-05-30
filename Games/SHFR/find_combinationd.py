from Basic.BasicReelsets import Reelsets
from Basic.Utils.PathHandler import BasicPathHandler
import xml.etree.ElementTree as ET
import numpy as np


handler = BasicPathHandler()
reels_path = handler.GetResultDataFilePath('SHFR', 'usual_95.xml', 'reels')
settings_xml = ET.parse(reels_path).getroot()

reels = Reelsets()
reels.ReadSettings_Xml(settings_xml)

base_reelsets = reels.GetReelsets(0)

# for reelset in base_reelsets:
#     print(reelset.mainTags['reelName'])
#     print(len(reelset.reels))

main_symbol = 0
sp_symbols = [13, 12, 2, 1]

find_board = [
    [main_symbol, main_symbol, main_symbol, main_symbol+1, main_symbol+1],
    [main_symbol+1, main_symbol+1, main_symbol+1, main_symbol+1, main_symbol+1],
    [main_symbol+1, main_symbol+1, main_symbol+1, main_symbol+1, main_symbol+1],
    [main_symbol+1, main_symbol+1, main_symbol+1, main_symbol+1, main_symbol+1]
]

second_rand = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

rand_board = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

reelset = base_reelsets[16]

for i, reel in enumerate(reelset.reels):
    row = i % 4
    col = i // 4
    symbol_to_find = find_board[row][col]
    index = 0
    if symbol_to_find != main_symbol:
        for j, symbol in enumerate(reel.symbols):
            if (symbol not in sp_symbols) and (reel.weights[j] != 0) and (symbol != main_symbol):
                index = j
    else:
        index = np.where(reel.symbols == main_symbol)[0][0]

    rand_board[row][col] = reel.WeightSumBefore(index)

print()
print([int(n) for n in reelset.mainTags['range'].split()][0], end=',')
print(*rand_board[0],*rand_board[1],*rand_board[2],*rand_board[3], sep=",",end=",")
print(*rand_board[0][3:],*rand_board[1],*rand_board[2],*rand_board[3], sep=",")