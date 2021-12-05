def ClearJournal():
    """
    Clear all journal texts.
    """
    pass


def InJournal(text: str, author: str, hue: int):
    """
    Check for a text in journal, optional source name.
    :param text:  String value - See description for usage.
    :param author:  String value - See description for usage. (Optional)
    :param hue:  Item Hue or -1 for any. (Optional)
    """
    pass


def WaitForJournal(entries: str, timeout: int, author: str):
    """
    Wait up the given timeout for one of any of provided array of string to appear in journal
    :param entries:  An array of strings.
    :param timeout:  Timeout specified in milliseconds.
    :param author:  String value - See description for usage. (Optional)
    """
    pass