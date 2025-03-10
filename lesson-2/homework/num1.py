num = float(input("Enter a float number: "))
temp_num = num * 100;
if temp_num > 0:
    temp_num += 0.5
else:
    temp_num -= 0.5
rounded_num = int(temp_num)/100
print("Rounded number: ", rounded_num)
