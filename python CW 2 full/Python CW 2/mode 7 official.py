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

prev_records=[]#https://www.w3schools.com/python/python_lists.asp #https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
file_name="saved_results.txt"

def check_total_validation(Pass,Defer,Fail):
    total=Pass+Defer+Fail
    if total!=120:
        print('Total incorrect')
        return False
    else:
        return True
        
def progression_outcome(Pass,Defer,Fail):
    
    if Pass == 120:
        print('Progress')
        results="Progress"
        global progress#https://stackoverflow.com/questions/74350156/unboundlocalerror-cannot-access-local-variable-command-where-it-is-not-associ
        progress+=1
    
    elif Pass == 100:
        print('Progress(module trailer)')
        results="Progress (module trailer)"
        global trailer
        trailer+=1

    elif (Pass == 40 and Fail == 80) or (Pass == 20 and Defer <= 20) or (Pass == 0 and Defer <= 40):
        print('Exclude')
        results="Exclude"
        global exclude
        exclude+=1
        
    elif (Pass == 80 and Defer+Fail == 40) or (Pass == 60 and Defer+Fail == 60 ) or ( Pass==40 and Defer+Fail==80 and Defer!=0 ) or (Pass==20 and Defer+Fail==100 and Fail!=100 and Fail!=80) or (Pass==0 and Defer+Fail==120 and Fail!=120 and Fail!=100 and Fail!=80) :
        print('Do not progress-module retriever')
        results="Module retriever"
        global retriver
        retriver+=1

    result_string = results +' - ' +str(Pass)+', '+str(Defer)+', '+str(Fail)
    global prev_records
    prev_records.append(result_string)#https://www.w3schools.com/python/ref_list_append.asp
    
    global file_name
    file = open(file_name, "a")#https://www.w3schools.com/python/python_file_write.asp #https://stackoverflow.com/questions/21839803/how-to-append-new-data-onto-a-new-line
    file.write(result_string+ "\n" )
    file.close()

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
        
file = open(file_name, "w")
file.close()

while True:
    Pass=input_num('Please enter your credits at pass:')
    Defer=input_num('Please enter your credits at def:')
    Fail=input_num('Please enter your credits at fail:')

                
    valid = check_total_validation(Pass,Defer,Fail)
    if valid:
        progression_outcome(Pass,Defer,Fail)
        while True:#cheking for 'y' or 'n'
            enter=str(input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:"))
            enter = enter.lower()#https://www.freecodecamp.org/news/how-to-lowercase-python-string/#:~:text=In%20Python%2C%20there%20is%20a,changes%20the%20strings%20to%20lowercase.
            if enter == "q" or enter == "y":
                break
            print("Invalid Input")

        if enter == "y":
            print("\n")
            continue
        elif enter == "q":
            break
      
print("------------------------------------------------------------------- ")
print("Histogrsm",'\n'"Progress",progress,"\t:",progress*"*")
print("Trailer",trailer,"\t:",trailer*"*")
print("Retriever",retriver,"\t:",retriver*"*")
print("Excluded",exclude,"\t:",exclude*"*")
outcomes = progress + trailer + retriver + exclude 
print("\n",outcomes,"outcomes in total.")
print("------------------------------------------------------------------")

print('Part 2:')

for i in range(len(prev_records)):
    print(prev_records[i])

print('\n\nPart 3:')

file = open(file_name, "r")
Lines = file.readlines()#https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/
for line in Lines:
    print(line)
    


