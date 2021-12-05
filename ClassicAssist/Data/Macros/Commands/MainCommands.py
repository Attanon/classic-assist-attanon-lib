def DisplayQuestPointer(x: int, y: int, enabled: bool):
    """
    Display quest arrow pointer to specified coordinates
    :param x:  X Coordinate.
    :param y:  Y Coordinate.
    :param enabled:  True/False value, see description for usage. (Optional)
    """
    pass


def HideEntity(obj):
    """
    Remove an item/mobile from the screen
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    """
    pass


def Hotkeys(onoff: str):
    """
    Enable and disable hotkeys.
    :param onoff:  "on" or "off". (Optional)
    """
    pass


def Info(obj):
    """
    Show object inspector for supplied serial / alias, will prompt for target if no parameter given.
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    """
    pass


def InvokeVirtue(virtue: str):
    """
    Use a virtue by name.
    :param virtue:  String value - See description for usage. See Also
    """
    pass


def Logout():
    """
    Disconnects from the server and returns to the login screen
    """
    pass


def MessageBox(title: str, body: str):
    """
    Show a simple message box with a custom title and body.
    :param title:  String value - See description for usage.
    :param body:  String value - See description for usage.
    """
    pass


def Pause(milliseconds: int):
    """
    Pauses execution for the given amount in milliseconds.
    :param milliseconds:  Timeout specified in milliseconds.
    """
    pass


def Playing(macroname: str):
    """
    Returns true if there is a macro, use in background macros.
    :param macroname:  Macro name.
    """
    pass


def PlaySound(obj5, bool5: bool):
    """
    Play sound by id or system .wav file.
    :param obj5: not documented
    :param bool5: not documented
    """
    pass


def Quit():
    """
    Closes the client
    """
    pass


def Resync():
    """
    Sends Resync request to server.
    """
    pass


def SetQuietMode(onoff: bool):
    """
    Set quiet mode True/False, True reduces the number of messages macro commands emit.
    :param onoff:  "on" or "off".
    """
    pass


def Snapshot(delay: int, fullscreen: bool, filename: str):
    """
    Take a screenshot of the window
    :param delay:  Integer value - See description for usage. (Optional)
    :param fullscreen:  True/False value, see description for usage. (Optional)
    :param filename:  String value - See description for usage. (Optional)
    """
    pass


def SysMessage(text: str, hue: int):
    """
    Send a text message.
    :param text:  String value - See description for usage.
    :param hue:  Item Hue or -1 for any. (Optional)
    """
    pass


def WarMode(onoff: str):
    """
    Sets war mode status, parameter on, off, or toggle, defaults to toggle if no parameter given.
    :param onoff:  "on" or "off". (Optional)
    """
    pass
