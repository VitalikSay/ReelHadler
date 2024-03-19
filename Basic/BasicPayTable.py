import xml.etree.ElementTree as ET
from Basic.Utils.PathHandler import BasicPathHandler
from Basic.Utils.XMLHandler import PrintXML, WriteXMLtoFile, PrettifyXML
import copy
import json

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
        if new_bet == self.for_bet:
            return self

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

    def Get_Symbol_XML_Element_Back_End(self):
        num_of_symbols = list(self.paytable.keys())
        num_of_symbols.sort()
        symbol_paymants = []
        for num_of_symbol in num_of_symbols:
            symbol = ET.Element('Payment')
            symbol.set('numOfSymbols', str(num_of_symbol))
            symbol.set('symbolId', str(self.symbol_id))
            symbol.set('name', self.symbol_name)

            payment = ET.Element('Payments')
            payment.set('Pay', str(self.paytable[num_of_symbol]))
            symbol.append(payment)
            symbol_paymants.append(PrettifyXML(symbol))

        return symbol_paymants

    def PrintSymbolXML(self):
        PrintXML(self.Get_Symbol_XML_Element())


class PayTable:
    def __init__(self):
        self.symbols = []
        self.for_bet = 10

        self.pathHandler = BasicPathHandler()

    def ReadPayTable(self, paytable_xml: ET.Element):
        self.for_bet = int(paytable_xml.attrib['forBet'])
        for symbol_pay in paytable_xml.findall('Payment'):
            symbol = Symbol()
            symbol.ReadSymbol(symbol_pay, self.for_bet)
            self.symbols.append(symbol)


    def Get_PayTable_XML_Element(self):
        paytable = ET.Element('WinLinePayTable')
        paytable.set('forBet', str(self.for_bet))
        for symbol in self.symbols:
            paytable.append(symbol.Get_Symbol_XML_Element())
        return PrettifyXML(paytable)

    def Get_PayTable_XML_Element_Back_End(self):
        paytable = ET.Element('WinLinePayTable')
        paytable.set('forBet', str(self.for_bet))
        for symbol in self.symbols:
            symbol_payments = symbol.Get_Symbol_XML_Element_Back_End()
            for payment in symbol_payments:
                paytable.append(payment)
        return PrettifyXML(paytable)

    def PrintPayTableXML(self):
        PrintXML(self.Get_PayTable_XML_Element())

    def PrintPayTable_BackEnd_XML(self):
        PrintXML(self.Get_PayTable_XML_Element_Back_End())

    def WritePayTable(self, game_name, file_name):
        WriteXMLtoFile(self.Get_PayTable_XML_Element(), self.pathHandler.GetResultDataFilePath(game_name, file_name))

    def ScalePayTable(self, new_bet):
        new_paytable = PayTable()
        new_paytable.for_bet = new_bet
        for symbol in self.symbols:
            new_paytable.symbols.append(symbol.ScaleSymbol(new_bet))
        return new_paytable

    def GetSymbol(self, find_symbol):
        for symbol in self.symbols:
            if symbol.symbol_id == find_symbol:
                return symbol
        return None

    def GetPay(self, symbol, length, bet=10):
        return self.GetSymbol(symbol).ScaleSymbol(bet).paytable[length]

    def PrintPayTable_FrontEnd(self):
        root = self.Get_PayTable_XML_Element_Back_End()
        output = []
        for payment in root.findall('Payment'):
            symbol_id = payment.attrib['symbolId']
            symbols_count = payment.attrib['numOfSymbols']
            amount = payment.find('Payments').attrib['Pay']
            output.append({
                "SymbolId": symbol_id,
                "SymbolsCount": symbols_count,
                "Amount": {
                    "Win": amount,
                    "FreespinsAmount": 0,
                    "RespinsAmount": 0
                }
            })
        print("export const PAYTABLE =", json.dumps(output, indent=4))

# Usage
if __name__ == "__main__":
    pay_table = PayTable()
    pay_table.ReadPayTable('SLL', 'sll_paytable.xml')

    scaled_pay_table = pay_table.ScalePayTable(200)
    scaled_pay_table.WritePayTable('SLL', 'sll_200_paytable.xml')
