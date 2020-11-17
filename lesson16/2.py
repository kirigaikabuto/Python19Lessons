n = int(input())
a = {
    "name": "yerassyl",
    "age": 16,
    "salary": 2000,
    "experience": 2,
}
# print(a["job"])
if n == 1:
    a["job"] = "IT"
    # job
else:
    a["freelance"] = "WEB"
    # freelance
print(a["job"])
