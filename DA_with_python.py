# DA with python: focused on numpy

import numpy as np
import urllib.request

a = np.arange(12).reshape(4, 3)
print(f"\na is \n{a}\n")
print(f"np.array.size\nreturns number of elements\na.size = {a.size}\n")
print(f"np.array.ndim\nreturns number of dimensions\na.ndim = {a.ndim}\n")
print(f"np.array.dtype\nreturns type of np.array\na.dype = {a.dtype}\n")

b = np.arange(12).reshape(3, 4)
print(f"\nb is \n{a}\n")


print(f"a @ b is \n{a@b}\n")
print("same as np.dot(a, b)\n")

# # [
# # #  [ 0  1  2]           [[ 0  1  2  3]
# #    [ 3  4  5]     x      [ 4  5  6  7]
# #    [ 6  7  8]            [ 8  9 10 11]]
# # #  [ 9 10 11]


# # = [[ 20  23  26  29]
# #   [ 56  68  80  92]
# #   [ 92 113 134 155]
# #   [128 158 188 218]]

# # (0*4) + (1*4) + (2*8) -> 20


# ______________________________________________
# ___________________ MULTIDIMENSIONAL NUMPY ARRAYS ______________________
# ______________________________________________

c = np.arange(27).reshape(3, 3, 3)
print(f"\nc is a 3D array, 27 items, 3x3x3:\n{c}\n")

climate_data = np.array(
    [[73, 67, 43], [91, 88, 64], [87, 134, 58], [102, 43, 37], [69, 96, 70]]
)  # ( 5, 3)

weights = np.array([0.3, 0.2, 0.5])

print(f"shape of climate_data is {climate_data.shape}\n")
print(f"shape of climate_data is {weights.shape}\n")

total = climate_data @ weights
print(f"climate_data @ weights is \n{total}, \nand shape is {total.shape}\n")

# common data analysis flow:
# 1. get a file
# 2. analyse file
# 3. perform action on file
# 4. add data to existing file
# 5. write data to another file

print(
    f"\nCommon data analysis flow: \n1. get a file\n2. analyse file\n3. perform action on file\n4. add data to existing file\n5. write data to another file\n"
)


urllib.request.urlretrieve(
    "https://gist.github.com/BirajCoder/a4ffcb76fd6fb221d76ac2ee2b8584e9/raw/4054f90adfd361b7aa4255e99c2e874664094cea/climate.csv",
    "climate.txt",
)

print(
    f"urllib.request.urlretriev downloads climate.txt into our current folder when this python file is run.\n"
)


climate_txt = np.genfromtxt("climate.txt", delimiter=",", skip_header=1)
print(
    f"np.genfromtxt generates np.array from downloaded climate.txt: \n{climate_txt}\n"
)


yields = climate_txt @ weights
print(yields.shape)
