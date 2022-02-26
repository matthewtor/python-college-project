
print("Blackwater Annual Music Concert")
print(" -------------------------------")

first = "1. Adding performers"

second = "2. Quit"
Annual_Concert = "Blackwater Annual Music Concert"
lines = "-------------------------------"
command = int(input(f" {first}\n {second}\n ==> " ))



if command == 1:
    performer_page = open("performer.txt", "a")
    print( " (1) Adding performers ")
    print("------------")

    performers = int(input("How many performers are you adding:  "))
    Singer = 0
    Dancer = 0
    Musician = 0

    total = 0



    r = 1

    n = 3

    i = 0
    page = ""
    longest_time = 0
    while i < performers and r <= n:
        print(f"Booking {i + 1} / {performers} :")
        name = input("Enter your name : ")
        surname = input("Enter your surname : ")
        print("Type of performance")
        print("1. Musical")
        print("2. Singer")
        print("3. Dance")
        option_two = int(input(" ==>: "))
        if option_two == 1:
            type = "Musician"
            code = "(Musician)"
            Musician += 1
        elif option_two == 2:
            type = "Singer"
            code = "(Singer)"
            Singer += 1
        else:
            type = "Dancer"
            code = "(Dancer)"
            Dancer += 1

        time = int(input("Time slot required(mins): "))
        if time > longest_time:
            longest_time = time
            longest_name = name  + " " + surname + " " + code
        total += time
        i = i + 1
        r += 1
        info =("The following information has been added.")

        string = f"{i}. {surname},{name}  {type}  {time} minutes \n "
    print(string.rstrip(), file=performer_page)
    performer_page.close()
    page = page + string


    print(info)
    print(page)

    print("Summary Notes:")
    print("-----------")

    if Singer > 1 or Singer == 0:
       print(f"{Singer} Singers")
    else:
        print(f"{Singer} Singer")

    if Dancer > 1 or Dancer == 0:
        print(f"{Dancer} Dancers")
    else:
        print(f"{Dancer} Dancer")

    if Musician >1 or Musician == 0:
        print(f"{Musician} Musicians")
    else:
        print(f"{Musician} Musician")

    if total < 60:
        print(f"Total time required is 0 hour(s), {total} min(s) ")
    else:
        print(f"Total time required is 1 hour(s), {total - 60 } min(s) ")

    print(f"The longest act added is {longest_name } {longest_time } minutes.  ")
    total_command = int(input(f"\n {Annual_Concert}\n {lines}\n {first}\n {second}\n {third}\n ==> "))



else:
    print("")
