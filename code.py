import csv
import os


if __name__ == "__main__":
    with open('data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        if 'USAID' not in os.getcwd():
            os.makedirs('USAID')
            os.chdir('USAID')
        for row in reader:
            os.system('axel {}'.format(row['File']))
