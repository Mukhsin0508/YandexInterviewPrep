# Convert temperatures between Fahrenheit and Celsius

# Step 1: Print a message asking the user to enter the temperature
print ( "Please enter the temperature: " )

# Step 2: Read the temperature from the user input
temp1 = input ( )

# Step 3: Print a message asking the user to enter the unit of the temperature
print ( "Please enter the unit of the temperature (F/C): " )

# Step 4: Read the unit of the temperature from the user input
unit = input ( )

# Step 5: Convert the temperature to the other unit
if unit == "F" or unit == "f" :
    temp2 = (float ( temp1 ) - 32) * 5 / 9
    new_unit = "Celsius"
    print ( "The temperature in" , new_unit , "is:" , temp2 )
elif unit == "C" or unit == "c" :
    temp2 = (float ( temp1 ) * 9 / 5) + 32
    new_unit = "Fahrenheit"
    print ( "The temperature in" , new_unit , "is:" , temp2 )
else :
    print ( "Invalid unit. Please enter F or C." )
    exit ( )
