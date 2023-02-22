print("Hello World")
mydic={
    "Employee1":{
      "Name":"Sudit1",
    "Age":"20",
    "ID":"1",
    "Salary":67
    },
    "Employee2":{
      "Name":"Sudit2",
    "Age":"20",
    "ID":"2",
    "Salary":432
    },
    "Employee3":{
      "Name":"Sudit3",
    "Age":"20",
    "ID":"3",
    "Salary":560
    },
    "Employee4":{
      "Name":"Sudit4",
    "Age":"20",
    "ID":"4",
    "Salary":100
    },
    "Employee5":{
      "Name":"Sudit5",
    "Age":"20",
    "ID":"5",
    "Salary":230
    },
}
a=mydic.get("Employee1")
b=mydic.get("Employee2")
c=mydic.get("Employee3")
d=mydic.get("Employee4")
e=mydic.get("Employee5")

if a["Salary"]>b["Salary"] and a["Salary"]>c["Salary"] and a["Salary"]>d["Salary"] and a["Salary"]>e["Salary"]:
  print(a["Name"])
elif b["Salary"]>a["Salary"] and b["Salary"]>c["Salary"] and b["Salary"]>d["Salary"] and b["Salary"]>e["Salary"]:
  print(b["Name"])
elif c["Salary"]>a["Salary"] and c["Salary"]>b["Salary"] and c["Salary"]>d["Salary"] and c["Salary"]>e["Salary"]:
  print(c["Name"])
elif d["Salary"]>a["Salary"] and d["Salary"]>c["Salary"] and d["Salary"]>b["Salary"] and d["Salary"]>e["Salary"]:
  print(d["Name"])
else :
  print(e["Name"])

