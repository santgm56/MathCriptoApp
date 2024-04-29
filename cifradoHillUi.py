from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QMessageBox
from cifradoHill import encriptar, desencriptar, matriz_llave
from sistemaHill import convertirStraList
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
import sys


class MathCripto(QMainWindow):
    def __init__(self):
        super().__init__()

        # Cargar el diseño de la aplicación
        loadUi("uiApp.ui", self)

        # Configurar la ventana
        self.setWindowTitle('MathCripto')

        self.stackedWidget.setCurrentWidget(self.page_uno)

        self.bt_encriptar.clicked.connect(self.mostrar_page_uno)
        self.bt_desencriptar.clicked.connect(self.mostrar_page_dos)
        self.bt_acercaDe.clicked.connect(self.mostrar_page_tres)
        self.bt_copiar_1.clicked.connect(self.copiar_texto_1)
        self.bt_copiar_2.clicked.connect(self.copiar_texto_2)
        self.bt_copiar_3.clicked.connect(self.copiar_texto_3)

        self.bt_encrypt.clicked.connect(self.encrypt_message)
        self.bt_encrypt_2.clicked.connect(self.decrypt_message)

        self.label_5.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.label_7.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.label_9.setTextInteractionFlags(Qt.TextSelectableByMouse)

    def mostrar_page_uno(self):
        self.stackedWidget.setCurrentWidget(self.page_uno)

    def mostrar_page_dos(self):
        self.stackedWidget.setCurrentWidget(self.page_dos)

    def mostrar_page_tres(self):
        self.stackedWidget.setCurrentWidget(self.page_tres)

    def encrypt_message(self):
        dimension = self.lineEdit_2.text()
        message = self.lineEdit_3.text()

        try:
            key = matriz_llave(int(dimension))
            encrypted_message = encriptar(message, key)
            key_format = [fila.tolist() for fila in key]
            self.label_5.setText(str(key_format))
            self.label_7.setText(encrypted_message)
        except ValueError as e:
            self.show_error_message(str(e))
        except Exception as e:
            self.show_error_message(f"Error: {str(e)}")

    def decrypt_message(self):
        llave = self.lineEdit_4.text()
        encrypt = self.lineEdit_5.text()

        try:
            key = convertirStraList(llave)
            decrypted_message = desencriptar(encrypt, key)
            self.label_9.setText(decrypted_message)
        except ValueError as e:
            self.show_error_message(str(e))
        except Exception as e:
            self.show_error_message(f"Error: {str(e)}")

    def copiar_texto_1(self):
        texto_a_copiar = self.label_5.text()
        clipboard = QApplication.clipboard()
        clipboard.setText(texto_a_copiar)

    def copiar_texto_2(self):
        texto_a_copiar = self.label_7.text()
        clipboard = QApplication.clipboard()
        clipboard.setText(texto_a_copiar)

    def copiar_texto_3(self):
        texto_a_copiar = self.label_9.text()
        clipboard = QApplication.clipboard()
        clipboard.setText(texto_a_copiar)

    def show_error_message(self, message):
        QMessageBox.critical(self, "Error", message)

    def show_info_message(self, message):
        QMessageBox.information(self, "Información", message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MathCripto()
    window.show()
    sys.exit(app.exec_())
