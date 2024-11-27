import pandas as pd
import xml.etree.ElementTree as ET
import xmltodict

class Table:
    
    # Constructor Method
    def __init__(self, path_parts, path_bubbles):
        self.path_bubblesn = path_bubbles
        self.path_partsn = path_parts

    def printTableBubbles(self, bubblesset, text):
            if len(bubblesset) != 0:
                print(text)
                print(bubblesset) 

    def compareTables(self):
        parts_list = pd.read_xml(self.path_partsn)
        parts_list = parts_list[['Lookup']].drop_duplicates().dropna()
        parts_list = parts_list['Lookup'].tolist()
        #print(parts_list)

        xml_data = open(self.path_bubblesn, 'r').read()  # Read data
        xmlDict = xmltodict.parse(xml_data)  # Parse XML
        M = dict(xmlDict['Matrix'])
        n_buubles = len(M['Value'])
        bubbles_list = []

        for i in range(n_buubles):
            bubbles_list.append(M['Value'][i]['Lookup'][0] + "-" + M['Value'][i]['Value']['Element'][0])
        #print(bubbles_list)
        
        bubbles_list.append("H")
        parts_set = set(parts_list)
        bubbles_set = set(bubbles_list)
        s1 = parts_set.difference(bubbles_set)
        s2 = bubbles_set.difference(parts_set)

        self.printTableBubbles(s1, "Burbujas que aparecen en la tabla de parts, pero no en la de burbujas")
        self.printTableBubbles(s2, "Burbujas que aparecen en la tabla de burbujas, pero no en la de parts")
        
obj1 = Table(r'C:\\Users\\Alexis\\Desktop\\Bubbles Macro\\Matrix 958_MCP1_Parts_REV0J.xml', r'C:\\Users\\Alexis\\Desktop\\Bubbles Macro\\Matrix 958_MCP1_Bubbles_REV0J.xml')
obj1.compareTables()