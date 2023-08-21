from functions import register, login, get_breweries

while True:
    option = input("Select an option (1=Register, 2=Login, 3=Breweries, 4=Exit): ")

    if option == '1':
        username = input("Enter username: ")
        password = input("Enter password: ")
        response = register(username, password)
        print(response)

    elif option == '2':
        username = input("Enter username: ")
        password = input("Enter password: ")
        response = login(username, password)
        print(response)

    elif option == '3':
        token = input("Enter your JWT token: ")
        query = input("Enter query parameter (or press Enter for no query): ")
        response = get_breweries(token, query)
        print(response)

    elif option == '4':
        print("Exiting the program.")
        break

    else:
        print("Invalid option. Please select a valid option.")
