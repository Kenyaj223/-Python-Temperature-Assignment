# Temperature and humdity readings
temp1 = 22
temp2 = 24
temp3 = 23
humdity1 = 48
humdity2 = 52
humdity3 = 50

# Calculate the moving average
avg_temp = (temp1 + temp2 + temp3) / 3 

avg_humdity = (humdity1 + humdity2 + humdity3) / 3 

# Print the averages

print(f"Moving avergae temperature:{avg_temp}")
print(f"Moving average humdity: {avg_humdity}")

# Check if the temperature is in the normal range (18 to 25)

if avg_temp >= 18 and avg_temp <= 25 :
    print(f"The temperature is normal")
if avg_temp > 25: 
    print("The temperature is high")
else:
    print("The temperature is low")