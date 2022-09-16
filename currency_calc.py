
"""currency calculator. The user can choose one of three currencies (PLN, Euro, USD) and convert a specific value.
 The calculator should display the round value to two decimal places."""

#Todo: jesli chodzi o klasy z currency to lepiej zrobic albo slowniki
#Todo: jesli chodzi o pln = float(0.21) - to mozna bez tego float
#Todo: nie wiem czego dotyczylo zadanie ale jesli chodzi o drugie zdjecie to nie wiem czy uzywal bym dziedziczenia
# - raczej nie - wszystko w jednej klasie

#Todo: bez funkcji _init_
#Todo: zmienne bezposrednio w funkcjach
#Todo: i uzywal metod statycznych cos z tego
# https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner

currency = {"Euro": 4.75, "USD": 4.70, "PLN": 0.21}

print(currency["Euro"])


def current_rates(currency):
    for key, value in currency.items():
        yield key,value

print (f"Welcome to the currency calculator. The current exchange rates are as follows:\n\n", {list(current_rates(currency)}))

type1= int(input("\nWhat currency do you want to exchange?: 1 = USD, 2 = EURO: "))


def type_of_currency():
    if type1 == 1:
        return "USD"
    elif type1 == 2:
        return "EURO"
    else:
        print ("error!")

def currency_choice():

    if type1 == 1:
        return usd
    elif type1 == 2:
        return euro
    else:
        print("error")

class BuyCurrency:
    def __init__(self,curr1, curr2):
        self.curr1 = curr1
        self.curr2 = curr2
    def conversion(self):
        return round(self.curr1 / self.curr2,2)

class SellCurrency(BuyCurrency):
    def conversion2(self):
        return round(self.curr2 / self.curr1, 2)


sell1 = float(input(f"How much PLN do you want to exchange into {type_of_currency()}?: "))
buy1 = float(input(f"How much {type_of_currency()} do you want to exchange into PLN: "))


sellobject = BuyCurrency (sell1,currency_choice())
sellobject2 = BuyCurrency (sell1,currency_choice())
buyobject = SellCurrency (pln,buy1)
print (sellobject.conversion(), type_of_currency())
print (buyobject.conversion2(), "PLN")


