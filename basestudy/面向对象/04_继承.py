class mammai:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.num_eyes = 2

    def breath(self):
        print(f'{self.name}在呼吸')

    def poop(self):
        print(f'{self.name}在拉屎')


class Human(mammai):
    def __init__(self,name,sex):
        super().__init__(name,sex)
        self.has_tail=False
        self.human_color="黄色"
    def read(self):
        print(f'{self.name}在阅读')


class Cat(mammai):
    def __init__(self, name, sex):
        super().__init__(name, sex)
        self.cat_type = "狸花猫"
        self.has_tail=True


    def scratch(self):
        print(f'{self.name}是{self.cat_type}')
        print(f'{self.name}在抓老鼠')

    def poop(self):
        print(f'{self.name}在猫砂盆拉屎')


cat1 = Cat("小白", "男")
cat1.poop()
cat1.breath()
cat1.scratch()
