from .TimePointAwardOptionType import TimePointAwardOptionType
from .CreditLimitOptionType import CreditLimitOptionType
from .UserGroupOption import UserGroupOption
from .GroupOverrides import GroupOverrides
from ..user.BillingOption import BillingOptions
from .UserInfoTypes import UserInfoTypes
from datetime import datetime

class UserGroupType:
    id: int
    name: str
    points: int
    options: UserGroupOption
    isDefault: bool
    overrides: GroupOverrides
    appGroupId: int
    createdTime: datetime
    createdById: int
    description: str
    creditLimit: int
    modifiedTime: datetime
    modifiedById: int
    billProfileId: int
    billingOption: BillingOptions
    pointsTimeRatio: int
    pointsMoneyRatio: int
    requiredUserInfo: UserInfoTypes
    securityProfileId: int
    isAgeRatingEnabled: bool
    pointsAwardOptions: TimePointAwardOptionType
    creditLimitOptions: CreditLimitOptionType
    waitingLinePriority: int
    isNegativeBalanceAllowed: bool
    isWaitingLinePriorityEnabled: bool