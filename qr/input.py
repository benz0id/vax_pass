def user_input():
    vax_input = input("Have you been vaccinated? (Yes or No): ")
    assert vax_input == "Yes" or vax_input == "No", \
        "Input must be 'Yes' or 'No'"
    
    vax = False
    if vax_input == "Yes":
        vax = True
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    
    
    birthday = int(input("What is your date of birth? (YYYYMMDD): "))
    assert birthday >= 10000000 and birthday <= 99999999, \
        "Date of birth must be valid"
    
    
    if vax == True:
        print("{} {} has been vaccinated.".format(first_name, last_name))
    else:
        print("{} {} has not been vaccinated.".format(first_name, last_name))
    
    return vax, first_name, last_name, birthday
#TODO date of birth

        