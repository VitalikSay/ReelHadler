import numpy as np
import xml.etree.ElementTree as ET
from Basic.BasicReel import Reel
from Basic.BasicBoard import Board


class Reelset:
    def __init__(self, reelset_index: int):
        self.reelset_index = reelset_index
        self.reels = list()
        self.mainTags = {'reelName': 'Test Name',
                         'range': '0 0',
                         'section': '-1',
                         'sectionName': 'Test Section',
                         'isMainCycle': 'false',
                         'isFreeSpin': 'false',
                         'isRespin': 'false',
                         'isStartScreen': 'false',
                         'betsIndices': '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25'}
        self.custTags = dict()

    def ReadReelset_Xml(self, reelset: ET.Element, reelset_index: int):
        self.reelset_index = reelset_index
        self._ReadTags_Xml(reelset)
        self._ReadReels_Xml(reelset)

    def ElementReelset_Xml(self):
        reelset = ET.Element('Reelset')
        for tag_name, tag_value in self.mainTags.items():
            reelset.set(tag_name, tag_value)
        for tag_name, tag_value in self.custTags.items():
            reelset.set(tag_name, tag_value)
        for i, reel in enumerate(self.reels):
            reelset.append(reel.ReelElement_Xml())
        return reelset

    def _ReadTags_Xml(self, reelset: ET.Element):
        for tag_name, tag_value in reelset.attrib.items():
            if tag_name in self.mainTags.keys():
                self.mainTags[tag_name] = tag_value
            else:
                self.custTags[tag_name] = tag_value

    def _ReadReels_Xml(self, reelset: ET.Element):
        for i, reel in enumerate(reelset):
            cur_reel = Reel(i)
            cur_reel.ReadReel_Xml(reel, i)
            self.reels.append(cur_reel)

    def FindCombination(self, *re_patterns, indexes=True):
        combination_indexes = []
        for i, reel in enumerate(self.reels):
            combination_indexes.append(reel.FindWindowIndex(re_patterns[i]))
        assert all(re_patterns), ValueError("No such patterns")
        if not indexes:
            return [reel.WeightSumBefore(combination_indexes[i]) for i, reel in enumerate(self.reels)]
        return combination_indexes

    def SymbolProbBoard(self, window_height=3):
        res = dict()

        for i, reel in enumerate(self.reels):
            reel_res = reel.CalcSymbolProbs(window_height)
            for symbol, probs in reel_res.items():
                if symbol not in res:
                    board = Board()
                    board.CreateTable(window_height, len(self.reels), default_value=0, dtype='float64')
                    res[symbol] = board
                for j in range(len(probs)):
                    res[symbol].SetSymbol(j, i, probs[j])
        return res


