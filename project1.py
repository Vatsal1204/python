print("welcome to the interactive personal data collector!")
name=input("enter the name of student:")
age=input("enter the age of student:")
height=input("enter the height in meters:")
fav_number=input("enter the favorite number:")
print("thank you! here is the information we collected:")
print(f"name:{name},{type(name)}")
print("memory_address:id{name}(decimal)")
print(f"age:{age},type:{type(age)}")
memory_address=id(age)
print(f"memory_address:{memory_address}(decimal)")
print(f"height:{height},type:{type(height)}")
memory_address=id(height)
print(f"memory_address:{memory_address}(decimal)")
print(f"fav_number:{fav_number},type:{type(fav_number)}")
print(f"memory_address:{id(fav_number)}(decimal)")
birth_year=2024- age
print(f"your birth year is approximately")
print(f"birth_year:{birth_year}")
print(f"thank you for using the personal data collector.goodbye")