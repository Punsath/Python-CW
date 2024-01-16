#Author:Punsath Vidunayana Perera

#I declear that my work contains no examples of misconduct,such as plagiarism,
#or collusion
#Student ID:20221072
#Date:11/12/2022

#The University progression outcomes at the end of each academic year

marks


def progression_outcome(pass_credit,defer_credit,fail_credit):
    
    if pass_credit == 120:
        print('progress')
    elif passe_credit == 100:
        print('progress(module trailer)')
    elif pass_credit == 80 and defer_credit == 20:
        print('Do not progress-module retriever')
    elif pass_credit == 80 and defer_credit == 20 and fail_credit == 20:
        print('Do not progress-module retriever')
    elif pass_credit == 80 and fail_credit == 40:
        print('Do not progress-module retriever')
    elif pass_credit == 60 and defer_credit == 60:
        print('Do not progress-module retriever')
    elif pass_credit == 60 and defer_credit == 40 and fail_credit == 20:
        print('Do not progress-module retriever')
    elif pass_credit == 60 and defer_credit == 20 and fail_credit == 40:
        print('Do not progress-module retriever')
    elif pass_credit == 60 and fail_credit == 60:
        print('Do not progress-module retriever')
    elif pass_credit == 40 and defer_credit == 80:
        print('Do not progress-module retriever')
    elif pass_credit == 40 and defer_credit == 60 and fail_credit == 20:
        print('Do not progress-module retriever')
    elif pass_credit == 40 and defer_credit == 40 and fail_credit == 40:
        print('Do not progress-module retriever')
    elif pass_credit == 40 and defer_credit == 20 and fail_credit == 60:
        print('Do not progress-module retriever')
    elif pass_credit == 40 and fail_credit == 80:
        print('Exclude')
    elif pass_credit == 20 and defer_credit == 100:
        print('Do not progress-module retriever')
    elif pass_credit == 20 and defer_credit == 80 and fail_credit == 20:
        print('Do not progress-module retriever')
    elif pass_credit == 20 and defer_credit == 60 and fail_credit == 40:
        print('Do not progress-module retriever')
    elif pass_credit == 20 and defer_credit == 40 and fail_credit == 60:
        print('Do not progress-module retriever')
    elif pass_credit == 20 and defer_credit == 20 and fail_credit == 80:
        print('Exclude')
    elif pass_credit == 20 and fail_credit == 100:
        print('Exclude')
    elif defer_credit == 120:
        print('Do no progress-module retriver')
    elif defer_credit == 100 and fail_credit == 20:
        print('Do not progress-module retriever')
    elif defer_credit == 80 and fail_credit == 40:
        print('Do not progress-module retriever')
    elif defer_credit == 60 and fail_credit == 60:
        print('Do not progress-module retriever')
    elif defer_credit == 40 and fail_credit == 80:
        print('Exclude')
    elif defer_credit == 20 and fail_credit == 100:
        print('Exclude')
    elif fail_credit == 120:
        print('Exclude')

response_1 = int(input('Please enter your credits at pass '))
if response_1 == str:
    print('Integer required')
elif response_1 >120:
    print('Out of range')

    
response_2 = int(input('Please enter your credits at defer '))
if response_2 == str:
    print('Integer required')
elif response_2 >120:
    print('Out of range')

    
response_3 = int(input('Please enter your credits at fail '))
if response_3 == str:
    print('Integer required')
elif response_3 >120:
    print('Out of range')

    
    
    
    
    

