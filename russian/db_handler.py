from sqlalchemy import func, select
from nonebot_plugin_orm import async_scoped_session

from .model import Player


async def get_gold_rank(
    user_id: int, group_id: int, session: async_scoped_session
) -> int:
    # user_id, group_id = str(user_id), str(group_id)
    rank_orign = await session.execute(
        select(Player.nickname, Player.gold, func.count())
        .where(Player.gid == group_id)
        .order_by(Player.gold.desc())
    )
    users = rank_orign.all()
    rank = next((i + 1 for i, u in enumerate(users) if str(u[0]) == user_id), None)
    return rank or 0
    