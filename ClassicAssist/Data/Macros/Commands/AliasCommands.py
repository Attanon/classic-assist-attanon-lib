def FindAlias(aliasname: str):
    """
    Returns true if alias serial can be found on screen, false if not.
    :param aliasname:  Alias name.
    """
    pass


def GetAlias(aliasname: str):
    """
    Gets the value of the given alias name.
    :param aliasname:  Alias name.
    """
    pass


def PromptAlias(aliasname: str):
    """
    Prompt with an in-game target cursor to supply value for given alias name.
    :param aliasname:  Alias name.
    """
    pass


def PromptMacroAlias(aliasname: str):
    """
    Prompt with an in-game target cursor to supply value for given alias name, alias is valid only in the current macro.
    :param aliasname:  Alias name.
    """
    pass


def SetAlias(aliasname: str, obj):
    """
    Sets the value of the given alias name.
    :param aliasname:  Alias name.
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    """
    pass


def SetMacroAlias(aliasname: str, obj):
    """
    Sets the value of the given alias name, alias is valid only in the current macro.
    :param aliasname:  Alias name.
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    """
    pass


def UnsetAlias(aliasname: str):
    """
    Removes the alias name given.
    :param aliasname:  Alias name.
    """
    pass