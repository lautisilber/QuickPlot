from email import header
import matplotlib.pyplot as plt
import numpy as np
from os.path import exists
import sys

def input_int(prompt) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter an integer.")

def input_bool(prompt, default_fale=True) -> bool:
    while True:
        try:
            i = input(prompt).lower()
            assert(i == 'y' or i == 'n' or i == '')
            return True if i == 'y' else False
        except ValueError:
            print("Please enter a 'y' or 'n'.")

def get_header_rows(file_name):
    '''
        Returns the number of rows in the header
    '''
    with open(file_name, 'r') as f:
        n = 0
        headers = None
        for line in f.readlines():
            cols = line.split(',')
            all_numbers = True
            for col in cols:
                try:
                    float(col)
                except ValueError:
                    all_numbers = False
                    break
            if all_numbers:
                break
            headers = cols.copy()
            n += 1
        return n, headers

def main():
    '''
        Presumes a csv file with header columns and then just data
    '''
    file_name = None
    if len(sys.argv) >= 2:
        file_name = sys.argv[1]
        if not exists(file_name):
            file_name = None
    if not file_name:
        while True:
            file_name = str(input("Enter the file name: "))
            if exists(file_name):
                break
            else:
                print("File does not exist.")
    n_skip, headers = get_header_rows(file_name)
    data = np.loadtxt(file_name, delimiter=",", skiprows=n_skip)
    x_data = data[:,0]
    y_data = data[:,1:data.shape[1]]

    for i in range(y_data.shape[1]):
        plt.plot(x_data, y_data[:,i], label=headers[i+1]) # +1 to skip the first column       
    

    save_file = input_bool("Save plot? (y/[n]): ")

    plt.legend()
    plt.xlabel(headers[0])
    if save_file:
        plt.savefig(file_name + ".png")
    plt.show()
    
if __name__ == "__main__":
    main()
    
