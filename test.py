#weight_pounds = input('Plase enter your weight in pounds ')
#weight_convertor = float(weight_pounds) * 0.453
#print('Your weight is ' + str(weight_convertor) + ' kg ')


#good_credit = True
#house_price = 1000000
#if good_credit:
#   down_payment =  (house_price * 0.1)
#else:
#    down_payment = (house_price * 0.2)
#print(f'down_payment: {down_payment} $')


name = input("Enter your name: ")
if len(name) < 3:
    print("Name must be at least 3 characters. ")
elif len(name) > 50:
    print("Name cannot exceed 50 characters. ")
else:
    print("Name looks good ")

