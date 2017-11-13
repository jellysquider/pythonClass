investmentAmount = eval(input("Enter the investment amount: "));
annualInterestRate = eval(input("Enter the annual interest rate: "));
numberOfYears = eval(input("Enter the number of years: "));

numberOfMonths = 12 * numberOfYears;
monthlyInterestRate = (annualInterestRate / 100) / numberOfMonths;
futureInvestmentValue = investmentAmount * ((1 + monthlyInterestRate) ** numberOfMonths);

print("Accumulated value is: ", int(futureInvestmentValue * 100) / 100);
