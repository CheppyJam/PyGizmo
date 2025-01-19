import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime

from .types.club import ClubType
from .types.user.Sex import Sex

from .exceptions.user.addUser import NonUniqueEntityValue

from .User import User
from .Host import Host
from .UserGroup import UserGroup
from .Reservation import Reservation

class Club(ClubType):
    def __init__(self, apiUri: str, username: str, password: str):
        self.apiUri = apiUri
        self.username = username
        self.session = requests.Session()
        self.session.auth = HTTPBasicAuth(username, password)
    
    @property
    def hosts(self):
        req = self.session.get(f'{self.apiUri}/api/hosts')
        if req.status_code == 200:
            hosts = []
            for host in req.json()['result']:
                if host['isDeleted']: continue
                hosts.append(host)
            return [Host(self, data) for data in hosts]
        else:
            raise Exception('Failed to GET Hosts')
    
    @property
    def usergroups(self):
        req = self.session.get(f'{self.apiUri}/api/usergroups')
        if req.status_code == 200:
            return [UserGroup(self, data) for data in req.json()['result']]
        else:
            raise Exception('Failed to GET UserGroups')
    
    @property
    def reservations(self):
        req = self.session.get(f'{self.apiUri}/api/reservations')
        if req.status_code == 200:
            return [Reservation(self, data) for data in req.json()['result']]
        else:
            raise Exception('Failed to GET UserGroups')
        
    def getUserGroup(self, userGroupId: int) -> UserGroup:
        for userGroup in self.usergroups:
            if userGroup.id == userGroupId: return userGroup
        return None

    def getUser(
            self,
            username: str = None,
            phoneNumber: str = None,
            userId: str = None,
            identification: str = None,
        ):
        """Return User object from GizmoServer
        
        Args:
        username: str # Username of User
        phoneNumber: str # Phone number without '+' of User
        userId: int # ID of User
        identification: str # ID field from Gizmo Manager of User
        """
        if not username == None:
            userId = self.session.get(f'{self.apiUri}/api/users/{username}/username')
            if userId.status_code != 200: return None
            if userId.json()['result'] == None: return None
            if userId.json()['result']['isDeleted']: return None
            return User(self, userId.json()['result'])
        elif not phoneNumber == None:
            users = self.session.get(f'{self.apiUri}/api/users/')
            if users.status_code != 200: return None
            if users.json()['result'] == None: return None
            for user in users.json()['result']:
                if user['isDeleted']: continue
                if user['isDisabled']: continue
                print(user['phone'] == phoneNumber)
                if user['phone'] == phoneNumber:
                    return User(self, user)
                if user['username'] == phoneNumber:
                    return User(self, user)
                if user['mobilePhone'] == phoneNumber:
                    return User(self, user)              
            return None
        elif not userId == None:
            userId = self.session.get(f'{self.apiUri}/api/users/{userId}')
            if userId.status_code != 200: return None
            if userId.json()['result'] == None: return None
            if userId.json()['result']['isDeleted']: return None
            return User(self, userId.json()['result'])
        elif not identification == None:
            users = self.session.get(f'{self.apiUri}/api/users/')
            if users.status_code != 200: return None
            if users.json()['result'] == None: return None
            for user in users.json()['result']:
                if user['identification'] == identification: 
                    if user['isDeleted']: return None
                    return User(self, user)
            return None
        else:
            return None
        
    def getHost(self, hostNumber: int = None, hostId: int = None):
        for host in self.hosts:
            if not hostNumber == None:
                if host.number == hostNumber: return host
            elif not hostId == None:
                if host.id == hostId: return host
        return None
    
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
        ):
        fields = {
            'username':'UserName',
            'userGroupId':'UserGroupId',
            'email':'Email',
            'firstName':'FirstName',
            'lastName':'LastName',
            'birthDate':'BirthDate',
            'address':'Address',
            'city':'City',
            'country':'Country',
            'postCode':'PostCode',
            'phone':'Phone',
            'mobilePhone':'MobilePhone',
            'sex':'Sex',
            'identification':'Identification'
        }

        userData = dict()

        if not username is None: userData[fields['username']] = username
        if not userGroupId is None: userData[fields['userGroupId']] = userGroupId
        if not email is None: userData[fields['email']] = email
        if not firstName is None: userData[fields['firstName']] = firstName
        if not lastName is None: userData[fields['lastName']] = lastName
        if not birthDate is None: userData[fields['birthDate']] = birthDate.isoformat()
        if not address is None: userData[fields['address']] = address
        if not city is None: userData[fields['city']] = city
        if not country is None: userData[fields['country']] = country
        if not postCode is None: userData[fields['postCode']] = postCode
        if not phone is None: userData[fields['phone']] = phone
        if not mobilePhone is None: userData[fields['mobilePhone']] = mobilePhone
        if not sex is None: userData[fields['sex']] = sex
        if not identification is None: userData[fields['identification']] = identification

        res = self.session.put(f'{self.apiUri}/api/users', params=userData)
        if res.status_code == 400:
            err = res.json()
            raise NonUniqueEntityValue(err['message'])