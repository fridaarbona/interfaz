import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E_04_EcuacionPrimerGrado.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class ResolverEcuacion(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_calcular.clicked.connect(self.resolver_ecuacion)

    # Área de los Slots
    def resolver_ecuacion(self):
        try:
            m = float(self.txt_m.text())
            b = float(self.txt_b.text())

            # Calcular y
            y = m * float(self.txt_x.text()) + b

            # Mostrar el resultado en lbl_resultado
            self.lbl_resultado.setText(f"El valor de y es: {y:.2f}")
        except ValueError:
            self.lbl_resultado.setText("Ingresa valores numéricos válidos.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ResolverEcuacion()
    window.show()
    sys.exit(app.exec_())
