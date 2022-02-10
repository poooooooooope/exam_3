import csv
import sys
import pandas as pandasForSortingCSV


class WorkWithCsvFile:

    def __init__(self, our_csv_file):
        self.our_csv_file = our_csv_file

    def sort_by_first_field(self):
        csvData = pandasForSortingCSV.read_csv(self.our_csv_file)
        csvData.sort_values([1], 
                    axis=0,
                    ascending=[False], 
                    inplace=True)
        
    def add_a_row(self, new_row):
        addrow = self.our_csv_file
        addrow.writerow(new_row)
        

    def update_a_row(self):
        pass

    def correct_a_row(self):
        pass

    def search_elements_by_condition(self, enter_number):
        number = enter_number
        csv_file = csv.reader(open(self.our_csv_file, "r"), delimiter=",")
        
        for row in csv_file:
            if number == row[1]:
         print (row)
        

file_name = ''

csv_file = WorkWithCsvFile(file_name)
