import pandas as pd
s = pd.Series (["X","Y", "T", "Aaba", "Baca", "CABA", None, "bird", "horse", "dog"])
a=s.str.upper()
print("uppercase: ",a)
b=s.str.lower()
print("lowercase: ",b)
c=s.str.len()
print("length: ",c)