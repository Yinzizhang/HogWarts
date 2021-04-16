from Police import Police
from Timo import Timo

class HeroFactory:
    """
    简单工厂模式专门定义一个类来负责创建其他类型的英雄的实例
    """
    # 1. 职责清晰
    # 2. 提供了一个入口。比如添加了新的英雄，其他研发调用代码的过程中，可以以factory为主，
    # 不需要一个文件一个文件去读写的内容。
    def create_hero(self, name):
        if name == "Police":
            # 如果名字是police，返回Police（）
            return Police()
        elif name == "Timo":
            # 如果名字是Timo，返回Timo（）
            return Timo()
        else:
            raise Exception("此英雄不在英雄池中")

#实例化
hero_factory = HeroFactory()

#timo实例化
timo= hero_factory.create_hero("Timo")
#police实例化
police = hero_factory.create_hero("Police")

##anny实例化,不在英雄池内抛出异常
#anny = hero_factory.create_hero("Anny")

#两个 hp 进行对比，血量剩余多的人获胜
police.fight(timo.hp, timo.power)

#打印提莫的台词
timo.speak_lines("Timo")

#打印police的台词
timo.speak_lines("Police")