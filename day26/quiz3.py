temp_c = {
    "Monday": 4,
    "Tuesday": 5,
    "Wednesday": 10,
    "Thursday": 11,
    "Friday": 12,
    "Saturday": 14,
    "Sunday": 16,
}


temp_f = {key:(val * 9 / 5 + 32) for (key, val) in temp_c.items()}

print(temp_f)