print("welcome to the interactive personal data collector!")
name=input("enter the name of student:")
age=int(input("enter the age of student:"))
height=float(input("enter the height in meters:"))
fav_number=input("enter the favorite number:")
print("thank you! here is the information we collected:")
print(f"name:{name},{type(name)}")
print("memory_address:id{name}(decimal)")
print(f"age:{age},type:{type(age)}")
print(f"memory_address:{id(age)}(decimal)")
print(f"height:{height},type:{type(height)}")
print(f"memory_address:{id(height)}(decimal)")
print(f"fav_number:{fav_number},type:{type(fav_number)}")
print(f"memory_address:{id(fav_number)}(decimal)")
birth_year=2024- age
print(f"your birth year is approximately")
print(f"birth_year:{birth_year}")
print(f"thank you for using the personal data collector.goodbye")