select=""
count1=0
count2=0
count3=0
count4=0
while True :
    while True:
        try:
            Pass=int(input("Please enter your credits at pass: "))
            Defer=int(input("Please enter your credits at defer: "))
            Fail=int(input("Please enter your credits at fail: ")) 
            if Pass==120 and Defer+Fail==0:
               print("progress")
               count1 +=1
               break
            elif Pass==100 and Defer+Fail==20 :
               print("progress(module trailer)")
               count2 +=1
               break
            elif Pass==80 and Defer+Fail==40:
               print("Do not Progress – module retriever")
               count3 +=1
               break
            elif Pass==60 and Defer+Fail==60:
               print("Do not Progress – module retriever")
               count3 +=1
               break
            elif Pass==40 and Defer+Fail==80 and Defer!=0:
               print("Do not Progress – module retriever")
               count3 +=1
               break
            elif Defer+Fail==100 and Defer>=40:
               print("Do not Progress – module retriever")
               count3 +=1
               break
            elif Pass==0 and Defer>=60:
               print("Do not Progress – module retriever")
               count3 +=1
               break
            elif Pass%20!=0 or Defer%20!=0 or Fail%20!=0:
               print("Out of range!!!!!!")
               print("\n")
            elif Pass<=40 and Defer<=40:
               print("Exclude")
               count4 +=1
               break
            elif Pass+Defer+Fail!=120:
               print("Total incorrect")
            else:
               print("Invalid entry please try again")
        except:
            print("Integer required \nTry again")
            continue


    select=str(input("\nWould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results:"))
    if select == "y":
        print("\n")
        continue
    if select == "q":
        break

print("------------------------------------------------------------------- \nHistogram")
print("Progress",count1,":",count1*"*")
print("Trailer",count2,":",count2*"*")
print("Retriever",count3,":",count3*"*")
print("Excluded",count4,":",count4*"*")
outcomes = count1 + count2 + count3 + count4 
print("\n",outcomes,"outcomes in total.")
print("\n--------------------------------------------------------------------")


    
