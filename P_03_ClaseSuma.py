import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_03_ClaseSuma.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_sumar.clicked.connect(self.suma)
        self.txt_suma.setEnabled(False)


    # Área de los Slots
    def suma (self):
        A = int(self.A.text())
        B = int(self.B.text())
        r = A+B
        print(r)
        self.txt_suma.setText(str(r))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())