import matplotlib.pyplot as plt
import sqlite3


years = []
co2_value = []
temp_value = []


# Connect to the SQLite database
connect_SQL = sqlite3.connect('climate.db')
cursor = connect_SQL.cursor()

# Get data from the ClimateData table
cursor.execute('SELECT Year, CO2, Temperature FROM ClimateData')
data = cursor.fetchall()

for row in data:
    year, co2, temperature = row
    years.append(year)
    co2_value.append(co2)
    temp_value.append(temperature)

# Close the database connection
connect_SQL.close()

# Print the fetched data (optional)
for year, co2, temperature in zip(years, co2_value, temp_value):
    print(f'Year: {year}, CO2: {co2}, Temperature: {temperature}')




plt.subplot(2, 1, 1)
plt.plot(years, co2_value, 'b--')
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp_value, 'r*-')
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png") 
