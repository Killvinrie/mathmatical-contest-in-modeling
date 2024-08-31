import pandas as pd

df = pd.read_excel("douban_top250.xlsx", "Sheet1", engine="openpyxl")

df.head()
print(df.head(10))
print(type(df.head()))
print(df.info())

print(df["rating_num"] >= 9.5)

df_sel = df[df["rating_num"] >= 9.5]
print("dfsel",df_sel)
print("mean value =%f" % (df["rating_num"].mean()))
print("mean value =%f" % (df["rating_num"].std()))
# import pandas as pd
# import numpy as np
#
# data = {"name": ["tom", "jerry", "jake", "kevin", "niko"],
#         "height": [175 for i in range(5)],
#         "weight": [70 for i in range(5)],
#         "grade": np.random.randint(50, 100, 5)
#         }
# print(data)
# df = pd.DataFrame(data)
# print(df)
# print(df["grade"])
# print(df["grade"] == max(df["grade"]))  #how the index of max grade
# print(df[df["grade"] == max(df["grade"])])
