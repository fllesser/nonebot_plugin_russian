from .model import Player
from nonebot import get_driver
import numpy as np
import random
import time

bot_name = next(iter(get_driver().config.nickname), "本裁判")

class GameManager:
    
    def __init__(self):
        self.game_dict: dict[int, Game] = dict()
   
    async def check_game_status(self, gid: int) -> str:
        if game := self.get(gid):
            if game.istimeout():
                game = await self.settlement(gid)
                #todo
                return f"对决已超时，强行结束"
            if game.is_begin:
                return f"[{game.creator.nickname}] 和 [{game.accepter.nickname}] 的对决还未结束"
            return f'现在是 {game.creator.nickname} 发起的对决\n请等待比赛结束后再开始下一轮...'
        return ""
    
    def check_shot(self, gid: int, count: int = 1, shoter: Player):
        if game := self.get(gid):
            if game.istimeout():
                if not game.is_begin:
                    return "这场对决已经过时了，请重新装弹吧！"
                else:
                    await self.settlement()
                    return #todo
            if not game.is_begin:
                if game.accepter is None:
                    return "请这位勇士先发送 接受对决 来站上擂台..."
                if shoter == game.creator:
                    "baka，游戏还没开始, 你是要枪毙自己嘛笨蛋！"
                if shoter == game.accepter:
                    return "请先 接受挑战 !"
                if shoter != game.accepter:
                    returm f"[{game.creator.nickname}]已经邀请了[{game.accepter.nickname}]作为对手"
         
            if game.operator != shoter:
                if shoter in [game.creator, game.accepter]:
                    return f"你的左轮不是连发的！该 [{shoter.nickname}] 开枪了"
                else:
                    return random.choice(
                        [
                            f"不要打扰 [{game.creator.nickname}] 和 [{game.accepter.nickname}] 的决斗啊！",
                            f"给我好好做好一个观众！不然{bot_name}就要生气了",
                            f"不要捣乱啊baka, {shoter.nickname}！",
                        ]
                    )
            
        else:
            return "目前没有进行的决斗，请发送 装弹 开启决斗吧！"
            
                
    
    def init_game(self, bullet_num: int, gold: int, creator: Player, accepter: Player = None):
        gid = creator.gid
        self.game_dict[gid] = Game(gid, creator, accepter, bullet_num, gold)
          
    def accept(self, accepter: Player):
        gid = accepter.gid
        if game := self.get(gid):
            if game.accepter in (accepter, None):
                game.accepter = accepter
                game.is_begin = True
                game.time = time.time()
                return game, True
    
    async def settlement(self, gid: int) -> Game:
        game = self.get(gid)
        if not game.is_begin:
            return game_dict.pop(gid)
        
        
    def get(self, gid:int) -> Game:
        return game_dict.get(gid)

class Game:
    
    def __init__(self, gid:int, creator:Player, accepter: Player = None, bullet_num: int = 2, gold: int = 200):
        self.gid = gid
        self.creator = creator
        self.accepter = accepter
        self.gold = gold
        self.bullet_num = bullet_num
        self.bullet_lst = None
        self.index = 0
        self.operator = None
        self.is_begin = False
        # self.is_end = False
        self.time = time.time()
        
    def shuffle_bullet(self):
        """
        随机子弹排列
        :param num: 装填子弹数量
        """
        if self.bullet_lst is None:
            self.operator = random.choice([self.creator, self.accepter])
            self.bullet_lst = [1] * self.bullet_num + [0] * (7 - bullet_num)
        seed = int(self.time * 1000) % 2**32  # 使用当前时间戳生成种子
        sub_lst = self.bullet_lst[self.index:]
        random.seed(seed)
        random.shuffle(sub_lst)
        np.random.seed(seed)
        np.random.shuffle(sub_lst)  # 使用numpy的随机打乱
        self.bullet_lst[self.index:] = sub_lst
    
    def istimeout(self) -> bool:
        return time.time() - self.time > 30
    
        
    async def shot(self, count: int = 1):
        shot_lst = self.bullet_lst[indexindex+count]
        if 1 in shot_lst:
            flag = self.index + shot_lst.index(1) + 1
            return random.choice(
                    [
                        '"嘭！"，你直接去世了',
                        "眼前一黑，你直接穿越到了异世界...(死亡)",
                        "终究还是你先走一步...",
                    ]
                ) + f"\n第 {flag} 发子弹送走了你..."
        else:
            self.index += count
            self.operator = self.creator if self.operator == self.accepter else self.accepter
            self.time = time.time()
            x = str(float(bullet_num) / float(7 - self.index) * 100)[:5]
            msg = f"连开{count}枪，" if count > 1 else ""