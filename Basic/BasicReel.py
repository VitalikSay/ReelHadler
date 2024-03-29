import numpy as np
import xml.etree.ElementTree as ET
from typing import Union
import re


class Reel:
    def __init__(self, reel_index: int):
        self.symbols = np.array([])
        self.weights = np.array([])
        self.reel_index = -1

    def TakeWindow(self, index: int, window_height: int):
        if index > self.Length() - window_height:
            res = np.concatenate((self.symbols[index:], self.symbols[:window_height - (self.Length() - index)]))
            return res
        else:
            return self.symbols[index: index + window_height]

    def Length(self):
        return len(self.symbols)

    def ReadReel_Xml(self, reel: ET.Element, reel_index: int = -1):
        self.reel_index = reel_index
        self.symbols = np.array([int(num) for num in reel.find('Symbols').text.split(',')])
        self.weights = np.array([int(num) for num in reel.find('Weights').text.split(',')])

    def ReelElement_Xml(self):
        reel = ET.Element('Reel')
        symbols = ET.SubElement(reel, 'Symbols')
        weights = ET.SubElement(reel, 'Weights')
        symbols.text = ','.join([str(num) for num in self.symbols])
        weights.text = ','.join([str(num) for num in self.weights])
        return reel

    def WeightSumBefore(self, position_index: int):
        return np.sum(self.weights[:position_index])

    def FindWindowIndex(self, re_pattern: str):
        str_symbols = ','.join([str(num) for num in self.symbols])
        matches = re.finditer(re_pattern, str_symbols)
        matches = list(matches)
        if matches:
            return str_symbols[0:matches[np.random.randint(0, len(matches))].start()].count(',')
        return False

    def CalcSymbolProbs(self, window_height=3):
        symbols = list(set(self.symbols))
        res = dict()

        for symbol in symbols:
            symbol_weights = [0 for _ in range(window_height)]
            for i in range(len(self.symbols)):
                window = self.TakeWindow(i, window_height)
                for j in range(window_height):
                    if window[j] == symbol:
                        symbol_weights[j] += self.weights[i]
            symbol_weights = [symbol_weights[k] / np.sum(self.weights) for k in range(window_height)]
            res[symbol] = symbol_weights
        return res

