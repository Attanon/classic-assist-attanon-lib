# coding=utf-8

#AttanonLib
Version = "0.0.1"

from AttanonTypes import *

from Assistant import Engine
from ClassicAssist.Data.Macros.Commands.AbilitiesCommands import *
from ClassicAssist.Data.Macros.Commands.ActionCommands import *
from ClassicAssist.Data.Macros.Commands.AgentCommands import *
from ClassicAssist.Data.Macros.Commands.AliasCommands import *
from ClassicAssist.Data.Macros.Commands.ConsumeCommands import *
from ClassicAssist.Data.Macros.Commands.DummyCommands import *
from ClassicAssist.Data.Macros.Commands.EntityCommands import *
from ClassicAssist.Data.Macros.Commands.GumpCommands import *
from ClassicAssist.Data.Macros.Commands.JournalCommands import *
from ClassicAssist.Data.Macros.Commands.ListCommands import *
from ClassicAssist.Data.Macros.Commands.MacroCommands import *
from ClassicAssist.Data.Macros.Commands.MainCommands import *
from ClassicAssist.Data.Macros.Commands.MenuCommands import *
from ClassicAssist.Data.Macros.Commands.MobileCommands import *
from ClassicAssist.Data.Macros.Commands.MovementCommands import *
from ClassicAssist.Data.Macros.Commands.MsgCommands import *
from ClassicAssist.Data.Macros.Commands.NotorietyCommands import *
from ClassicAssist.Data.Macros.Commands.ObjectCommands import *
from ClassicAssist.Data.Macros.Commands.OrganizerCommands import *
from ClassicAssist.Data.Macros.Commands.PropertiesCommands import *
from ClassicAssist.Data.Macros.Commands.RegionCommands import *
from ClassicAssist.Data.Macros.Commands.SkillCommands import *
from ClassicAssist.Data.Macros.Commands.SpellCommands import *
from ClassicAssist.Data.Macros.Commands.TargetCommands import *
from ClassicAssist.Data.Macros.Commands.TimerCommands import *
from ClassicAssist.Data.Macros.Commands.WandCommands import *

import os
import math

def GetType(itemTypeName):
    if itemTypeName in Graphics:
        return Graphics[itemTypeName]
    elif itemTypeName in Types:
        return Types[itemTypeName]

    return 0

def FindTypeBy(itemType, container=None):
    items = []
    if container is not None:
        cont = Engine.Items.GetItem(container)

        if cont.Container == None:
            WaitForContents(container, 5000)

        items = cont.Container.GetItems()
    else:
        items = Engine.Items.GetAllItems()


    returnItems = []
    if isinstance(itemType, ItemTypeClass):
        for item in items:
            if itemType.match(item):
                returnItems.append(item)
    elif isinstance(itemType, str):
        itemType = GetType(itemType)
        if itemType == 0:
            print("Type " + itemType + " neexistuje")
            return 0

        return FindTypeBy(itemType, container)
    else:
        for item in items:
            if item.ID == itemType:
                returnItems.append(item)

    if returnItems == []:
        return None

    return returnItems[0]


def MoveItem(type, src, tar, amount=1, color=-1):
    if CountType(type, src) <= 0:
        return False

    FindType(type, -1, src, color)
    MoveItem("found", tar, amount)
    return True

def Distance(x1, y1, x2, y2):
    return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
