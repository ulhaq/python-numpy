import numpy as np

def data_to_numpy(filename = 'befkbhalderstatkode.csv'):
    data = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)

    return data

def english_speakers(data):
    native_codes = [5170, 5502]

    native_mask = (data[:,3] == 5170) | (data[:,3] == 5502)
    native_sum = sum(data[native_mask][:,4])

    non_native_mask = (data[:,3] != 5170) & (data[:,3] != 5502)
    non_native_sum = sum(data[non_native_mask][:,4])

    return native_sum, non_native_sum

def mask_filtering(data, mask):
    return data[(mask)]

def selected_data_sum(data, arg):
    sel = {
        'year': 0,
        'city': 1,
        'age': 2,
        'code': 3
    }

    x = sel[arg]

    unique_dataset = np.unique(data[:,x])
    rs = {}

    for y in unique_dataset:
        rs[y] = sum(data[(data[:,x] == y)][:,4])

    return rs

# print(english_speakers(data_to_numpy()))
