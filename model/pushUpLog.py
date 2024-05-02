from dataclasses import dataclass, field
from datetime import datetime

from model.user import User


@dataclass
class PushUpLog:
    id: int = field(default_factory=int)
    comment: str = field(default_factory=str)
    timestamp: datetime = datetime.utcnow()
    userId: int = User.id
