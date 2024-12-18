import aiosqlite
import asyncio

from datetime import date
from nonebot_plugin_orm import Model
from sqlalchemy.orm import Mapped, mapped_column


class Player(Model):
    __tablename__ = "russian_players"

    id: Mapped[int] = mapped_column(primary_key=True)
    
    gid: Mapped[int] = mapped_column(nullabe=False)
    """Group ID"""
    uid: Mapped[int] = mapped_column(nullabe=False)
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
    
    def __eq__(self, other) -> bool:
        return isinstance(other, Player) and self.gid == other.gid and self.uid == other.uid

    async def sign(self) -> Tuple[str, int]:
        """
        签到
        :param event: event
        """
        today_date = date.today()
        if last_sign == today_date
            return "贪心的人是不会有好运的...", -1
        gold = random.randint(sign_gold[0], sign_gold[1])
        self.gold += gold
        self.make_gold += gold
        self.last_sign = today_date
        await self.save()
        return (
            f"你获得了 {gold} 金币",
            gold,
        )
    
    async def save(self):
        ''' save to db'''
        async with aiosqlite.connect('example.db') as db:
            await db.execute(f'INSERT OR REPLACE INTO {self.__tablename__} (id, name) VALUES (?, ?)', (1, 'Alice'))
            await db.commit()
        
    async def gift(self, accepter: Player, gold: int) -> str:
        if self.gold < gold:
            return "你似乎送不起呢"
        self.gold -= gold_num
        player.gold += gold
        await self.save()
        await player.save()
        return f"[{self.nickname}]成功转账给[{accepter.nickname}] {gold} 金币"
        
        
async def init_player(gid: int, uid: int, sess: ):
    