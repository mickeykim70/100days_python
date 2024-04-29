student_dict = {
    "student": ["Angela", "Bob", "Jim"],
    "score": [90, 56, 78],
}
#
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

import pandas as pd
df = pd.DataFrame(student_dict)

# print(df)
for (key, value) in df.items():
    print(key, value)

