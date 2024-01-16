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
    
    elif pass_credits == 100:
        print('progress(module trailer)')

    elif (pass_credits == 40 and fail_credits == 80) or (pass_credits == 20 and def_credits <= 20) or (pass_credits == 0 and def_credits <= 40):
        ptint('Exclude')
        
    else:
        print('Do not progress-module retriever')
 
def input_num(massage,OR = "out of range",IR = "Intiger required"):
    
    while True:
        try:
            pass_credits=int(input(massage))
            if pass_credits<0 or pass_credits>120:
                 print(OR)
                 continue
                
            
        except ValueError:
            print(IR)
            continue

        else:
            return pass_credits
        break

pass_credits=input_num('Please enter your credits at pass:')
def_credits=input_num('Please enter your credits at def:')
fail_credits=input_num('Please enter your credits at fail:')

            
check_total_validation(pass_credits,def_credits,fail_credits)
progression_outcome(pass_credits,def_credits,fail_credits)


print('would you like to enter another set of data?')

#while True:
    #if input('Do you want to continue: ') != 'y':
        #continue
    #else:
        #break
'''
answer = None 
while answer not in ("y", "q"): 

    answer = input("Enter yes or no: ") 
    if answer == "yes": 
    
             
    elif answer == "no": 
             
    else: 
        print("Please enter yes or no.") 
'''
