from enum import Enum


class Status(Enum):
    """
    Estados posibles para parámetros y alarmas.
    """

    NORMAL = 0
    WARNING = 1
    ALARM = 2