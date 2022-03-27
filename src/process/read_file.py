
def read_payment_data(file_path):
    with open(file_path, 'r') as file:
        return [x.replace("\n", "") for x in file.readlines()]


