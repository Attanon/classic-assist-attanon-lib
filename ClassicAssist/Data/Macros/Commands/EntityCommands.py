def AddFriend(obj):
    """
    Adds a mobile to friends list, will display target cursor if no serial/alias supplied.
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    """
    pass


def Ally(obj):
    """
    Returns true if the mobile's notoriety is Ally
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    """
    pass


def AutoColorPick(hue: int):
    """
    Setup an automated reply to the incoming dye color gump, allowing you to define dye tubs color. That command should be added prior to the action that opens the color pick gump.
    :param hue:  Item Hue or -1 for any.
    """
    pass


def BuffExists(name: str):
    """
    Check for a specific buff
    :param name:  Buff name.
    """
    pass


def BuffTime(name: str):
    """
    Returns milliseconds remaining for given buff name, or 0 if expired/not enabled.
    :param name:  Buff name.
    """
    pass


def ClearIgnoreList():
    """
    Clears the ignore list.
    """
    pass


def ClearObjectQueue():
    """
    Clears all actions in action packet queue
    """
    pass


def CountType(graphic: int, source, hue: int):
    """
    Amount comparison of item type inside a container.
    :param graphic:  ItemID / Graphic such as 0x3db.
    :param source:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    :param hue:  Item Hue or -1 for any. (Optional)
    """
    pass


def CountTypeGround(graphic: int, hue: int, range: int):
    """
    Amount comparison of item or mobile type on the ground.
    :param graphic:  ItemID / Graphic such as 0x3db.
    :param hue:  Item Hue or -1 for any. (Optional)
    :param range:  Range, ie 10. (Optional)
    """
    pass


def Criminal(obj):
    """
    Returns true if the mobile's notoriety is Criminal
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    """
    pass


def Dead(obj):
    """
    Returns true if given mobile is dead, false if not, if parameter is null, then returns the value from the player (parameter can be serial or alias).
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    """
    pass


def Dex():
    """
    Returns the dexterity of the player
    """
    pass


def DiffHits(obj):
    """
    Returns the given mobiles difference between max and current hits, if parameter is null, then returns the value from the player (parameter can be serial or alias).
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    """
    pass


def DiffHitsPercent(obj):
    """
    Returns the given mobiles different between max and currents hits as a percentage, if parameter is null, then returns the value from the player (parameter can be serial or alias).
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    """
    pass


def DiffWeight():
    """
    Returns the difference between max weight and weight.
    """
    pass


def Direction(obj):
    """
    Returns the Direction the given alias/serial is facing
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    """
    pass


def DirectionTo(obj):
    """
    Returns the Direction the entity is in relative to the player.
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    """
    pass


def Distance(obj, y):
    """
    Returns the distance to the given entity or coordinates.
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self". (Optional) or x, y
    :param y:  Y Coordinate.
    """
    pass


def Enemy(obj):
    """
    Returns true if the mobile's notoriety is Enemy
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    """
    pass


def EquipWand(wandname: str, minimumcharges: int):
    """
    Search for a wand inside your backpack and equip it
    :param wandname:  Wand name. See Also
    :param minimumcharges:  Integer value - See description for usage. (Optional)
    """
    pass


def FindObject(obj, range: int, findlocation):
    """
    Searches for entity by serial and sets found alias, defaults to ground if no source given.
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    :param range:  Range, ie 10. (Optional)
    :param findlocation:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    """
    pass


def FindType(graphic: int, range: int, findlocation, hue: int, minimumstackamount: int):
    """
    Searches for entity by graphic ID and sets found alias, defaults to ground if no source given.
    :param graphic:  ItemID / Graphic such as 0x3db.
    :param range:  Range, ie 10. (Optional)
    :param findlocation:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    :param hue:  Item Hue or -1 for any. (Optional)
    :param minimumstackamount:  Integer representing an amount, ie 10. (Optional)
    """
    pass


def FindWand(wandname: str, containersource, minimumcharges: int):
    """
    Search for a wand and set alias "found".
    :param wandname:  Wand name. See Also
    :param containersource:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    :param minimumcharges:  Integer value - See description for usage. (Optional)
    """
    pass


def Followers():
    """
    Returns the number of current followers as per status bar data.
    """
    pass


def Gold():
    """
    Returns the gold value as per status bar data.
    """
    pass


def Graphic(obj):
    """
    Returns Item ID of given object (parameter can be serial or alias).
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    """
    pass


def Gray(obj):
    """
    Returns true if the mobile's notoriety is Attackable
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    """
    pass


def Hidden(obj):
    """
    Returns true if given mobile is hidden, false if not, if parameter is null, then returns the value from the player (parameter can be serial or alias).
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    """
    pass


def Hits(obj):
    """
    Returns the given mobiles hitpoints, if parameter is null, then returns the value from the player (parameter can be serial or alias).
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    """
    pass


def Hue(obj):
    """
    Returns Hue of given object (parameter can be serial or alias).
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    """
    pass


def IgnoreObject(obj):
    """
    Ignores the given object from find commands
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    """
    pass


def InFriendList(obj):
    """
    Returns true if supplied mobile exists in the friends list.
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    """
    pass


def InIgnoreList(obj):
    """
    Check whether the given serial / alias exists in the ignore list.
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    """
    pass


def Innocent(obj):
    """
    Returns true if the mobile's notoriety is Innocent
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    """
    pass


def InParty(obj):
    """
    Return the true if the given serial/alias is in party with you.
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    """
    pass


def InRange(obj, distance: int):
    """
    Check for range between your character and another mobile or an item
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    :param distance:  Distance.
    """
    pass


def Int():
    """
    Returns the intelligence of the player
    """
    pass


def Invulnerable(obj):
    """
    Returns true if the mobile's notoriety is Invulnerable
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    """
    pass


def Luck():
    """
    Returns the luck value as per status bar data.
    """
    pass


def Mana(obj):
    """
    Returns the given mobiles mana, if parameter is null, then returns the value from the player (parameter can be serial or alias).
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    """
    pass


def MaxFollowers():
    """
    Returns the number of max followers as per status bar data.
    """
    pass


def MaxHits(obj):
    """
    Returns the given mobiles max hitpoints, if parameter is null, then returns the value from the player (parameter can be serial or alias).
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    """
    pass


def MaxMana(obj):
    """
    Returns the given mobiles max mana, if parameter is null, then returns the value from the player (parameter can be serial or alias).
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    """
    pass


def MaxStam(obj):
    """
    Returns the given mobiles max stamina, if parameter is null, then returns the value from the player (parameter can be serial or alias).
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    """
    pass


def MaxWeight():
    """
    Returns the max weight as per status bar data.
    """
    pass


def Mounted(obj):
    """
    Returns true if the specified mobile is mounted.
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    """
    pass


def MoveItem(item, destination, amount: int, x: int, y: int):
    """
    Move item to container (parameters can be serials or aliases).
    :param item:  An entity serial in integer or hex format, or an alias string such as "self".
    :param destination:  An entity serial in integer or hex format, or an alias string such as "self".
    :param amount:  Integer representing an amount, ie 10. (Optional)
    :param x:  X Coordinate. (Optional)
    :param y:  Y Coordinate. (Optional)
    """
    pass


def MoveItemOffset(obj, xoffset: int, yoffset: int, zoffset: int, amount: int):
    """
    Move the given serial/alias to the specified x,y,z offset of the player, no amount specified or -1 will move the full stack.
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    :param xoffset:  X Coordinate offset.
    :param yoffset:  Y Coordinate offset.
    :param zoffset:  Z Coordinate offset.
    :param amount:  Integer representing an amount, ie 10. (Optional)
    """
    pass


def MoveType(id: int, sourcecontainer, destinationcontainer, x: int, y: int, z: int, hue: int, amount: int):
    """
    Move a type from source to destintion.
    :param id:  ItemID / Graphic such as 0x3db.
    :param sourcecontainer:  An entity serial in integer or hex format, or an alias string such as "self".
    :param destinationcontainer:  An entity serial in integer or hex format, or an alias string such as "self".
    :param x:  X Coordinate. (Optional)
    :param y:  Y Coordinate. (Optional)
    :param z:  Z Coordinate. (Optional)
    :param hue:  Item Hue or -1 for any. (Optional)
    :param amount:  Integer representing an amount, ie 10. (Optional)
    """
    pass


def MoveTypeOffset(id: int, findlocation, xoffset: int, yoffset: int, zoffset: int, amount: int, hue: int, range: int):
    """
    Move the given type from the specified source container to the specified x,y,z offset of the player, no amount specified or -1 will move the full stack.
    :param id:  ItemID / Graphic such as 0x3db.
    :param findlocation:  An entity serial in integer or hex format, or an alias string such as "self".
    :param xoffset:  X Coordinate offset.
    :param yoffset:  Y Coordinate offset.
    :param zoffset:  Z Coordinate offset.
    :param amount:  Integer representing an amount, ie 10. (Optional)
    :param hue:  Item Hue or -1 for any. (Optional)
    :param range:  Distance. (Optional)
    """
    pass


def Murderer(obj):
    """
    Returns true if the mobile's notoriety is Murderer
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    """
    pass


def Name(obj):
    """
    Return the name of the given mobile.
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    """
    pass


def Paralyzed(obj):
    """
    Returns true if the specified mobile is frozen.
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    """
    pass


def Poisoned(obj):
    """
    Returns true if the specified mobile is poisoned.
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    """
    pass


def Rehue(obj, hue: int):
    """
    Rehue an item/mobile the specified hue value, set to 0 to remove. (Experimental)
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    :param hue:  Item Hue or -1 for any.
    """
    pass


def RemoveFriend(obj):
    """
    Removes a mobile from the friends list, will display target cursor if no serial/alias supplied.
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    """
    pass


def SpecialMoveExists(name: str):
    """
    Check for a specific special move
    :param name:  Special move name.
    """
    pass


def Stam(obj):
    """
    Returns the given mobiles stamina, if parameter is null, then returns the value from the player (parameter can be serial or alias).
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    """
    pass


def Str():
    """
    Returns the strength of the player
    """
    pass


def TithingPoints():
    """
    Returns the current players' tithing points.
    """
    pass


def UseLayer(layer, obj):
    """
    Uses object in the specified layer, optional parameter for mobile
    :param layer:  String representing a layer, such as "OneHanded" or "Talisman" etc.
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    """
    pass


def War(obj):
    """
    Checks whether a mobile is in war mode.
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    """
    pass


def Weight():
    """
    Returns the current weight as as per status bar data.
    """
    pass


def X(obj):
    """
    Returns X coordinate of given object (parameter can be serial or alias).
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    """
    pass


def Y(obj):
    """
    Returns Y coordinate of given object (parameter can be serial or alias).
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    """
    pass


def YellowHits(obj):
    """
    Returns true if the specified mobile is yellowhits.
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    """
    pass


def Z(obj):
    """
    Returns Z coordinate of given object (parameter can be serial or alias).
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    """
    pass