import xml.etree.ElementTree as ET
from Basic.Utils.PathHandler import BasicPathHandler
from Utils.XMLHandler import PrintXML, WriteXMLtoFile, PrettifyXML
import copy

class Symbol:
    def __init__(self):
        self.symbol_id = -1
        self.symbol_name = 'Test_Name'
        self.paytable = {}
        self.for_bet = 10
    def Copy(self):
        new = Symbol()
        new.symbol_id = copy.deepcopy(self.symbol_id)
        new.symbol_name = copy.deepcopy(self.symbol_name)
        new.paytable = copy.deepcopy(self.paytable)
        new.for_bet = copy.deepcopy(self.for_bet)
        return new

    def ReadSymbol(self, xml_element, for_bet=10):
        self.symbol_id = int(xml_element.attrib['symbolId'])
        self.symbol_name = xml_element.attrib['name']
        self.for_bet = for_bet
        for payment in xml_element.findall('Payments'):
            self.paytable[int(payment.attrib['numOfSymbols'])] = int(payment.attrib['Pay'])

    def ScaleSymbol(self, new_bet):
        new_symbol = self.Copy()

        for count, pay in new_symbol.paytable.items():
            new_pay = pay / new_symbol.for_bet * new_bet
            if new_pay % 1 != 0:
                print('Double pay:', new_pay)
                new_pay = input('New pay: ')
            new_symbol.paytable[count] = int(new_pay)
        new_symbol.for_bet = new_bet
        return new_symbol

    def Get_Symbol_XML_Element(self):
        symbol = ET.Element('Payment')
        symbol.set('symbolId', str(self.symbol_id))
        symbol.set('name', self.symbol_name)
        for pay in sorted(list(self.paytable.keys())):
            payment = ET.Element('Payments')
            payment.set('numOfSymbols', str(pay))
            payment.set('Pay', str(self.paytable[pay]))
            symbol.append(payment)
        return PrettifyXML(symbol)

    def PrintSymbolXML(self):
        PrintXML(self.Get_Symbol_XML_Element())


class PayTable:
    def __init__(self):
        self.symbols = []
        self.for_bet = 10

        self.pathHandler = BasicPathHandler()

    def ReadPayTable(self, game_name, file_name):
        tree = ET.parse(self.pathHandler.GetResultDataFilePath(game_name, file_name))
        root = tree.getroot()
        self.for_bet = int(root.attrib['forBet'])
        for symbol_pay in root.findall('Payment'):
            symbol = Symbol()
            symbol.ReadSymbol(symbol_pay, self.for_bet)
            self.symbols.append(symbol)


    def Get_PayTable_XML_Element(self):
        paytable = ET.Element('WinLinePayTable')
        paytable.set('forBet', str(self.for_bet))
        for symbol in self.symbols:
            paytable.append(symbol.Get_Symbol_XML_Element())
        return PrettifyXML(paytable)

    def PrintPayTableXML(self):
        PrintXML(self.Get_PayTable_XML_Element())

    def WritePayTable(self, game_name, file_name):
        WriteXMLtoFile(self.Get_PayTable_XML_Element(), self.pathHandler.GetResultDataFilePath(game_name, file_name))

    def ScalePayTable(self, new_bet):
        new_paytable = PayTable()
        new_paytable.for_bet = new_bet
        for symbol in self.symbols:
            new_paytable.symbols.append(symbol.ScaleSymbol(new_bet))
        return new_paytable

# Usage
pay_table = PayTable()
pay_table.ReadPayTable('SLL', 'sll_paytable.xml')

scaled_pay_table = pay_table.ScalePayTable(200)
scaled_pay_table.WritePayTable('SLL', 'sll_200_paytable.xml')
