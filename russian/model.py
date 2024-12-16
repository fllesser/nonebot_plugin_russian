from datetime import date

from nonebot_plugin_orm import Model
from sqlalchemy.orm import Mapped, mapped_column


class Player(Model):
    __tablename__ = "russian_players"

    gid: Mapped[int] = mapped_column(primary_key=True)
    """Group ID"""
    uid: Mapped[int] = mapped_column(primary_key=True)
    """User ID"""
    nickname: Mapped[str] = mapped_column(default="russian player")
    gold: Mapped[int] = mapped_column(default=0)
    """User's Gold"""
    make_gold: Mapped[int] = mapped_column(default=0)
    """User's Make Gold"""
    lose_gold: Mapped[int] = mapped_column(default=0)
    """User's Lose Gold"""
    win_count: Mapped[int] = mapped_column(default=0)
    """User's Win Count"""
    lose_count: Mapped[int] = mapped_column(default=0)
    """User's Lose Count"""
    last_sign: Mapped[date]
    """Last Sign Date"""
