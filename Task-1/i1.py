h=float(input("Enter height in meters: "))
w=int(input("Enter weight in kilograms: "))
BMI=w/(h)**2
if BMI>=30:
    print("Obesity")
if BMI>=25 and BMI<=29:
    print("Overweught")
if BMI>=18.5 and BMI<25:
    print("Normal")
if BMI<18.5:
    print("Underweight")