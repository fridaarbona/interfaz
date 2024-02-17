import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E_02_CalcularIMC.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class CalculadoraIMC(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_calcular.clicked.connect(self.calcular_imc)

    # Área de los Slots
    def calcular_imc(self):
        try:
            peso = float(self.txt_peso.text())
            altura = float(self.txt_altura.text())

            # Calcular el IMC
            imc = peso / (altura * altura)

            # Mostrar el resultado en lbl_resultado
            self.lbl_resultado.setText(f"Tu IMC es: {imc:.2f}")
        except ValueError:
            self.lbl_resultado.setText("Ingresa valores numéricos válidos.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CalculadoraIMC()
    window.show()
    sys.exit(app.exec_())
