#Author:Punsath Vidunayana Perera

#I declear that my work contains no examples of misconduct,such as plagiarism,
#or collusion
#Student ID:20221072
#Date:11/12/2022

#The University progression outcomes at the end of each academic year

def check_total_validation(pass_credits,defer_credits,fail_credits):
    total=pass_credits+defer_credits+fail_credits
    if total!=120:
        print('Total incorrect')
        return
        
def progression_outcome(pass_credit,defer_credit,fail_credit):
    
    if pass_credits == 120:
        print('progress')
        progress=progress+1
    
    elif pass_credits == 100:
        print('progress(module trailer)')
        trailer=trailer+1

    elif (pass_credits == 40 and fail_credits == 80) or (pass_credits == 20 and def_credits <= 20) or (pass_credits == 0 and def_credits <= 40):
        print('Exclude')
        Exclude=Exclude+1
    else:
        print('Do not progress-module retriever')
        module_retriver=module_retriver+1

progress=0
trailer=0
Exclude=0
module_retriver=0

while True:
    try:
        pass_credits=int(input('Please enter your credits at pass:'))
        
        if pass_credits<0 or pass_credits>120:
             print('out of range')
        else:
            break
    except ValueError:
        print('Integer required')
       
while True:
    try:
        def_credits=int(input('Please enter your credits at def:'))
        
        if def_credits<0 or def_credits>120:
             print('out of range')
        else:
            break
    except ValueError:
        print('Integer required')

while True:
    try:
        fail_credits=int(input('Please enter your credits at fail:'))
        
        if fail_credits<0 or fail_credits>120:
             print('out of range')
        else:
            break
    except ValueError:
        print('Integer required')
        
check_total_validation(pass_credits,def_credits,fail_credits)
progression_outcome(pass_credits,def_credits,fail_credits)

print('would you like to enter another set of data?')
while True:
    try:
        continue_exit=str(input("Enter 'y' for yes or 'q' to quit:"))
        answer="y" or "q"

        if answer == "y":
            continue
        else:
            break
    
    except ValueError:
        print('please enter valid answer')

            
            


