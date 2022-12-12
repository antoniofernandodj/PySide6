from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QLabel

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Inputs e labels')
        # self.setMinimumHeight(600)
        # self.setMinimumWidth(800)
        
        vertical_layout = QVBoxLayout()
        
        self.input_nome_competo = QLineEdit()
        nome_completo_layout = QHBoxLayout()
        nome_completo_layout.addWidget(QLabel('Nome completo: '))
        nome_completo_layout.addWidget(self.input_nome_competo)
        
        self.input_idade = QLineEdit()
        idade_layout = QHBoxLayout()
        idade_layout.addWidget(QLabel('Idade: '))
        idade_layout.addWidget(self.input_idade)
        
        enviar_layout = QHBoxLayout()
        button = QPushButton("Pegar os dados")
        button.clicked.connect(self.enviar_dados)
        enviar_layout.addWidget(button)
        
        vertical_layout.addLayout(nome_completo_layout)
        vertical_layout.addLayout(idade_layout)
        vertical_layout.addLayout(enviar_layout)
        
        self.setLayout(vertical_layout)
        
        self.text_holder_label = QLabel('Estou aqui!!!')
        
    def enviar_dados(self):
        dados = {
            'nome': self.input_nome_competo.text(),
            'idade': self.input_idade.text()
        }
        print(dados)

