try:
    with open('./non.txt', mode="r") as file:
        reading = file.read()
        print(reading)
    some_dict = {
        "awesome": "You are!"
    }        
    result = some_dict["wwwwwww"]
    print(result)
# avoid bare exceptions -- specify the type of error to target only that type of error to avoid catching all types of error causing unwanted behavior        
except FileNotFoundError as error_message:
    print(f"{error_message}")
    file = open("./non.txt", mode="w")
    file.write("I am some filler text!")
except KeyError as error_message:
    print(f"Could not find key: {error_message}.")    
finally: 
    print("Done!")
    file.close()
    print("Closing file...")
    raise KeyError("I'm a key error! :D")
    raise TypeError("I will not execute :(")

#   Some common types of errors to use, KeyError, ValueError, TypeError  