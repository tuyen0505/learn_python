def main():
    CURRENT_YEAR = 2021
    METER_TO_FEET = 3.281

    first_name = input("your firstname: ")
    last_name = input("your lastname: ")
    year_born = input("when you were born: ")
    height_meter = input("you hight (meter): ")

    year_born = int(year_born)

    age = CURRENT_YEAR - year_born

    height_meter = float(height_meter)
    height_feet = height_meter * METER_TO_FEET
    height_feet = round(height_feet,1)

    print("_____________________________")
    print("your name is: " + first_name + last_name)
    print(f"{first_name} is {age} year old in {CURRENT_YEAR}")
    print("you are " + str(height_feet) + " feet tall")

    list_answer = ["yes", "no"]
    while True:
        gender_input = input("are you male (yes/no): ")
        if gender_input.lower() == "yes" or gender_input.lower() == "no":
            break

    is_male = None

    if gender_input.lower() == "yes":
        is_male = True
    elif gender_input.lower() == "no":
        is_male = False

    if is_male == None:
        print("INVALID ANSWER")
    elif is_male == True:
        if height_feet > 6.5:
            print("you are very tall as a man")
        elif height_feet > 6.0:
            print("you are tall as a man")
        else:
            print("you are short as a man")
    elif is_male == False:
        if height_feet > 5.7:
            print("you are tall as a man")
        else:
            print("you are short as a man")
    else:
        print("Systym error: Variable 'is_male' is'nt correct")

main()