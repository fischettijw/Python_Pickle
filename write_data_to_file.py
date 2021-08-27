# https://www.youtube.com/watch?v=qt15PnF8x-M
import pickle
import os

os.system("cls")

# region Initialize
print("===== Python Data To and From Text File =====\n")

my_text = "Hello World"
my_integer = 1_234_567
my_list = [1, 56, "hello", (12, 23, 5.67, "goodbye")]
my_dict = {"a": 123, "b": 234, "c": ["abc", 1, 4.5]}
my_float = 3.14159

my_data = [my_text, my_integer, my_list, my_dict, my_float]

print("*** Data BEFORE Text File Write & Read ***\n")

print(my_text)
print(my_integer)
print(my_list)
print(my_dict)
print(my_float)
print("-" * 40)
print(my_data)
print("-" * 40)
print()

# endregion Initialize

# region Text File

print("*** Data AFTER Text File Write & Read ***\n")

with open("data_output.txt", "w") as wd:
    wd.write(my_text + "\n")
    wd.write(str(my_integer) + "\n")
    wd.write(str(my_list) + "\n")
    wd.write(str(my_dict) + "\n")
    wd.write(str(my_float) + "\n")


with open("data_output.txt", "r") as rd:
    data = rd.read().splitlines()
    my_txt = data[0]
    my_int = int(data[1])
    my_lst = list(data[2])
    my_dict = list(data[3])
    my_flt = float(data[4])


print(my_txt)
print(my_int)
print(my_lst)
print(my_flt)

print()
print("".join(my_lst))
print("".join(my_dict))
print("-" * 40)

# endregion Text File

# region Pickle File

print("\n\n\n===== Python Data To and From Pickle File =====\n")

with open("data_output.pkl", "wb") as pkl:
    pickle.dump(my_data, pkl)

print("*** Pickled File Written Successfully ***")
print("-" * 40)


with open("data_output.pkl", "rb") as pkl:
    my_data_after = pickle.load(pkl)
print("*** Pickled File Read Successfully ***")
print("-" * 40)
print("\n*** Data AFTER Pickle File Write & Read ***\n")
# print(my_data_after)
# print('-'*40)
# print()

my_txt = my_data_after[0]
my_int = my_data_after[1]
my_lst = my_data_after[2]
my_dic = my_data_after[3]
my_flt = my_data_after[4]

print(my_txt)
print(my_int)
print(my_lst)
print(my_dic)
print(my_flt)
print("-" * 40)
print(my_data_after)
print()
print("-" * 40)

# endregion Pickle File
