# take the input
name = input("Enter the Employee's name: ");
hrs_wk = eval(input("Enter the number of hours worked in a week: "));
rate_hr = eval(input("Enter the hourly pay rate: "));
fed_tax = eval(input("Enter the federal tax withholding rate: "));
state_tax = eval(input("Enter the state tax withholding rate: "));

gross_pay = hrs_wk * rate_hr;
fed_deductible = (20 * gross_pay) / 100;
state_deductible = (9 * gross_pay) / 100;
total_deduction = fed_deductible + state_deductible;
net = gross_pay - total_deduction;

print("Employee Name: ", name);
print("Hours Worked: ", format(hrs_wk, "<.1f"));
print("Pay Rate: $", rate_hr);
print("Gross Pay: $", gross_pay);
print("Deductions:")
print(format("Federal Withholding (20.0%): $", ">32s"), fed_deductible);
print(format("State Withholding (9.0%): $", ">29s"), int(state_deductible * 100) / 100);
print(format("Total Deductions: $", ">21s"), int(total_deduction * 100) / 100);
print("Net Pay: $", format(net, "<.2f"));
