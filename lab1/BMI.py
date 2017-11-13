# one pound is 0.45359237 kilograms and one inch is 0.0254 meters.

pounds = eval(input("Enter your weight in pounds: "));
inches = eval(input("Enter your height is inches: "));

kg = pounds * 0.45359237;
m = inches * 0.0254;

BMI = kg / (m ** 2);

print("Your BMI is: ", round(BMI, 4));
