
prev_records=[]
result_dictonary = {}#https://www.geeksforgeeks.org/initialize-an-empty-dictionary-in-python/

def check_total_validation(Pass,Defer,Fail):
    total=Pass+Defer+Fail
    if total!=120:
        print('Total incorrect')
        return False
    else:
        return True
        
def progression_outcome(Pass,Defer,Fail,id):
    
    if Pass == 120:
        print('Progress')
        results="Progress"
        
    elif Pass == 100:
        print('Progress(module trailer)')
        results="Progress (module trailer)"

    elif (Pass == 40 and Fail == 80) or (Pass == 20 and Defer <= 20) or (Pass == 0 and Defer <= 40):
        print('Exclude')
        results="Exclude"
        
    elif (Pass == 80 and Defer+Fail == 40) or (Pass == 60 and Defer+Fail == 60 ) or ( Pass==40 and Defer+Fail==80 and Defer!=0 ) or (Pass==20 and Defer+Fail==100 and Fail!=100 and Fail!=80) or (Pass==0 and Defer+Fail==120 and Fail!=120 and Fail!=100 and Fail!=80) :
        print('Do not progress-module retriever')
        results="Module retriever"

    result_string = results +' - ' +str(Pass)+', '+str(Defer)+', '+str(Fail)
   
    global result_dictonary
    result_dictonary [id] = result_string
    
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
        
print("Part 4:")

while True:
    id =input('Please enter your id:')
    Pass=input_num('Please enter your credits at pass:')
    Defer=input_num('Please enter your credits at def:')
    Fail=input_num('Please enter your credits at fail:')
                
    valid = check_total_validation(Pass,Defer,Fail)
    if valid:
        progression_outcome(Pass,Defer,Fail,id)
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
      
for key, value in result_dictonary.items():#https://thispointer.com/python-4-ways-to-print-items-of-a-dictionary-line-by-line/
    print(key, ' : ', value)
