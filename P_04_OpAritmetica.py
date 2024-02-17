import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_04_OpAritmetica.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_suma.clicked.connect(self.suma)
        self.btn_resta.clicked.connect(self.resta)
        self.btn_multiplicar.clicked.connect(self.multiplicar)
        self.btn_division.clicked.connect(self.division)
        self.txt_resultado.setEnabled(False)


    # Área de los Slots
    def suma (self):
        A = int(self.A.text())
        B = int(self.B.text())
        r = A+B
        print(r)
        self.txt_resultado.setText(str(r))

    def resta(self):
        A = int(self.A.text())
        B = int(self.B.text())
        r = A-B
        print(r)
        self.txt_resultado.setText(str(r))

    def multiplicar(self):
        A = int(self.A.text())
        B = int(self.B.text())
        r = A*B
        print(r)
        self.txt_resultado.setText(str(r))

    def division(self):
        A = int(self.A.text())
        B = int(self.B.text())
        r = A/B
        print(r)
        self.txt_resultado.setText(str(r))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())