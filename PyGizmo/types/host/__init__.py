from .HostStatus import HostStatus
from datetime import datetime

class HostType:
    id: int
    name: str
    status: HostStatus
    state: int
    number: int
    iconId: int
    isDeleted: bool
    hostGroupId: int
    createdById: int
    createdTime: datetime
    modifiedTime: datetime
    modifiedById: int

    def lock(self) -> None:
        """Lock the Host"""
    
    def unlock(self) -> None:
        """Unlock the Host"""
    
    @property
    def status(self) -> HostStatus:
        """Return HostStatus
        values:
        INGAME = 0: int
        FREE = 1: int
        LOCKED = 2: int
        BROKEN = 3: int
        """
    