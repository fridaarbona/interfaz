import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E_07_CalcularFactorial.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class CalculadoraFactorial(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_calcular.clicked.connect(self.calcular_factorial)

    # Área de los Slots
    def calcular_factorial(self):
        try:
            numero = int(self.txt_numero.text())

            # Calcular el factorial
            factorial = 1
            for i in range(1, numero + 1):
                factorial *= i

            # Mostrar el resultado en lbl_resultado
            self.lbl_resultado.setText(f"El factorial de {numero} es: {factorial}")
        except ValueError:
            self.lbl_resultado.setText("Ingresa un número entero válido.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CalculadoraFactorial()
    window.show()
    sys.exit(app.exec_())
