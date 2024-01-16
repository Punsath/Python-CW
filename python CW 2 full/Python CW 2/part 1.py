#Author:Punsath Vidunayana Perera

#I declear that my work contains no examples of misconduct,such as plagiarism,
#or collusion
#Student ID:20221072
#Date:11/12/2022

#The University progression outcomes at the end of each academic year

progress = 0
trailer = 0
exclude = 0
retriver = 0

def check_total_validation(Pass,Defer,Fail):
    total=Pass+Defer+Fail
    if total!=120:
        print('Total incorrect')
        return False
    else:
        return True
        
def progression_outcome(Pass,Defer,Fail):
    
    if Pass == 120:
        print('progress')
        global progress
        progress+=1
    
    elif Pass == 100:
        print('progress(module trailer)')
        global trailer
        trailer+=1

    elif (Pass == 40 and Fail == 80) or (Pass == 20 and Defer <= 20) or (Pass == 0 and Defer <= 40):
        print('Exclude')
        global exclude
        exclude+=1
        
    elif (Pass == 80 and Defer+Fail == 40) or (Pass == 60 and Defer+Fail == 60 ) or ( Pass==40 and Defer+Fail==80 and Defer!=0 ) or (Pass==20 and Defer+Fail==100 and Fail!=100 and Fail!=80) or (Pass==0 and Defer+Fail==120 and Fail!=120 and Fail!=100 and Fail!=80) :
        print('Do not progress-module retriever')
        global retriver
        retriver+=1

def input_num(message):
    OR = "out of range"
    IR = "Intiger required"
    while True:
        try:
            Pass=int(input(message))
            if Pass<0 or Pass>120:
                 print(OR)
                 continue
              
        except ValueError:
            print(IR)
            continue

        else:
            return Pass
        break
while True:
    Pass=input_num('Please enter your credits at pass:')
    Defer=input_num('Please enter your credits at def:')
    Fail=input_num('Please enter your credits at fail:')

                
    valid = check_total_validation(Pass,Defer,Fail)
    if valid:
        progression_outcome(Pass,Defer,Fail)
        while True:#cheking for 'y' or 'n'
            enter=str(input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:"))
            enter = enter.lower()
            if enter == "q" or enter == "y":
                break
            print("Invalid Input")

        if enter == "y":
            print("\n")
            continue
        elif enter == "q":
            break
      
print("------------------------------------------------------------------- ")
print("Histogram")
print("Progress",progress,"\t:",progress*"*")
print("Trailer",trailer,"\t:",trailer*"*")
print("Retriever",retriver,"\t:",retriver*"*")
print("Excluded",exclude,"\t:",exclude*"*")
outcomes = progress + trailer + retriver + exclude 
print("\n",outcomes,"outcomes in total.")
print("------------------------------------------------------------------")

