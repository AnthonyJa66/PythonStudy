
class ATM:
    def __init__(self,id,bank,branch):
        self.id=id,
        self.bank=bank,
        self.branch=branch

class MoneyPaper:
    def __init__(self,id,value,year):
        self.id=id,
        self.value=value,
        self.year=year

atm1=ATM("010","中国银行","上海支行")
money1=MoneyPaper("001",100,2023)


def getmoney(ATM,MoneyPaper):
    print(f"在{ATM.bank}的{ATM.branch}的{ATM.id}编号ATM中取了{MoneyPaper.value}钞票编号是{MoneyPaper.id}的")

getmoney(atm1,money1)
