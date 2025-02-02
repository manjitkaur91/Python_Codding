from collections import OrderedDict
IniOrderedDict=OrderedDict[('man',1),('san',3)]
IniOrderedDict.update({'nav':'5'})
IniOrderedDict.move_to_end('nav', last=False)
print("full Dictionary" + str(IniOrderedDict))