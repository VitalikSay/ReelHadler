import numpy as np
import xml.etree.ElementTree as ET
from xml.dom import minidom
from Basic.BasicReel import Reel
from Basic.BasicReelset import Reelset
from Basic.PathHandler import BasicPathHandler


class Settings:
    def __init__(self):
        self.mainTags = {'GameNameShort': 'Test',
                         'GameNameFull': 'Test',
                         'VersionName': 'Test',
                         'id': 'Test'}
        self.custTags = dict()
        self.reelsets = list()
        self.section_names = []
        self.path_handler = BasicPathHandler()

    def ReadSettings_Xml(self, settings: ET.Element):
        self._ReadTags_Xml(settings)
        self._ReadReelsets_Xml(settings)

    def SettingsElement_Xml(self):
        settings = ET.Element('settings')
        reelsets = ET.SubElement(settings, 'Reelsets')
        for tag_name, tag_value in self.mainTags.items():
            settings.set(tag_name, tag_value)
        for tag_name, tag_value in self.custTags.items():
            settings.set(tag_name, tag_value)
        for i, reelset in enumerate(self.reelsets):
            reelsets.append(reelset.ElementReelset_Xml())
        return self._Prettify_Xml(settings)

    def GetReelsets(self, section_id=None, section_name=None):
        if section_id is None and section_name is None:
            return self.reelsets
        elif section_id is not None and section_name is None:
            return [reelset for reelset in self.reelsets if reelset.mainTags['section'] == str(section_id)]
        elif section_name is not None and section_id is None:
            return [reelset for reelset in self.reelsets if reelset.mainTags['sectionName'] == section_name]

    def CheckRanges(self):
        section_tot_weights = [0 for _ in range(len(self.section_names))]
        section_reelsets_count = [0 for _ in range(len(self.section_names))]
        for i in range(len(self.section_names)):
            reelsets_in_section = self.GetReelsets(i)
            section_reelsets_count[i] = len(reelsets_in_section)
            prev_range = [-1, -1]
            for j, reelset in enumerate(reelsets_in_section):
                reelset_range = [int(num) for num in reelset.mainTags['range'].split()]
                if reelset_range[0]-1 != prev_range[1]:
                    print('RANGE ERROR. SECTION NAME:', self.section_names[i], 'SECTION ID:', i)
                    if j == 0:
                        print('range:', prev_range)
                    else:
                        print('    Reelset', reelsets_in_section[j-1].reelset_index,
                              reelsets_in_section[j-1].mainTags['reelName'],
                              'range:', prev_range)
                    print('    Reelset', reelset.reelset_index, reelset.mainTags['reelName'], 'range:', reelset_range)
                    print()
                prev_range = reelset_range
                section_tot_weights[i] += reelset_range[1] - reelset_range[0] + 1
        print('Section Weights')
        for i, section in enumerate(self.section_names):
            print(i, section, 'Total Weight:', section_tot_weights[i], section_reelsets_count[i], 'Reelsets')

    def SaveSettings(self, game_name: str = '', file_name: str = '', *inner_directories):
        if game_name == '':
            game_name = self.mainTags['GameNameShort']
        if file_name == '':
            file_name = self.mainTags['VersionName']+'.xml'
        result_path = self.path_handler.GetResultDataFilePath(game_name, file_name, *inner_directories)
        ET.ElementTree(self.SettingsElement_Xml()).write(result_path)

    def _ReadTags_Xml(self, settings: ET.Element):
        for tag_name, tag_value in settings.attrib.items():
            if tag_name in self.mainTags.keys():
                self.mainTags[tag_name] = tag_value
            else:
                self.custTags[tag_name] = tag_value

    def _ReadReelsets_Xml(self, settings: ET.Element):
        for i, reelset in enumerate(settings[0]):
            cur_reelset = Reelset(i)
            cur_reelset.ReadReelset_Xml(reelset, i)
            self.reelsets.append(cur_reelset)
            if reelset.attrib['sectionName'] not in self.section_names:
                self.section_names.append(reelset.attrib['sectionName'])

    def _Prettify_Xml(self, root_elem: ET.Element):
        rough_string = ET.tostring(root_elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return ET.fromstring(reparsed.toprettyxml(indent="    "))