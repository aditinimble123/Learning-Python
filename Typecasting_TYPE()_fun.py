# type() fun is used to konw the data type of given variable
a = 43 
t = type(a) #class <int>
print(t)
b = 43.41 
t = type(b) #class <float>
print(t)
c = "aditi" 
t = type(c) #class <char>
print(t)

# You can change data types using type() fun
d="31.2" # here 31 is float but using"" we converted it into the string
t = type(d)
print(t)

# Type conversion
e=float(d)  #here we changed datatype of d to float and stored it into e
t=type(e)
print(t)