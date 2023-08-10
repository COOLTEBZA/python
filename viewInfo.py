import userInfo as u1

#getDefaultValue
print(u1.user_data[0])
print(u1.user_data[1])
print(u1.user_data[2])
print(u1.user_data[3])

#setValue
u1.user_data[0] = "0"
u1.user_data[1] = "1"
u1.user_data[2] = "2"
u1.user_data[3] = "3"

#get (Changed/Replace/removed/clearFeild/clearString) Value
print(u1.user_data[0])
print(u1.user_data[1])
print(u1.user_data[2])
print(u1.user_data[3])

#When you close the app data becomes default or reseted
#If the code doesn't work Python language may have new features this is for py 3 version
