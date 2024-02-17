
import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E_01_AreaRectangulo.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_calcular.clicked.connect(self.calcular_area)
        self.txt_resultado.setEnabled(False)

    # Área de los Slots
    def calcular_area(self):
        longitud = float(self.txt_longitud.text())
        anchura = float(self.txt_anchura.text())

        # Calcular área del rectángulo
        area_rectangulo = longitud * anchura

        # Mostrar resultado en txt_resultado
        self.txt_resultado.setText(str(area_rectangulo))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
