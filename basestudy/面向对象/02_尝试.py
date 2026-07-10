class cutecat:
    def __init__(self,cat_name,cat_age,cat_color):
        self.name=cat_name
        self.age=cat_age
        self.color=cat_color

    def speak(self):
        print("喵"*self.age)


cat1=cutecat("小白",3,"黄色")
cat1.speak()