from Basic.BasicReelsets import Reelsets
from Basic.Utils.PathHandler import BasicPathHandler
from Basic.BasicBoard import Board
from Basic.BasicSlotSettings import SlotSettings
from Basic.BasicWinlines import Winlines
from Basic.BasicPayTable import PayTable
import xml.etree.ElementTree as ET
import numpy as np
from itertools import permutations

handler = BasicPathHandler()
reels_path = handler.GetResultDataFilePath('BBH', 'free.xml', 'free_reelsets')
print(reels_path)
reelsets_xml = ET.parse(reels_path).getroot()
reelsets = Reelsets()
reelsets.ReadSettings_Xml(reelsets_xml)

settings = SlotSettings()
settings.ReadSettings('BBH', 'settings.xml', 'settings')
SCATTER_ID = int(settings.GetGeneralSettings().find('Scatter').attrib['symbolId'])

reelset = reelsets.GetReelsets()[0]
boards = reelset.SymbolProbBoard(3)
scatter_symbol_boards = dict()
for symbol in boards.keys():
    if symbol == SCATTER_ID:
        continue
    scatter_board = Board()
    scatter_board.CreateTable(3, 5, 0, dtype='float64')
    for col in range(len(reelset.reels)):
        for i in range(len(reelset.reels[col].symbols)):
            window = reelset.reels[col].TakeWindow(i, 3)
            for j in range(len(window)):
                if window[j] == SCATTER_ID and symbol not in window:
                    scatter_board.board[j, col] += reelset.reels[col].weights[i]/np.sum(reelset.reels[col].weights)
    scatter_symbol_boards[symbol] = scatter_board

print(boards[0].board)
for symbol, board in boards.items():
    for col in range(5):
        board.board[:, col] = np.array([np.sum(board.board[:, col]) for _ in range(3)])
print(boards[0].board)

def calc_symbol_rtp(symbol_id):
    winlines = Winlines()
    paytbale = PayTable()
    winlines.ReadWinlines(settings.GetWinlinesElemment())
    paytbale.ReadPayTable(settings.GetPaytableElement())

    res = 0
    for winline in winlines.GetWinlines():
        symbol_min_pay = np.min(list(paytbale.GetSymbol(symbol_id).paytable.keys()))
        for winline_length in range(symbol_min_pay, 6):
            for symbol_count in range(1, winline_length+1):
                scatter_count = winline_length - symbol_count
                arr = np.array([symbol_id for _ in range(symbol_count)] + [SCATTER_ID for _ in range(scatter_count)] + [-1 for _ in range(5-symbol_count-scatter_count)])
                perms = list(permutations(arr))
                for perm in perms:
                    inner_res = 1
                    for j in range(len(perm)):
                        if perm[j] == symbol_id:
                            inner_res *= boards[symbol_id].board[winline[j], j]
                        elif perm[j] == SCATTER_ID:
                            inner_res *= scatter_symbol_boards[symbol_id].board[winline[j], j]
                    res += inner_res * paytbale.GetPay(symbol_id, winline_length)
    return res

symbol_rtps = [calc_symbol_rtp(symbol_id) for symbol_id in range(0,9)]
for rtp in symbol_rtps:
    print(rtp, rtp / sum(symbol_rtps) * 100, '%')
print('avg', sum(symbol_rtps) / len(symbol_rtps))
