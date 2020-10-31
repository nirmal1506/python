x = int(input("Enter your marks :"))
if x > 90 and x <= 100:
    print("got A grade")
elif x > 80 and x <= 90:
    print("got B grade")
elif x > 60 and x <= 80:
    print("got C garde")
elif x > 40 and x <= 60:
    print("got D grade")
elif x < 40:
    print("Sorry! You are fail")
else:
    print("invalid marks")