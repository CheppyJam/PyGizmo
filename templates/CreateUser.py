import PyGizmo
from datetime import datetime
from PyGizmo.types.user import Sex

# Init club
club = PyGizmo.Club(
    'http://10.11.0.9',
    'Admin',
    'admin'
)


# Create user
club.addUser(
    username='SherryJam',
    userGroupId=club.usergroups[0].id,
    email='chep@spworlds.ru',
    address='Lorem Ipsum',
    birthDate=datetime.fromtimestamp(1108209600),
    city='Moscow',
    country='Russia',
    firstName='Aleksey',
    identification='@CheppyJam',
    sex=Sex.MALE
)
