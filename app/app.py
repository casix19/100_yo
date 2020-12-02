import datetime
from PySide2 import QtWidgets, QtCore, QtGui
import sys
import sqlite3

language = ["english"]
title_app = "test title"
age_txt = "test age"
compute_txt = "test compute"
result_txt = "test result"


class Window_lang(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("language selection")
        self.setup_ui_lang()
        self.setup_lang_connections()

    def setup_ui_lang(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.btn_fr = QtWidgets.QPushButton("French")
        self.btn_fi = QtWidgets.QPushButton("Finnish")
        self.btn_en = QtWidgets.QPushButton("English")

        self.btn_fr.setIcon(QtGui.QIcon(r"C:\Users\alexs\Documents\Python\exercises\how_old\flag_french.png"))
        self.btn_fi.setIcon(QtGui.QIcon(r"C:\Users\alexs\Documents\Python\exercises\how_old\flag_finnish.png"))
        self.btn_en.setIcon(QtGui.QIcon(r"C:\Users\alexs\Documents\Python\exercises\how_old\flag_english.png"))

        self.layout.addWidget(self.btn_en)
        self.layout.addWidget(self.btn_fr)
        self.layout.addWidget(self.btn_fi)

        widget = QtWidgets.QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def setup_lang_connections(self):
        self.btn_fr.clicked.connect(self.show_calcul_window_fr)
        self.btn_fi.clicked.connect(self.show_calcul_window_fi)
        self.btn_en.clicked.connect(self.show_calcul_window_en)

    def show_calcul_window_fr(self, checked):
        language.clear()
        language.append("french")
        " ".join(language)
        self.w = Window_age()
        self.w.show()

    def show_calcul_window_en(self, checked):
        language.clear()
        language.append("english")
        " ".join(language)
        self.w = Window_age()
        self.w.show()
        
    def show_calcul_window_fi(self, checked):
        language.clear()
        language.append("finnish")
        " ".join(language)
        self.w = Window_age()
        self.w.show()

class Window_age(QtWidgets.QWidget):
  
    def __init__(self):
        super().__init__()
        self.lang()
        self.setWindowTitle(str(title_app[0][0]))
        self.setup_ui()
        self.setupt_css()
        self.setup_connections()

    def lang(self):
        conn = sqlite3.connect("language.db")
        c = conn.cursor()
        langue = " ".join(language)
        c.execute(f"SELECT title FROM {langue}")
        global title_app
        title_app = c.fetchall()
        c.execute(f"SELECT age FROM {langue}")
        global age_txt
        age_txt = c.fetchall()
        c.execute(f"SELECT compute FROM {langue}")
        global compute_txt
        compute_txt = c.fetchall()
        c.execute(f"SELECT result FROM {langue}")
        global result_txt
        result_txt = c.fetchall()
        
        conn.close()

    
    def setup_ui(self):
        self.layout = QtWidgets.QFormLayout(self)
        self.lne_current_age = QtWidgets.QLineEdit()
        self.btn_launch_calc = QtWidgets.QPushButton(str(compute_txt[0][0]))
        self.anne_retour = QtWidgets.QLabel()


        self.layout.addRow(str(age_txt[0][0]), self.lne_current_age)
        self.layout.addRow(self.btn_launch_calc)
        self.layout.addRow(self.anne_retour)
        self.anne_retour.setAlignment(QtCore.Qt.AlignCenter)

    def setupt_css(self):
        self.setFixedHeight(150)
        self.setFixedWidth(500)

    def setup_connections(self):
        self.lne_current_age.returnPressed.connect(self.compute)
        self.btn_launch_calc.clicked.connect(self.compute)


    def compute(self):
        age = int(self.lne_current_age.text())
        years_left = 100 - age
        date_today = datetime.date.today()
        this_year = date_today.year
        year_hunderd_yo =this_year + years_left
        result_txt_txt = str(result_txt[0][0])
        final_text = f"{result_txt_txt} {year_hunderd_yo}"
        self.anne_retour.setText(final_text)


app = QtWidgets.QApplication([])
win = Window_lang()
win.show()
app.exec_()