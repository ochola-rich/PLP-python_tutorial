try:
    with open("my_file.txt", "w") as file:
        file.write("""
You still suck at programming?
Maybe it's because you don't have 3 monitors.
Maybe is because you don't grind 200 leetcodes a day.
        """)

    with open("my_file.txt", "r") as file:
        print(file.read())

    with open("my_file.txt", "a") as file:
        file.write("""
You still suck at programming because you don't watch ThePrimeagen.
Your programming skill sucks so bad that breaks chatgpt while debugging.
If you had a superhero name based on your programming skills, You will be known as Captain skill-Issue.
        """)

except FileNotFoundError:
    print("Error: File not found")

except PermissionError:
    print("Error: You don't have the required permission to open the file")

finally:
    if file:
        file.close()
    print(f"{file.name} has been closed after the successfull operations")    
 
