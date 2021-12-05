def CloseGump(serial: int):
    """
    Close a specified gump serial
    :param serial:  An entity serial such as 0xf00ff00f.
    """
    pass


def ConfirmPrompt(str9: str, bool4: bool):
    """
    Displays an ingame prompt with the specified message, returns True if Okay was pressed, False if not.
    :param str9: not documented
    :param bool4: not documented
    """
    pass


def GumpExists(int4: int):
    """
    Checks if a gump id exists or not.
    :param int4: not documented
    """
    pass


def InGump(gumpid: int, text: str):
    """
    Check for a text in gump.
    :param gumpid:  An entity serial in integer or hex format, or an alias string such as "self".
    :param text:  String value - See description for usage.
    """
    pass


def MessagePrompt(message: str, initialtext: str, closable: bool):
    """
    Displays an ingame gump prompting for a message
    :param message:  String value - See description for usage.
    :param initialtext:  String value - See description for usage. (Optional)
    :param closable:  True/False value, see description for usage. (Optional)
    """
    pass


def OpenGuildGump():
    """
    Opens the Guild gump
    """
    pass


def OpenQuestsGump():
    """
    Opens the Quests gump
    """
    pass


def OpenVirtueGump(obj):
    """
    Opens the Virtue gump of the given serial/alias (defaults to current player)
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    """
    pass


def ReplyGump(gumpid: int, buttonid: int, switches: int, textentries: int, str6: str):
    """
    Sends a button reply to server gump, parameters are gumpID and buttonID.
    :param gumpid:  ItemID / Graphic such as 0x3db.
    :param buttonid:  Gump button ID.
    :param switches:  Integer value - See description for usage. (Optional)
    :param textentries:  Not specified - See description for usage. (Optional)
    :param str6: not documented
    """
    pass


def SelectionPrompt(options: str, message: str, closable: bool):
    """
    **Produces an in-game gump to choose from a list of options
    :param options:  An array of strings.
    :param message:  String value - See description for usage. (Optional)
    :param closable:  True/False value, see description for usage. (Optional)
    """
    pass


def WaitForGump(gumpid: int, timeout: int):
    """
    Pauses until incoming gump packet is received, optional paramters of gump ID and timeout
    :param gumpid:  ItemID / Graphic such as 0x3db. (Optional)
    :param timeout:  Timeout specified in milliseconds. (Optional)
    """
    pass