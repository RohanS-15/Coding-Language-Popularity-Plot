import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file = pd.read_csv("data.csv")
list = file["LanguagesWorkedWith"].tolist()

x = ["Python", "JavaScript", "HTML/CSS", "C++", "C#"]

pythonCounter  = 0
javascriptCounter = 0
htmlCounter = 0
CppCounter = 0
CsCounter = 0

for langs in list:
    if "Python" in langs:
        
        pythonCounter += 1
    if "JavaScript" in langs:
        javascriptCounter += 1
    if "HTML/CSS" in langs:
        htmlCounter += 1
    if "C++" in langs:
        CppCounter += 1
    if "C#" in langs:
        CsCounter += 1
 
y = [pythonCounter, javascriptCounter, htmlCounter, CppCounter, CsCounter]
print(f"Python: {pythonCounter}, JavaScript: {javascriptCounter}, HTML/CSS: {htmlCounter}, C++: {CppCounter}, C#: {CsCounter}")
plt.bar(x,y, color = "black") 


plt.xlabel("Languages")
plt.ylabel("Num of people using the languages(out of 88863 people)")
plt.title("Amount of people who use programming languages")                  
plt.show()