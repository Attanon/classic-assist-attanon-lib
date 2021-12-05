def ClearList(listname: str):
    """
    Clear a list by name.
    :param listname:  List name.
    """
    pass


def CreateList(listname: str):
    """
    Create list with given name, if list already exists, it is overwritten.
    :param listname:  List name.
    """
    pass


def GetList(listname: str):
    """
    Returns array of all entries in the list, for use with for loop etc.
    :param listname:  List name.
    """
    pass


def InList(listname: str, value):
    """
    Checks whether a list contains a given element.
    :param listname:  List name.
    :param value:  Integer value - See description for usage.
    """
    pass


def List(listname: str):
    """
    Returns the number of entries in the list.
    :param listname:  List name.
    """
    pass


def ListExists(listname: str):
    """
    Returns true if list exist, or false if not.
    :param listname:  List name.
    """
    pass


def PopList(listname: str, elementvalue):
    """
    Remove elements from a list, returns the number of elements removed
    :param listname:  List name.
    :param elementvalue:  Element value to remove from list, or 'front' to remove the first item, or 'back' to remove last entry, default 'back'. (Optional)
    """
    pass


def PushList(listname: str, value):
    """
    Pushes a value to the end of the list, will create list if it doesn't exist.
    :param listname:  List name.
    :param value:  Integer value - See description for usage.
    """
    pass


def RemoveList(listname: str):
    """
    Removes the list with the given name.
    :param listname:  List name.
    """
    pass