
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
 
while True:
    try:
        pass_credits=int(input('Please enter your credits at pass:'))
        def_credits=int(input('Please enter your credits at def:'))
        fail_credits=int(input('Please enter your credits at fail:'))
        if pass_credits<0 or pass_credits>120:
             print('out of range')
        else:
            break
    except ValueError:
        print('Integer required')
            
        if def_credits<0 or def_credits>120:
             print('out of range')
        else:
            break
    except ValueError:
        print('Integer required')

        
        if fail_credits<0 or fail_credits>120:
             print('out of range')
        else:
            break
    except ValueError:
        print('Integer required')



