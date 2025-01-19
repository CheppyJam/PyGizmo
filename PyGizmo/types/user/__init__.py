from datetime import datetime
from .BillingOption import BillingOptions
from .Sex import Sex

class UserMemberType():
    id: int
    sex: Sex
    city: str
    email: str
    guid: str
    phone: str
    country: str
    address: str
    lastName: str
    username: str
    postCode: str
    firstName: str
    isDisabled: bool
    birthDate: datetime
    enableDate: datetime
    isDisabled: bool
    createdById: int
    userGroupId: int
    createdTime: datetime
    mobilePhone: str
    modifiedById: int
    disabledDate: datetime
    modifiedTime: datetime
    smartCardUID: str
    identification: str
    billingOptions: BillingOptions
    isPersonalInfoRequested: bool
    isNegativeBalanceAllowed: bool