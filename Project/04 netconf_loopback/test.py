from main import file_path, read_data

data = read_data(file_path)
print(data.shape)
print(data.dtype)
for line in range(data.shape[0]):
    print(1)
    print(data[line])
    print(2)