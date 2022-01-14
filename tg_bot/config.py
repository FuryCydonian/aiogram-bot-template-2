from dataclasses import dataclass
from typing import List


@dataclass
class TgBot:
    token: str
    admin_ids: List[int]
    use_redis: bool

@dataclass
class Config:
    tg_bot
    db
    misc