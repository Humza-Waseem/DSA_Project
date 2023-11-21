from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import time 
import pandas as pd
import sys

class Ui_Form(object):
    def load_table(self):
        self.data=pd.read_csv('CarData6.csv',nrows=300)
        with open('CarData6.csv', "r",encoding="utf-8") as fileInput:
            roww = 0
            data = list(csv.reader(fileInput))

            self.tableWidget.setRowCount(len(data))
            for row in data:
                self.tableWidget.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row[0])))
                self.tableWidget.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row[1])))
                self.tableWidget.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row[2])))
                self.tableWidget.setItem(roww, 3 , QtWidgets.QTableWidgetItem((row[3])))
                self.tableWidget.setItem(roww, 4 , QtWidgets.QTableWidgetItem((row[4])))
                self.tableWidget.setItem(roww, 5 , QtWidgets.QTableWidgetItem((row[5])))
                self.tableWidget.setItem(roww, 6 , QtWidgets.QTableWidgetItem((row[6])))
                self.tableWidget.setItem(roww, 7 , QtWidgets.QTableWidgetItem((row[7])))
                self.tableWidget.setItem(roww, 8 , QtWidgets.QTableWidgetItem((row[8])))
                roww += 1
    def sort_data(self):
        selected_algorithm = self.comboBox.currentText()
        selected_attribute = int(self.lineEdit.text())
        if selected_algorithm == "Selection Sort":
                start_time=time.time()
                self.selection_sort(selected_attribute)
                end_time=time.time()
                self.total_time=end_time-start_time 
                self.TimeComplexity.setText(str(self.total_time*1000))   
                                    
                self.update_table(self.data)
                        
        elif selected_algorithm == "Bubble Sort":
                start_time=time.time()
                self.bubble_sort(selected_attribute)
                end_time=time.time()
                self.total_time=end_time-start_time 
                self.TimeComplexity.setText(str(self.total_time*1000))  
                                                            
                self.update_table(self.data)

        elif selected_algorithm == "Insertion Sort":
                start_time=time.time()  
                self.insertion_sort(selected_attribute)
                end_time=time.time()
                self.total_time=end_time-start_time  
                self.TimeComplexity.setText(str(self.total_time*1000))  
                                                            
                self.update_table(self.data)
        elif selected_algorithm == "Merge Sort":  
                start_time=time.time()                        
                self.merge_sort(selected_attribute)
                end_time=time.time()
                self.total_time=end_time-start_time   
                self.TimeComplexity.setText(str(self.total_time*1000)) 
                                                            
                self.update_table(self.data)
        elif selected_algorithm == "Quick Sort": 
                start_time=time.time() 
                self.quicksort(selected_attribute)
                end_time=time.time()
                self.total_time=end_time-start_time 
                self.TimeComplexity.setText(str(self.total_time*1000)) 
                                                            
                self.update_table(self.data)
    def selection_sort(self, column):
         print(self.data)
         n = len(self.data)
         for i in range(n):
             min_idx = i
             for j in range(i + 1, n):
                 if self.data.iloc[j, column] < self.data.iloc[min_idx, column]:
                     min_idx = j
             if min_idx != i:
                 # Swap rows in the DataFrame
                 self.data.iloc[i], self.data.iloc[min_idx] = self.data.iloc[min_idx].copy(), self.data.iloc[i].copy()
         print(self.data)
         return self.data
    def bubble_sort(self, column):
        print(self.data)
        n = len(self.data)
        for i in range(n):
            swapped = False  # Track if any swaps occurred in this pass
            for j in range(0, n-i-1):
                if self.data.iloc[j, column] > self.data.iloc[j+1, column]:
                    # Swap rows in the DataFrame
                    self.data.iloc[j], self.data.iloc[j+1] = self.data.iloc[j+1].copy(), self.data.iloc[j].copy()
                    swapped = True
            if not swapped:
                # If no swaps occurred in a pass, the data is already sorted
                break
        print(self.data)
        return self.data
    def insertion_sort(self, column):
        print(self.data)
        n = len(self.data)
        for i in range(1, n):
            key = self.data.iloc[i].copy()
            j = i - 1
            while j >= 0 and self.data.iloc[j, column] > key[column]:
                self.data.iloc[j + 1] = self.data.iloc[j].copy()
                j = j - 1
            self.data.iloc[j + 1] = key.copy()
        print(self.data)
        return self.data
    def merge_sort(self, column):
            print(self.data)
            self._merge_sort_recursive(self.data, column, 0, len(self.data) - 1)
            print(self.data)
            return self.data

    def _merge_sort_recursive(self, data, column, left, right):
            
            if left < right:
                mid = (left + right) // 2
                self._merge_sort_recursive(data, column, left, mid)
                self._merge_sort_recursive(data, column, mid + 1, right)

                self._merge(data, column, left, mid, right)
                

    def _merge(self, data, column, left, mid, right):
            
            n1 = mid - left + 1
            n2 = right - mid

            left_half = data.iloc[left:left + n1].copy()
            right_half = data.iloc[mid + 1:mid + 1 + n2].copy()

            i = j = 0
            k = left

            while i < n1 and j < n2:
                if left_half.iloc[i, column] <= right_half.iloc[j, column]:
                    data.iloc[k] = left_half.iloc[i].copy()
                    i += 1
                else:
                    data.iloc[k] = right_half.iloc[j].copy()
                    j += 1
                k += 1

            while i < n1:
                data.iloc[k] = left_half.iloc[i].copy()
                i += 1
                k += 1

            while j < n2:
                data.iloc[k] = right_half.iloc[j].copy()
                j += 1
                k += 1

    def quicksort(self, column):
        print(self.data)
        low = 0
        high = len(self.data) - 1
        self._quicksort_recursive(self.data, column, low, high)
        print(self.data)
        return self.data
    
    def _quicksort_recursive(self, data, column, low, high):
        if low < high:
            pivotIndex = self._partition(data, column, low, high)
            self._quicksort_recursive(data, column, low, pivotIndex - 1)
            self._quicksort_recursive(data, column, pivotIndex + 1, high)
    
    def _partition(self, data, column, low, high):
        pivot = data.iloc[high, column]
        i = low - 1
        for j in range(low, high):
            if data.iloc[j, column] <= pivot:
                i = i + 1
                data.iloc[i, :], data.iloc[j, :] = data.iloc[j, :].copy(), data.iloc[i, :].copy()
        data.iloc[i + 1, :], data.iloc[high, :] = data.iloc[high, :].copy(), data.iloc[i + 1, :].copy()
        return i + 1
    def update_table(self, data):
        num_rows, num_cols = data.shape
        self.tableWidget.setRowCount(num_rows)
        for row_idx, row_data in enumerate(data.values):
            for col_idx, value in enumerate(row_data):
                 item = QtWidgets.QTableWidgetItem(str(value))
                 self.tableWidget.setItem(row_idx, col_idx, item)
                
                     
                 
    def Search_update_table(self, data):
        for row_idx, row_data in enumerate(data):
            for col_idx, contain in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(contain))
                self.tableWidget.setItem(row_idx, col_idx, item)
    def get_data_from_table(self):
        data = []
        for row in range(self.tableWidget.rowCount()):
            row_data = []
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item is not None and item.text():
                    row_data.append(str(item.text()))  
                else:
                    row_data.append(str(0))
            data.append(row_data)
        return data
    def perform_search_and_move(self):
        data=self.get_data_from_table()
        column=self.comboBox_2.currentIndex()
        item=self.lineEdit_2.text()
        result = self.LinearSearchStart(data, column, item) 
        self.Search_update_table(result) 
    def LinearSearchStart(self, data, column, item):
        result = []
        for i in range(len(data)):
            if(str(data[i][column]).find(item) != -1):
                result.append(data[i])
        return result
     
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1413, 776)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 191, 781))
        self.widget.setStyleSheet("background-image: url(:/img/loginimg.png);")
        self.widget.setObjectName("widget")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(30, 130, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(0, 70, 21, 16))
        self.widget_2.setStyleSheet("image: url(:/img/sort.png);")
        self.widget_2.setObjectName("widget_2")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(10, 180, 16, 21))
        self.widget_3.setStyleSheet("image: url(:/img/icons8-time-24.png);")
        self.widget_3.setObjectName("widget_3")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(10, 70, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("bold")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 590, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.perform_search_and_move)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 640, 131, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("font: 9pt \"Bauhaus 93\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.ExitButton = QtWidgets.QPushButton(self.widget)
        self.ExitButton.setGeometry(QtCore.QRect(30, 700, 131, 21))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(11)
        self.ExitButton.setFont(font)
        self.ExitButton.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.ExitButton.setStyleSheet("color:rgb(255, 0, 0)")
        self.ExitButton.setObjectName("ExitButton")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 180, 141, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 470, 131, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 219, 141, 31))
        self.label.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 420, 131, 20))
        self.label_2.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.LoadButton = QtWidgets.QPushButton(self.widget)
        self.LoadButton.setGeometry(QtCore.QRect(30, 330, 131, 51))
        self.LoadButton.setStyleSheet("font: 75 14pt \"Rockwell\";")
        self.LoadButton.setObjectName("LoadButton")
        self.LoadButton.clicked.connect(self.load_table)
        self.TimeComplexity = QtWidgets.QLineEdit(self.widget)
        self.TimeComplexity.setGeometry(QtCore.QRect(30, 270, 113, 22))
        self.TimeComplexity.setObjectName("TimeComplexity")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setGeometry(QtCore.QRect(30, 540, 131, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(190, 0, 1221, 781))
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(1049999)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)

        self.retranslateUi(Form)
        self.ExitButton.clicked.connect(self.ExitButton.click) # type: ignore
        self.LoadButton.clicked.connect(self.tableWidget.show) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox.setItemText(0, _translate("Form", "Merge Sort"))
        self.comboBox.setItemText(1, _translate("Form", "Quick Sort"))
        self.comboBox.setItemText(2, _translate("Form", "Insertion Sort"))
        self.comboBox.setItemText(3, _translate("Form", "Bubble Sort"))
        self.comboBox.setItemText(4, _translate("Form", "Selection Sort"))
        self.pushButton.setText(_translate("Form", "Sort Data"))
        self.pushButton.clicked.connect(self.sort_data)
        self.pushButton_2.setText(_translate("Form", "Search"))
        self.pushButton_3.setText(_translate("Form", "Admin Login"))
        self.ExitButton.setText(_translate("Form", "Exit"))
        self.lineEdit.setPlaceholderText("Enter the column Number")
        self.lineEdit_2.setPlaceholderText("Enter the Attribute")
        self.label.setText(_translate("Form", "Time Complexity"))
        self.label_2.setText(_translate("Form", "      Searching"))
        self.LoadButton.setText(_translate("Form", "LOAD"))
        self.comboBox_2.setItemText(0, _translate("Form", "Name"))
        self.comboBox_2.setItemText(1, _translate("Form", "Price"))
        self.comboBox_2.setItemText(2, _translate("Form", "City"))
        self.comboBox_2.setItemText(3, _translate("Form", "Model"))
        self.comboBox_2.setItemText(4, _translate("Form", "Distance"))
        self.comboBox_2.setItemText(5, _translate("Form", "Fuel"))
        self.comboBox_2.setItemText(6, _translate("Form", "Engine"))
        self.comboBox_2.setItemText(7, _translate("Form", "Gear"))
        self.comboBox_2.setItemText(8, _translate("Form", "Category"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Price"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "City"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Model"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Distance Travel"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Fuel Type"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Engine Capacity"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Gear Type"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Category"))
if __name__=="__main__":
        app=QtWidgets.QApplication(sys.argv)
        widget=QtWidgets.QStackedWidget()
        Form=QtWidgets.QWidget()
        ui=Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_()) 