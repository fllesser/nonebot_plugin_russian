from .model import Player
import numpy as np
import random
import time

class GameManager:
    
    def __init__(self):
        self.game_dict = {}
        self.
   
    def ready(self, gid: int, uid: int, bullet_num: int = 2, gold: int = 200, atid: int = None):
        if cur_game := self.get(gid):
            return f'现在是 {cur_game.plr1.nickname} 发起的对决\n请等待比赛结束后再开始下一轮...'
        creator := await get_bydb(uid):
           
        accepter = 
      
        
        self.game_dict[gid] = Game(gid, creator, None, bullet_num, gold)
            
        
    def accept(self, gid: int, uid: int):
        game = self.

    def get(self, gid:int) -> Game:
        return game_dict.get(gid)

class Game:
    
    def __init__(self, gid:int, creator:Player, accepter: Player = None, bullet_num: int = 2, gold: int = 200):
        self.gid = gid
        self.creator = creator
        self.accepter = accepter
        self.gold = gold
        self.bullet_num = bullet_num
        self.bullet_lst = shuffle_bullet(bullet_num, 7)
        self.is_begin = False
        

    
    def shuffle_bullet(self, num: int, cap: int) -> List[int]:
        """
        随机子弹排列
        :param num: 装填子弹数量
        """
        seed = int(time.time() * 1000) % 2**32  # 使用当前时间戳生成种子
        bullet_lst = [1] * num + [0] * (cap - num)
        random.seed(seed)
        random.shuffle(bullet_lst)
        np.random.seed(seed)
        np.random.shuffle(bullet_lst)  # 使用numpy的随机打乱
        return bullet_lst
        
     
