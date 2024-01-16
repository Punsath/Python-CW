#Author:Punsath Vidunayana Perera

#I declear that my work contains no examples of misconduct,such as plagiarism,
#or collusion
#Student ID:20221072
#Date:11/12/2022

#The University progression outcomes at the end of each academic year

progress=0
trailer=0
exclude=0
retriver=0

def check_total_validation(Pass,Defer,Fail):
    total=Pass+Defer+Fail
    if total!=120:
        print('Total incorrect')
        
def progression_outcome(Pass,Defer,Fail):

    while True:

        if Pass == 120:
            print('progress')
            progress+=1
            break
        
        elif Pass == 100:
            print('progress(module trailer)')
            trailer+=1
            break

        elif (Pass == 40 and Fail == 80) or (Pass == 20 and Defer <= 20) or (Pass == 0 and Defer <= 40):
            print('Exclude')
            exclude+=1
            break
            
        elif (Pass == 80 and Defer+Fail == 40) or (Pass == 60 and Defer+Fail == 60 ) or ( Pass==40 and Defer+Fail==80 and Defer!=0 ) or (Pass==20 and Defer+Fail==100 and Fail!=100 and Fail!=80) or (Pass==0 and Defer+Fail==120 and Fail!=120 and Fail!=100 and Fail!=80) :
            print('Do not progress-module retriever')
            retriver+=1
            break

def input_num(massage,OR = "out of range",IR = "Intiger required"):
    
    while True:
        try:
            Pass=int(input(massage))
            if Pass<0 or Pass>120:
                 print(OR)
                 continue
              
        except ValueError:
            print(IR)
            continue

        else:
            return Pass
        break

Pass=input_num('Please enter your credits at pass:')
Defer=input_num('Please enter your credits at def:')
Fail=input_num('Please enter your credits at fail:')

            
check_total_validation(Pass,Defer,Fail)
progression_outcome(Pass,Defer,Fail)

while True:
    enter=str(input("\nWould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results:"))
    if enter == "y":
        print("\n")
        continue
    if enter == "q":
        break

print("------------------------------------------------------------------- ")
print("Histogram")
print("Progress",progress,":",progress*"*")
print("Trailer",trailer,":",trailer*"*")
print("Retriever",retriver,":",retriver*"*")
print("Excluded",exclude,":",exclude*"*")
outcomes = progress + trailer + retriver + exclude 
print("\n",outcomes,"outcomes in total.")
print("\n------------------------------------------------------------------")

print('Part 2')

list1 = []
while True:
    element = input("enter the elemenet")
    list1.append(element)

print("Progress:",list1)
print("Progress (module trailer):",list2)
print("Module retriever:",list3)
print("Moduler retriver:",list4)
print("Exclude:",list5)