def Autoloot(obj):
    """
    Sets the container for the Autoloot agent to put items into...
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    """
    pass


def Counter(name: str):
    """
    Returns the count of the given counter agent.
    :param name:  Agent entry name.
    """
    pass


def Dress(name: str):
    """
    Returns true if the Dress agent is currently dressing or undressing.
    :param name:  Agent entry name. (Optional)
    """
    pass


def DressConfig():
    """
    Adds all equipped items to a temporary list that isn't persisted on client close.
    """
    pass


def Dressing():
    """
    Returns true if the Dress agent is currently dressing or undressing.
    """
    pass


def Organizer(entryname: str, sourcecontainer, destinationcontainer):
    """
    Set the source and destination for the specified Organizer name
    :param entryname:  Agent entry name.
    :param sourcecontainer:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    :param destinationcontainer:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    """
    pass


def Organizing():
    """
    Returns true if currently running an organizer agent, or false if not.
    """
    pass


def SetAutolootContainer(obj):
    """
    Sets the container for the Autoloot agent to put items into...
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    """
    pass


def SetOrganizerContainers(entryname: str, sourcecontainer, destinationcontainer):
    """
    Set the source and destination for the specified Organizer name
    :param entryname:  Agent entry name.
    :param sourcecontainer:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    :param destinationcontainer:  An entity serial in integer or hex format, or an alias string such as "self". (Optional)
    """
    pass


def SetVendorBuyAutoBuy(listname: str, onoff: str):
    """
    Enables or disables autobuying of the specified vendor buy list name...
    :param listname:  List name.
    :param onoff:  "on" or "off". (Optional)
    """
    pass


def Undress(name: str):
    """
    Undress all items in the specified dress agent.
    :param name:  Agent entry name.
    """
    pass