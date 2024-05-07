import pandas as pd

data_1 = {
    'name2': ['王小郭', '張小華', '廖丁丁', '丁小光'],
    'email': ['min@gmail.com', 'hchang@gmail.com', 'laioding@gmail.com', 'hsulight@gmail.com'],
    # 'grades': [60, 77, 92, 43]
}

data_2 = {
    'name': ['黃明明', '汪新新', '鮑呱呱', '江組組'],
    # 'email': ['ww@gmail.com', 'cc@gmail.com', 'bb@gmail.com', 'ee@gmail.com'],
    'grades': [70, 17, 32, 43]
}

# 建立 DataFrame 物件
student_df_1 = pd.DataFrame(data_1)
student_df_2 = pd.DataFrame(data_2)

# print(student_df_1)
# print(student_df_2)
# print(pd.concat([student_df_1, student_df_2], ignore_index=True))


data_3 = {
    'name': ['王小郭', '張小華', '廖丁丁', '丁小光'],
    'email': ['min@gmail.com', 'hchang@gmail.com', 'laioding@gmail.com', 'hsulight@gmail.com'],
    'grades': [60, 77, 92, 43]
}

data_4 = {
    'name': ['王小郭', '張小華2', '廖丁丁3', '丁小光4'],
    'email': ['min@gmail.com', 'hchang@gmail.com2', 'laioding@gmail.com3', 'hsulight@gmail.com4'],
    'age': [19, 20, 32, 43]
}

# 建立 DataFrame 物件
student_df_3 = pd.DataFrame(data_3)
student_df_4 = pd.DataFrame(data_4)
student_merge = pd.merge(student_df_3, student_df_4)
print(student_merge)
