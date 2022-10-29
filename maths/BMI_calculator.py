w = int(input("enter the weight"))
h = float(input("enter the height"))
x = 0
x = (w / (h**2))
if x<18.5:
          print("Underweight")
if 18.5 <= x and x<25:
          print("Normal")
if x>=25 and x<30:
          print("Overweight")
          
if x>30:
          print("Obesity")
