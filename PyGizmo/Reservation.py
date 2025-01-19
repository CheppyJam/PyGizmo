from .types.club import ClubType
from .types.reservation import ReservationType
from datetime import datetime

update_supported_params = {
    'id': 'Id',
    'userId': 'UserId',
    'note': 'Note',
    'contactPhone': 'ContactPhone',
    'contactEmail': 'ContactEmail',
    'date': 'Date',
    'duration': 'Duration',
    'users': 'Users',
    'hosts': 'Hosts'
}

class Reservation(ReservationType):
    def __init__(self, gizmo: ClubType, data: dict):
        self.gizmo = gizmo
        self.data = data
    
    def __getattribute__(self, name):
        if name == 'data':
            return super().__getattribute__(name)
        # Convert type to datetime
        if name in ['date', 'endDate']:
            if self.data.get(name) is None: return
            return datetime.fromisoformat(self.data.get(name)[0:23])
        
        # Convert type to int
        elif name in ['id', 'userId', 'duration']:
            if self.data.get(name) is None: return 0
            return int(self.data.get(name))
        
        # Properties
        elif name in ['hosts']:
            return super().__getattribute__(name)

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
        res = self.gizmo.session.post(f'{self.gizmo.apiUri}/api/reservations/',params={
            update_supported_params['id']: self.id,
            update_supported_params[name]: value
        })
        print(res.json())
        return res.status_code == 200
    
    @property
    def hosts(self):
        hostIds = [host['hostId'] for host in self.data['hosts']]
        hosts =  list()
        for host in hostIds:
            hosts.append(self.gizmo.getHost(hostId=host))
        return hosts