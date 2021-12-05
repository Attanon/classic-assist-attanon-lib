def Attack(obj):
    """
    Attack mobile (parameter can be serial or alias).
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    """
    pass


def BandageSelf():
    """
    Applies a bandage to the player.
    """
    pass


def ClearHands(hand: str):
    """
    Clear hands, "left", "right", or "both"
    :param hand:  Hand - "left", "right", or "both". (Optional)
    """
    pass


def ClearUseOnce():
    """
    Clear UseOnce list.
    """
    pass


def ClickObject(obj):
    """
    Single click object (parameter can be serial or alias).
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    """
    pass


def Contents(obj, timeout: int):
    """
    Wait for container contents for given container.
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    :param timeout:  Timeout specified in milliseconds. (Optional)
    """
    pass


def ContextMenu(obj, entry: int):
    """
    Request a context menu option.
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    :param entry:  Context menu entry index number.
    """
    pass


def EquipItem(obj, layer):
    """
    Equip a specific item into a given layer. Use object inspector to determine layer value.
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    :param layer:  String representing a layer, such as "OneHanded" or "Talisman" etc. See Also
    """
    pass


def EquipLastWeapon():
    """
    Send quick switch weapon packet (probably not supported on pre-AoS servers.
    """
    pass


def EquipType(id: int, layer):
    """
    Equip a specific type into a given layer. Use object inspector to determine layer value.
    :param id:  ItemID / Graphic such as 0x3db.
    :param layer:  String representing a layer, such as "OneHanded" or "Talisman" etc. See Also
    """
    pass


def Feed(obj, graphic: int, amount: int, hue: int):
    """
    Feed a given alias or serial with graphic.
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    :param graphic:  ItemID / Graphic such as 0x3db.
    :param amount:  Integer representing an amount, ie 10. (Optional)
    :param hue:  Item Hue or -1 for any. (Optional)
    """
    pass


def FindLayer(layer, obj):
    """
    Returns true and updates found alias if an item exists in the specified layer, option serial/alias for mobile to check.
    :param layer:  String representing a layer, such as "OneHanded" or "Talisman" etc. See Also
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    """
    pass


def InRegion(attribute: str, obj):
    """
    Returns true if the region of the target has the specified attribute.
    :param attribute:  String value - See description for usage. See Also
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    """
    pass


def Ping():
    """
    Retrieve an approximated ping with server. -1 on failure.
    """
    pass


def Rename(obj, name: str):
    """
    Sends rename request.
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    :param name:  String representing a name, ie "Snoopy".
    """
    pass


def ShowNames(showtype: str):
    """
    Display corpses and/or mobiles names (parameter "mobiles" or "corpses".
    :param showtype:  Show type - "mobiles" or "corpses". See Also
    """
    pass


def ToggleMounted():
    """
    Unmounts if mounted, or mounts if unmounted, will prompt for mount if no "mount" alias.
    """
    pass


def UseObject(obj, skipqueue: bool):
    """
    Sends use (doubleclick) request for given object (parameter can be serial or alias).
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    :param skipqueue:  Not specified - See description for usage. (Optional)
    """
    pass


def UseOnce(graphic: int, hue: int):
    """
    Use a specific item type (graphic) from your backpack, only once
    :param graphic:  ItemID / Graphic such as 0x3db.
    :param hue:  Item Hue or -1 for any. (Optional)
    """
    pass


def UseTargetedItem(item, target):
    """
    Uses specified item and targets target in one action. Requires server support (OSI / ServUO)
    :param item:  An entity serial in integer or hex format, or an alias string such as "self".
    :param target:  An entity serial in integer or hex format, or an alias string such as "self".
    """
    pass


def UseType(type, hue: int, container, skipqueue: bool):
    """
    Sends use (doubleclick) request for given type, optional parameters of hue and container object (defaults to player backpack) (parameters can be serial or alias).
    :param type:  An entity serial in integer or hex format, or an alias string such as "self".
    :param hue:  Item Hue or -1 for any. (Optional)
    :param container:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    :param skipqueue:  Not specified - See description for usage. (Optional)
    """
    pass


def WaitForContents(obj, timeout: int):
    """
    Wait for container contents for given container.
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    :param timeout:  Timeout specified in milliseconds. (Optional)
    """
    pass


def WaitForContext(obj, entry, timeout: int):
    """
    Request or wait for a context menu option.
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    :param entry:  Context menu entry index number.
    :param timeout:  Timeout specified in milliseconds.
    """
    pass
