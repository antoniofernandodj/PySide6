from PySide6.QtWidgets import QApplication
from windows.MainWindow import MainWindow
import sys

# Criar o app
app = QApplication(sys.argv)

# Criar a janela
window = MainWindow(app)

# Exibir a janela
window.show()

# Executar
app.exec()