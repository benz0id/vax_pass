def user_input():
    vax_input = input("Have you been vaccinated? (Yes or No): ")
    vax = False
    if vax_input == "Yes":
        vax = True
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    
    if vax == True:
        print("{} {} has been vaccinated.".format(first_name, last_name))
    else:
        print("{} {} has not been vaccinated.".format(first_name, last_name))
    
    return vax, first_name, last_name
        