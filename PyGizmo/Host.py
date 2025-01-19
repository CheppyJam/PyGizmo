from .types.host.HostStatus import HostStatus
from .types.host import HostType
from .types.club import ClubType
from datetime import datetime


class Host(HostType):
    def __init__(self, gizmo: ClubType, data: dict):
        self.gizmo = gizmo
        self.server = gizmo.session
        self.apiUri = gizmo.apiUri
        self.data = data

        def returnGroup():
            groupsName: list = self.server.get(
                f'{self.apiUri}/api/hostgroups'
            ).json()['result']
            for i in groupsName:
                if i['id'] == self.hostGroupId:
                    return i['name']
            return 'Неизвестная группа'

        self.groupName = returnGroup()

    def lock(self):
        return self.server.post(
            f'{self.apiUri}/api/hosts/{self.id}/lock/true'
        ).status_code

    def unlock(self):
        return self.server.post(
            f'{self.apiUri}/api/hosts/{self.id}/lock/false'
        ).status_code

    def __getattribute__(self, name):
        if name in [
            'data',
            'server',
            'gizmo',
            'apiUri',
            'status'
        ]:
            return super().__getattribute__(name)

        # Convert type to datetime
        elif name in ['createdTime', 'modifiedTime']:
            if self.data.get(name) is None:
                return
            return datetime.fromisoformat(self.data.get(name)[0:23])

        # Convert type to int
        elif name in [
            'id',
            'number',
            'iconId',
            'hostGroupId',
            'createdById',
            'modifiedById'
        ]:
            if self.data.get(name) is None:
                return 0
            return int(self.data.get(name))
        else:
            ...
        # Return if type not converted and if exists in data object
        if name in self.data.keys():
            return self.data.get(name)
        else:
            return super().__getattribute__(name)

    @property
    def status(self):
        self.data = self.gizmo.session.get(
            f'{self.gizmo.apiUri}/api/hosts/{self.id}'
        ).json()['result']
        if self.state > 0:
            if self.state == 2:
                return HostStatus.LOCKED
            if self.state in [1, 3]:
                return HostStatus.BROKEN

        usersessions = self.server.get(
            f'{self.apiUri}/api/usersessions/active'
        ).json()['result']

        for usersession in usersessions:
            if usersession['hostId'] == self.id:
                return HostStatus.INGAME

        return HostStatus.FREE

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Host({self.id}, \'{self.name}\')'
