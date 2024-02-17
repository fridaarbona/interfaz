import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E_06_PromedioCalificaciones.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class CalculadoraPromedio(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_calcular.clicked.connect(self.calcular_promedio)

    # Área de los Slots
    def calcular_promedio(self):
        try:
            calificacion1 = float(self.txt_calif1.text())
            calificacion2 = float(self.txt_calif2.text())
            calificacion3 = float(self.txt_calif3.text())
            calificacion4 = float(self.txt_calif4.text())
            calificacion5 = float(self.txt_calif5.text())

            # Calcular el promedio
            promedio = (calificacion1 + calificacion2 + calificacion3 + calificacion4 + calificacion5) / 5

            # Mostrar el resultado en lbl_resultado
            self.lbl_resultado.setText(f"Tu promedio es: {promedio:.2f}")
        except ValueError:
            self.lbl_resultado.setText("Ingresa calificaciones numéricas válidas.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CalculadoraPromedio()
    window.show()
    sys.exit(app.exec_())
