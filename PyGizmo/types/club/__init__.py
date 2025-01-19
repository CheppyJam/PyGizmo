from typing import List
from ..user import UserMemberType
from ..host import HostType
from ..usergroup import UserGroupType
from ..reservation import ReservationType
from datetime import datetime
from ..user import Sex
from requests import Session
from requests.auth import HTTPBasicAuth


class ClubType:
    def __init__(self, apiUri: str, username: str, password: str):
        self.apiUri: str = apiUri
        self.username: str = username
        self.session: Session
        self.session.auth = HTTPBasicAuth(username, password)

    @property
    def reservations(self) -> List[ReservationType]:
        """Return all Reservation in Club"""

    @property
    def hosts(self) -> List[HostType]:
        """Return all Hosts in Club"""

    @property
    def usergroups(self) -> List[UserGroupType]:
        """Return all UserGroups in Club"""

    def getUserGroup(self, userGroupId: int) -> UserGroupType:
        """Return one UserGroup
        Args:
        userGroupId: int # User group id
        """

    def getUser(
            self,
            username: str = None,
            phoneNumber: str = None,
            userId: str = None,
            identification: str = None,
    ) -> UserMemberType:
        """Return User object from GizmoServer

        Args:
        username: str # Username of User
        phoneNumber: str # Phone number without '+' of User
        userId: int # ID of User
        identification: str # ID field from Gizmo Manager of User
        """

    def getHost(self, hostNumber: int = None, hostId: int = None) -> HostType:
        """Return Host object

        Args:
        hostNumber - Visible number of Host
        hostId - Gizmo id of Host
        """
    def addUser(
            self,
            username: str,
            userGroupId: int,
            email: str = None,
            firstName: str = None,
            lastName: str = None,
            birthDate: datetime = None,
            address: str = None,
            city: str = None,
            country: str = None,
            postCode: str = None,
            phone: str = None,
            mobilePhone: str = None,
            sex: Sex = None,
            identification: str = None
    ) -> None:
        """Create User on GizmoServer

        Args:
        username: str,
        userGroupId: int,
        email: str = None,
        firstName: str = None,
        lastName: str = None,
        birthDate: datetime = None,
        address: str = None,
        city: str = None,
        country: str = None,
        postCode: str = None,
        phone: str = None,
        mobilePhone: str = None,
        sex: Sex = None,
        identification: str = None
        """
