mul_two =  lambda x: x*2

print(mul_two(2))

mul_add = lambda x,y: x*2 + y

print(  mul_add(3,4))

salary_list = [100000, 200000, 150000, 120000, 80000, 750000]


#Normal function

# def calculate_salary(base_salary, bonus_rate=.1):

#   total_salary = base_salary * ((1+ bonus_rate))
#   return total_salary

# total_salary = [calculate_salary(salary) for salary in salary_list]


total_salary_list = [(lambda x: x * 1.1) (salary) for salary in salary_list ]

total_salary_list = [salary * 1.1 for salary in salary_list ]


print(total_salary_list);
