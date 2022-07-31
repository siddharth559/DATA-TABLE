from re import X
import numpy

#this is a library to make tables

class Table:
    def __init__(self,arr=None,file=None):
        self.table = {}
        self.keys = []

        #here i have defined a classs to represent tables 
        '''self.table actually represents the table:
        its keys are strings representing the column_names 
        and its values are lists representng the columns'''
        #self.keys represent the keys of the dictionary self.table

        if file!=None:
            arr = file.readline()[0:-1].split(',')

        #if file in not_null then the class reads from the file
        # and converts that into a table
        # this is feature directly converts a .csv file to table object
        # if file_name in null then the class requires the column_names as array to instanciate the class      
        
        for i in arr:
            self.table[i] = numpy.array([])
            self.keys = self.table.keys()
        
        if file!=None:
            for i in file.readlines():
                    self.append(i[0:-1].split(','))   

    #following are the methods associated with the class
    #append takes a list and adds it as a row to the table
    #edit_row takes the index of the row(to be edited) and and array, it changes the specific row by the input array
    #get_row returns the row at particular index as a numpy array
    #sort sorts the table based on a particular column

    def append(self,array):
        cur_ind = 0
        for i in self.keys:
            self.table[i] = numpy.append(self.table[i],array[cur_ind])
            cur_ind+=1
    def edit_row(self,ind,array):
        cur_ind = 0
        for i in self.keys:
            self.table[i][ind] = array[cur_ind]
            cur_ind+=1
    def get_row(self,row_ind):
        ret_row = numpy.array([])
        for i in self.keys:
            ret_row = numpy.append(ret_row,self.table[i][row_ind])
        return ret_row
    def normalise(self, col=None):
        if col == None:
            for col in self.keys:
                self.table[col] = self.table[col]/self.table[col].sum()
        elif col not in self.keys:
            print('value not in table')
        else:
            self.table[col] = self.table[col]/self.table[col].sum()
    def convert_float(self,col=None):
        if col == None:
            for col in self.keys:
                self.table[col] = numpy.array([float(i) for i in self.table[col]])
        elif col not in self.keys:
            print('col not in table')
        else:
            self.table[col] = numpy.array([float(i) for i in self.table[col]])
    def convert_int(self,col):
        if col == None:
            for col in self.keys:
                self.table[col] = numpy.array([int(i) for i in self.table[col]])
        elif col not in self.keys:
            print('col not in table')
        else:
            self.table[col] = numpy.array([int(i) for i in self.table[col]])
    def convert_str(self,col):
        if col == None:
            for col in self.keys:
                self.table[col] = numpy.array([str(i) for i in self.table[col]])
        elif col not in self.keys:
            print('col not in table')
        else:
            self.table[col] = numpy.array([str(i) for i in self.table[col]])
    def sort(self,col):
        if col not in self.keys:
            print('value not in table')
        else:
            copy_array = [i for i in self.table[col]]
            copy_array.sort()
            for i in range(len(copy_array)):
                j = list(self.table[col][i:]).index(copy_array[i])+i
                if i != j:
                    prev = self.get_row(i)
                    self.edit_row(i,self.get_row(j))
                    self.edit_row(j,prev)


if __name__ == "__main__":
    ''' 
    here are the tests
    we make a table with
    the column_names as
    a b c d and the do some 
    operations over it
    '''
    main = Table(['a','b','c','d'])
    main.append([2,3,1,4])
    main.append([2,3,4,5])
    main.append([1,3,6,2])
    main.append([2,7,3,1])
    print(main.table)
    main.sort('c')
    print(main.table)


        
