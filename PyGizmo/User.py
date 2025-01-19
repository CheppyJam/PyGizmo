
from .UserGroup import UserGroup
from .types.club import ClubType
from .types.user import UserMemberType
from datetime import datetime, timedelta
from .types.reservation import ReservationType
from typing import List
from .types.host import HostStatus


update_supported_params = {
    'username':'UserName',
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

class User(UserMemberType):
    def __init__(self,gizmo: ClubType, data: dict):
        self.data = data
        self.gizmo = gizmo

    @property
    def usergroup(self) -> UserGroup:
        return self.gizmo.getUserGroup(self.data['userGroupId'])
    
    def login(self, hostId):
        return self.gizmo.session.post(f'{self.gizmo.apiUri}/api/users/{self.id}/login/{hostId}')  

    def __getattribute__(self, name):
        if name == 'data':
            return super().__getattribute__(name)
        
        # Convert type to datetime
        elif name in ['createdTime', 'birthDate', 'enableDate', 'disabledDate', 'modifiedTime']:
            if self.data.get(name) is None: return
            return datetime.fromisoformat(self.data.get(name)[0:23])
        
        # Convert type to int
        elif name in ['id', 'createdById', 'userGroupId', 'modifiedById']:
            if self.data.get(name) is None: return 0
            return int(self.data.get(name))

        # Return if type not converted and if exists in data object
        elif name in self.data.keys():
            return self.data.get(name)
        
        else:
            return super().__getattribute__(name)

    def __setattr__(self, name, value):
        if name in update_supported_params:
            self.data[name] = value
            self._api_update_value(name, value)
        else:
            super().__setattr__(name,value)

    def _api_update_value(self, name, value):
        res = self.gizmo.session.post(f'{self.gizmo.apiUri}/api/users/',params={
            'UserId': self.id,
            update_supported_params[name]: value
        })
        print(res.json())
        return res.status_code == 200

    def __repr__(self):
        res = '<gizmo.user.User {} {} {} >'
        return res.format(
            f'username:{self.username}',
            f'group:{self.usergroup.name}',
            f'id:{self.id}'
        )
    
    def auth_qr(self, hostId):
        host = self.gizmo.getHost(hostId)
        def checkReservation():
            reservations: List[ReservationType]  = self.gizmo.reservations
            current_time = datetime.now() + timedelta(hours=3)
            for reservation in reservations:
                if reservation.status ==  1: continue
                if not host.id in [host.id for host in reservation.hosts]: continue
                print('---'*3, reservation.id, '---'*3)
                end_block_time = reservation.date + timedelta(minutes=15)
                print(end_block_time, current_time)
                if end_block_time > current_time:
                    return True
        
        def checkHostAuth():
            return not host.status == HostStatus.FREE

        reservated = checkReservation()
        in_use = checkHostAuth()

        can_login = not (reservated or in_use)
        print(reservated, in_use)
        if can_login:
            self.login(host.id)
            return True
        return False
        
