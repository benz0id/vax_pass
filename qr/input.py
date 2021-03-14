def user_input():
    # asks vaccination status (must be 'Yes' or 'No')
    while vax_input != "Yes" or vax_input != "No":
        vax_input = input("Have you been vaccinated? (Yes or No): ")
    
    # converts to Boolean
    vax = False
    if vax_input == "Yes":
        vax = True
        
    # gets name
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    
    # gets birthday (must be 8 digits)
    while birthday < 10000000 or birthday > 99999999:
        birthday = int(input("What is your date of birth? (YYYYMMDD): "))
    
    #prints either statement depending on user answers.
    if vax == True:
        print("{} {} has been vaccinated.".format(first_name, last_name))
    else:
        print("{} {} has not been vaccinated.".format(first_name, last_name))
    
    return vax, first_name, last_name, birthday


        
