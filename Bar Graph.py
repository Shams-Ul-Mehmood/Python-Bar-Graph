import matplotlib.pyplot as plt

# Sample Data
malware_Classes = [ "worm" , "virus" , "ransomware" , "keylogger" , "rat" , "spyware" , "botnet" ]
values = [ 45 , 10 , 30 , 24 , 14 , 70 , 98 ]

# Bar Graph Creation
plt.bar( malware_Classes , values )

# Add title and labels
plt.xlabel(" Malware Classes ")
plt.ylabel( " Values " )
plt.title( "Malware Impact Graph" )

plt.show()