from .types.usergroup import UserGroupType
from datetime import datetime


class UserGroup(UserGroupType):
    def __init__(self, gizmo, data: dict):
        self.data = data
        self.gizmo = gizmo

    def __getattribute__(self, name):
        if name == 'data':
            return super().__getattribute__(name)

        # Convert type to datetime
        elif name in ['createdTime', 'modifiedTime']:
            if self.data.get(name) is None:
                return
            return datetime.fromisoformat(self.data.get(name)[0:23])

        # Convert type to int
        elif name in [
            'id',
            'points',
            'appGroupId',
            'createdById',
            'creditLimit',
            'modifiedById',
            'billProfileId',
            'pointsTimeRatio',
            'pointsMoneyRatio',
            'securityProfileId',
            'waitingLinePriority'
        ]:
            if self.data.get(name) is None:
                return 0
            return int(self.data.get(name))

        # Return if type not converted and if exists in data object
        elif name in self.data.keys():
            return self.data.get(name)

        else:
            return super().__getattribute__(name)
