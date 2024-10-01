# import numpy as np
#
# def remove_outliers(data, m=2):
#     """Remove outliers from the data
#     :param data: numpy array
#     :param m: int, default 2
#     :return: numpy array
#     :abs is used to get the absolute value of the data
#     """
#
#     return data[abs(data - np.mean(data)) < m * np.std(data)]
#
# data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(remove_outliers(data))

# Compare this snippet from Practice/RemoveOutliers.py:
def remove_outliers(numbers):
    numbers.sort()
    numbers = numbers[2:-2]
    return numbers

print(remove_outliers(numbers=[3, 7, 9, 20, 5, 8, 40])) # [3, 5, 7, 8, 9, 20, 40] -> [7, 8, 9]
