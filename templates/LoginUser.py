import PyGizmo

# Init club
club = PyGizmo.Club(
    'http://10.11.0.9',
    'Admin',
    'admin'
)

# Get user
user = club.getUser(
    username='SherryJam'
)
# Login user to PC-02
# This ID is VISIBLE ID of Host in Manager
user.login(2)
