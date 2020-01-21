import sys  # Pasaremos argumentos argv
from PyQt5.QtWidgets import QApplication, QMainWindow  # Para poder trabajar con la aplicación y con ventanas
from PyQt5 import uic  # Para poder manejar archivos .ui (Interfaz de usuario)


# Clase heredada de QMainWindow (Constructor de ventanas)
class Ventana(QMainWindow):
    # Método constructor de la clase
    def __init__(self):
        # Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        # Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("MainWindow.ui", self)


# Instancia para iniciar una aplicación
app = QApplication(sys.argv)

# Crear un objeto de la clase
_ventana = Ventana()

# Mostrar la ventana
_ventana.show()

# Ejecutamos la aplicación
app.exec()
