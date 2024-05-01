from dataclasses import dataclass, field


@dataclass
class User:
    id: int = field(default_factory=int)
    name: str = field(default_factory=str)
    email: str = field(default_factory=str)
