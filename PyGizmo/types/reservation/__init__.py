from datetime import datetime
from .ReservationStatus import ReservationStatus
from typing import List
from ..user import UserMemberType
from ..host import HostType

class ReservationType:
    id: int
    userId: int
    note: str
    duration: int
    contactPhone: str
    contactEmail: str
    date: datetime
    pin: str
    status: ReservationStatus
    endDate: datetime
    users: List[UserMemberType]
    hosts: List[HostType]