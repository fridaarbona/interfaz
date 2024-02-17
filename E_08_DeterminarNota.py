import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E_08_DeterminarNota.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class DeterminarNota(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_calcular.clicked.connect(self.determinar_nota)

    # Área de los Slots
    def determinar_nota(self):
        try:
            calificacion = float(self.txt_calificacion.text())

            # Determinar la nota
            if calificacion >= 9:
                nota = "A"
            elif calificacion >= 8:
                nota = "B"
            elif calificacion >= 7:
                nota = "C"
            elif calificacion >= 6:
                nota = "D"
            else:
                nota = "F"

            # Mostrar el resultado en lbl_resultado
            self.lbl_resultado.setText(f"La nota del alumno es: {nota}")
        except ValueError:
            self.lbl_resultado.setText("Ingresa una calificación numérica válida.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DeterminarNota()
    window.show()
    sys.exit(app.exec_())
