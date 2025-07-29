# data = {
#   "name": "Pushpak",
#   "education": "MCA",
#   "college": "NSHM Academy",
#   "Marks":[56,67,55,78,]
# }

# print(data)
# print(type(data))
# print(data["Marks"])
# data["name"] = "Pushpak Jha"
# print(data["name"])

# data["Roll No"] = 22854
# print(data)



data = {
  "name": "Pushpak",
  "education": "MCA",
  "college": "NSHM Academy",
  "Marks":[56,67,55,78,],
  "subject" :{
    "physics":56,
    "chemistry":66,
    "biology":50,
    "history":70,
    "geography":45
  }
}

print(data["subject"]["chemistry"])

print(data.keys())  # Print all keys
print(list(data))  # convert dictionary to list
print(len(data))