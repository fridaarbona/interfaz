import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E_05_CalculoPuntoMedio.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class CalculadoraPuntoMedio(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_calcular.clicked.connect(self.calcular_punto_medio)

    # Área de los Slots
    def calcular_punto_medio(self):
        try:
            x1 = float(self.txt_punto1_x.text())
            y1 = float(self.txt_punto1_y.text())
            x2 = float(self.txt_punto2_x.text())
            y2 = float(self.txt_punto2_y.text())

            # Calcular el punto medio
            punto_medio_x = (x1 + x2) / 2
            punto_medio_y = (y1 + y2) / 2

            # Mostrar el resultado en lbl_resultado
            self.lbl_resultado.setText(f"El punto medio es: ({punto_medio_x:.2f}, {punto_medio_y:.2f})")
        except ValueError:
            self.lbl_resultado.setText("Ingresa valores numéricos válidos.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CalculadoraPuntoMedio()
    window.show()
    sys.exit(app.exec_())
