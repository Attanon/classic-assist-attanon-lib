def ActiveAbility():
    """
    Returns True if either the primary or secondary ability is set
    """
    pass


def ClearAbility():
    """
    Clear weapon ability.
    """
    pass


def Fly(obj):
    """
    Returns true if mobile is currently flying.
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    """
    pass


def Flying(obj):
    """
    Returns true if mobile is currently flying.
    :param obj:  An entity serial in integer or hex format, or an alias string such as "self".
    """
    pass


def Land():
    """
    (Garoyle) Stop flying if currently flying.
    """
    pass


def SetAbility(ability: str, onoff: str):
    """
    Set weapon ability, parameter "primary" / "secondary".
    :param ability:  The name of the ability, "primary", "secondary", "stun" or "disarm".
    :param onoff:  "on" or "off". (Optional)
    """
    pass
