#Author:Punsath Vidunayana Perera

#I declear that my work contains no examples of misconduct,such as plagiarism,
#or collusion
#Student ID:20221072
#Date:11/12/2022

#The University progression outcomes at the end of each academic year

while True:
    pass_credit =input('Please enter your credits at pass:')
    if pass_credit.isdigit() and pass_credit>=0 and pass_credit <= 120:
        pass_credit = int(pass_credit)
        break
    else:
        print('Integer required')

while True:
    def_credit =input('Please enter your credits at fail:')
    if def_credit.isdigit() and def_credit>=0 and def_credit<=120:
        def_credit = int(def_credit)
        break
    else:
        print('Integer required')

while True:
    fail_credit =input('please enter your credits at fail:')
    if fail_credit.isdigit() and fail_credit>=0 and fail_credit<=120:
        fail_credit = int(fail_credit)
        break
    else:
        print('Integer required')

def input_valid_number(which="pass"):
    while True:
        n = input("enter your {} credits: ".format(which))
        
            n = int(n)
            if 0 <= n <= 120 and (n % 20) == 0:
                return n
        
            pass
while True:
    pass_credit = input_valid_number("pass")
    defer_credit = input_valid_number("defer")
    fail_credit = input_valid_number("fail")
    if sum(pass_credit, defer_credit, fail_credit) == 120:
        break
    print("Total incorrect,Please try again")
    

def progression_outcome(pass_credit,defer_credit,fail_credit):
    
    if pass_credit == 120:
        print('progress')
    
    elif passe_credit == 100:
        print('progress(module trailer)')

    elif (pass_credit == 40 and fail_credit == 80) or (pass_credit == 20 and defer_credit <= 20) or (pass_credit == 0 and defer_credit <= 40):
        ptint('Exclude')
        
    else:
        print('Do not prodree-module retriver')
 

    print(progression_outcome)
    
    
