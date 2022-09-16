import datetime
from datetime import date

class Budget_Prediction:
    months = 12
    current_day = date.today()
    budget = float(input("Enter your current amount: "))
    income = float(input("What is your income per month: "))
    expenses = float(input("What are your expenses per month: "))
    target_budget = float(input("What is your year-end budget goal?: "))
    month = (months - current_day.month)

    def __init__(self):
        self.prediction = None
        self.next_year = None

    @property
    def budget_predict(self):
        self.prediction = self.budget + (self.income - self.expenses) * self.month
        return self.prediction

    def diff_target_budget(self):
        self.diff = (self.budget + (self.income - self.expenses) * self.month) - self.target_budget
        return self.diff

    def next_years_forecast(self):
        self.next_year = (self.budget + (self.income - self.expenses) * self.month) + ((self.income - self.expenses)*12)
        return self.next_year

    def five_years_forecast(self):
        self.five_years = (self.budget + (self.income - self.expenses) * self.month) + ((self.income - self.expenses)*12*5)
        return self.five_years

    def ten_years_forecast(self):
        self.ten_years = (self.budget + (self.income - self.expenses) * self.month) + ((self.income - self.expenses)*12*10)
        return self.ten_years



forecast = Budget_Prediction()
finalforecast = forecast.budget_predict
diff_target = Budget_Prediction()
result =  diff_target.diff_target_budget()
next_year = Budget_Prediction()
next_year_result = next_year.next_years_forecast()
five_years = Budget_Prediction()
five_years_result = five_years.five_years_forecast()
ten_years = Budget_Prediction()
ten_years_result = ten_years.ten_years_forecast()

print("\n")

if finalforecast > 0:
    print (f"By the end of the year you will save: {finalforecast} ")
    if result > 0:
        print (f"Your savings plan will generate a surplus over your target budget: {result}")
    else:
        if result == 0:
            print ("Bravo! The implementation of the assumptions will allow you to achieve your goal")
        else:
            print (f"To the target budget missing: {result}")
else:
    print (f"By the end of the year, you will generate a gap of: {finalforecast}")

print ("\n--- Long term perspective and recommendations ---")

print ("\nAt the end of the next year, your account will include: ", next_year_result)
print("In five years, there will be: ", five_years_result)


#dodać informacje ile miesięcznie więcej musi oszczędzać aby wyjść na 0. In future create a set with text assigne to the values
def long_perspective():
    long_perspective = ten_years_result
    if next_year_result < 0:
        print (f"In ten years you will have a gap: {long_perspective}. It's time to start saving!!")
        cover_gap = ten_years_result/10/12
        print (f"Start saving {cover_gap} more monthly and you will achieve break-even.")
    elif next_year_result <= 5000:
        print (f"In ten years you'll have it on your account: {long_perspective}. You can buy a lot for this amount!")
    elif next_year_result <= 10000:
        if long_perspective <= 70000:
            print (f"In ten years you'll have it on your account: {long_perspective}. "
                   f"You can buy a 2-year-old car or wait a moment more and the new car will be yours!")
        else:
            print (f"In ten years you'll have it on your account: {long_perspective}. The new car could be yours!")
    elif next_year_result <= 25000:
        print (f"In ten years you'll have it on your account: {long_perspective}. "
               f"For this amount, you can buy yourself a nice car!")
    else:
        if long_perspective < 1000000:
            print (f"Your savings are impressive! In ten years you'll have it on your account: {long_perspective} ")
        else:
            print (f"In ten years you'll have it on your account: {long_perspective}. You will be a millionaire so buy "
               f"yourself what you want!")

long_perspective()


















