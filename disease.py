import json
import matplotlib.pyplot as plt

filename='sex_age_diagnosis.json'

age_diseases1=0
age_diseases2=0
age_diseases3=0
age_diseases4=0
age_diseases5=0
age_diseases6=0
age_diseases7=0
with open(filename) as f:
    disease_data = json.load(f)
    print(disease_data)

    for disease_dict in disease_data:
        if disease_dict['age']=="18-24":
            age_diseases1+=1
        elif disease_dict['age']=="25-34":
            age_diseases2+=1
        elif disease_dict['age']=="35-44":
            age_diseases3+=1
        elif disease_dict['age']=="13-17":
            age_diseases4+=1
        elif disease_dict['age']=="44-54":
            age_diseases5+=1
        elif disease_dict['age']=="55-64":
            age_diseases6+=1
        else:
            age_diseases7+=1

x_values=["13-17","18-24","25-34","35-44","44-54","55-64","65+"]
y_values=[age_diseases4,age_diseases1,age_diseases2,age_diseases3,age_diseases5,age_diseases6,age_diseases7]

plt.xlabel('Ages')
plt.ylabel('Amount of ailments recorded')
plt.bar(x_values,y_values)
plt.show()
