import sys
from PyQt5 import uic, QtWidgets
import math

qtCreatorFile = "E_03_DistanciaEntrePuntos.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class CalculadoraDistancia(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_calcular.clicked.connect(self.calcular_distancia)

    # Área de los Slots
    def calcular_distancia(self):
        try:
            x1 = float(self.txt_punto1_x.text())
            y1 = float(self.txt_punto1_y.text())
            x2 = float(self.txt_punto2_x.text())
            y2 = float(self.txt_punto2_y.text())

            # Calcular la distancia entre dos puntos
            distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

            # Mostrar el resultado en lbl_resultado
            self.lbl_resultado.setText(f"La distancia entre los puntos es: {distancia:.2f}")
        except ValueError:
            self.lbl_resultado.setText("Ingresa valores numéricos válidos.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CalculadoraDistancia()
    window.show()
    sys.exit(app.exec_())
