from PySide6.QtWidgets import QMainWindow, QApplication, QToolBar, QStatusBar
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
import PySide6
from typing import Optional

class MainWindow(QMainWindow):
    def __init__(self, app: QApplication):
        super().__init__()
        
        # Declarar o app
        self.app = app
        self.setWindowTitle("Minha janela")
        self.setMinimumHeight(600)
        self.setMinimumWidth(800)
        
        # Menubar e menus
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&Arquivo")
        newnote_action = file_menu.addAction("Nova nota")
        open_action = file_menu.addAction("Abrir")
        openrecent_action = file_menu.addAction("Abrir recente")
        file_menu.addSeparator()
        save_action = file_menu.addAction("Salvar")
        saveas_action = file_menu.addAction("Salvar como...")
        share_action = file_menu.addAction("Compartilhar")
        file_menu.addSeparator()
        quit_action = file_menu.addAction("Sair")
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu("&Editar")
        edit_menu.addAction("Copiar")
        edit_menu.addAction("Recortar")
        edit_menu.addAction("Colar")
        edit_menu.addAction("Desfazer")
        edit_menu.addAction("Refazer")

        select_menu = menu_bar.addMenu("&Selecionar")
        
        view_menu = menu_bar.addMenu("&Exibir")

        help_menu = menu_bar.addMenu("&Ajuda")
        help_menu.addAction("Iniciante?")
        help_menu.addAction("Documentação")
        help_menu.addAction("Sobre")
        
        # Trabalhando com barra de tarefas
        toolbar = QToolBar('Barra de tarefas principal')
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
        
        action1 = QAction(QIcon("icons/sair.png"), "Sair", self)
        action1.setStatusTip("Sair do programa")
        toolbar.addAction(action1)
        action1.triggered.connect(self.quit_app)
        
        # Trabalhando com barras de status
        self.setStatusBar(QStatusBar(self))
        
    def quit_app(self):
        self.app.quit()
        
        