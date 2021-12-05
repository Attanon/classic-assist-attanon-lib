def CloseMenu(gumpid: int):
    """
    Closes the specified menu id
    :param gumpid:  ItemID / Graphic such as 0x3db.
    """
    pass


def InMenu(gumpid: int, text: str):
    """
    Returns True if the menu title or entry titles contains the given text.
    :param gumpid:  ItemID / Graphic such as 0x3db.
    :param text:  String value - See description for usage.
    """
    pass


def MenuExists(int0: int):
    """
    Return true if the given menu id exists.
    :param int0: not documented
    """
    pass


def ReplyMenu(gumpid: int, buttonid: int, itemid: int, hue: int):
    """
    Sends a button reply to server menu
    :param gumpid:  ItemID / Graphic such as 0x3db.
    :param buttonid:  Gump button ID.
    :param itemid:  ItemID / Graphic such as 0x3db. (Optional)
    :param hue:  Item Hue or -1 for any. (Optional)
    """
    pass


def WaitForMenu(gumpid: int, timeout: int):
    """
    Pauses until incoming menu packet is received, optional paramters of gump ID and timeout
    :param gumpid:  ItemID / Graphic such as 0x3db. (Optional)
    :param timeout:  Timeout specified in milliseconds. (Optional)
    """
    pass