# Form implementation generated from reading ui file 'meu_layout.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets

import sys
import os

def resource_path(relative_path):
    """Retorna o caminho absoluto do recurso, para uso no modo 'congelado'."""
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), "img_source", relative_path)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(570, 631)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(575, 636))
        MainWindow.setMaximumSize(QtCore.QSize(575, 636))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.a_Sup = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a_Sup.sizePolicy().hasHeightForWidth())
        self.a_Sup.setSizePolicy(sizePolicy)
        self.a_Sup.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.a_Sup.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.a_Sup.setObjectName("a_Sup")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.a_Sup)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.microphoneButton = QtWidgets.QPushButton(parent=self.a_Sup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.microphoneButton.sizePolicy().hasHeightForWidth())
        self.microphoneButton.setSizePolicy(sizePolicy)
        self.microphoneButton.setMinimumSize(QtCore.QSize(0, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("start_record_icon.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon.addPixmap(QtGui.QPixmap(resource_path("stop_record_icon.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.microphoneButton.setIcon(icon)
        self.microphoneButton.setIconSize(QtCore.QSize(20, 20))
        self.microphoneButton.setCheckable(True)
        self.microphoneButton.setChecked(False)
        self.microphoneButton.setObjectName("microphoneButton")
        self.verticalLayout_2.addWidget(self.microphoneButton)
        self.Traduzir_tabWidget = QtWidgets.QTabWidget(parent=self.a_Sup)
        self.Traduzir_tabWidget.setObjectName("Traduzir_tabWidget")
        self.Texto_atual = QtWidgets.QWidget()
        self.Texto_atual.setObjectName("Texto_atual")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Texto_atual)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Texto_textEdit = QtWidgets.QTextEdit(parent=self.Texto_atual)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Texto_textEdit.sizePolicy().hasHeightForWidth())
        self.Texto_textEdit.setSizePolicy(sizePolicy)
        self.Texto_textEdit.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.Texto_textEdit.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.Texto_textEdit.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.Texto_textEdit.setLineWidth(1)
        self.Texto_textEdit.setMidLineWidth(0)
        self.Texto_textEdit.setTabChangesFocus(False)
        self.Texto_textEdit.setDocumentTitle("")
        self.Texto_textEdit.setObjectName("Texto_textEdit")
        self.verticalLayout_3.addWidget(self.Texto_textEdit)
        self.Traduzir_tabWidget.addTab(self.Texto_atual, "")
        self.Texto_original = QtWidgets.QWidget()
        self.Texto_original.setObjectName("Texto_original")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Texto_original)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Original_textEdit = QtWidgets.QTextEdit(parent=self.Texto_original)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Original_textEdit.sizePolicy().hasHeightForWidth())
        self.Original_textEdit.setSizePolicy(sizePolicy)
        self.Original_textEdit.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.Original_textEdit.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.Original_textEdit.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.Original_textEdit.setLineWidth(1)
        self.Original_textEdit.setMidLineWidth(0)
        self.Original_textEdit.setTabChangesFocus(False)
        self.Original_textEdit.setDocumentTitle("")
        self.Original_textEdit.setObjectName("Original_textEdit")
        self.verticalLayout_4.addWidget(self.Original_textEdit)
        self.Traduzir_tabWidget.addTab(self.Texto_original, "")
        self.verticalLayout_2.addWidget(self.Traduzir_tabWidget)
        self.verticalLayout.addWidget(self.a_Sup)
        self.b_Mid = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_Mid.sizePolicy().hasHeightForWidth())
        self.b_Mid.setSizePolicy(sizePolicy)
        self.b_Mid.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.b_Mid.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.b_Mid.setObjectName("b_Mid")
        self.gridLayout = QtWidgets.QGridLayout(self.b_Mid)
        self.gridLayout.setObjectName("gridLayout")
        self.Tradutor_label = QtWidgets.QLabel(parent=self.b_Mid)
        self.Tradutor_label.setObjectName("Tradutor_label")
        self.gridLayout.addWidget(self.Tradutor_label, 0, 0, 1, 1)
        self.Clareza_label = QtWidgets.QLabel(parent=self.b_Mid)
        self.Clareza_label.setObjectName("Clareza_label")
        self.gridLayout.addWidget(self.Clareza_label, 5, 0, 1, 1)
        self.Velocidade_label = QtWidgets.QLabel(parent=self.b_Mid)
        self.Velocidade_label.setObjectName("Velocidade_label")
        self.gridLayout.addWidget(self.Velocidade_label, 6, 0, 1, 1)
        self.Tom_Slider = QtWidgets.QSlider(parent=self.b_Mid)
        self.Tom_Slider.setMaximum(100)
        self.Tom_Slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.Tom_Slider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBothSides)
        self.Tom_Slider.setObjectName("Tom_Slider")
        self.gridLayout.addWidget(self.Tom_Slider, 7, 1, 1, 1)
        self.Tom_label = QtWidgets.QLabel(parent=self.b_Mid)
        self.Tom_label.setObjectName("Tom_label")
        self.gridLayout.addWidget(self.Tom_label, 7, 0, 1, 1)
        self.Estilo_label = QtWidgets.QLabel(parent=self.b_Mid)
        self.Estilo_label.setObjectName("Estilo_label")
        self.gridLayout.addWidget(self.Estilo_label, 3, 0, 1, 1)
        self.Resetar_Estilo_Button = QtWidgets.QPushButton(parent=self.b_Mid)
        self.Resetar_Estilo_Button.setMinimumSize(QtCore.QSize(115, 0))
        self.Resetar_Estilo_Button.setObjectName("Resetar_Estilo_Button")
        self.gridLayout.addWidget(self.Resetar_Estilo_Button, 4, 2, 1, 1)
        self.Vozes_comboBox = QtWidgets.QComboBox(parent=self.b_Mid)
        self.Vozes_comboBox.setMinimumSize(QtCore.QSize(0, 25))
        self.Vozes_comboBox.setObjectName("Vozes_comboBox")
        self.gridLayout.addWidget(self.Vozes_comboBox, 1, 1, 1, 1)
        self.Resetar_Velocidade_Button = QtWidgets.QPushButton(parent=self.b_Mid)
        self.Resetar_Velocidade_Button.setMinimumSize(QtCore.QSize(115, 0))
        self.Resetar_Velocidade_Button.setObjectName("Resetar_Velocidade_Button")
        self.gridLayout.addWidget(self.Resetar_Velocidade_Button, 6, 2, 1, 1)
        self.Intensidade_Slider = QtWidgets.QSlider(parent=self.b_Mid)
        self.Intensidade_Slider.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.Intensidade_Slider.setAutoFillBackground(True)
        self.Intensidade_Slider.setMaximum(100)
        self.Intensidade_Slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.Intensidade_Slider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBothSides)
        self.Intensidade_Slider.setObjectName("Intensidade_Slider")
        self.gridLayout.addWidget(self.Intensidade_Slider, 4, 1, 1, 1)
        self.Vozes_label = QtWidgets.QLabel(parent=self.b_Mid)
        self.Vozes_label.setObjectName("Vozes_label")
        self.gridLayout.addWidget(self.Vozes_label, 1, 0, 1, 1)
        self.Intensidade_label = QtWidgets.QLabel(parent=self.b_Mid)
        self.Intensidade_label.setMinimumSize(QtCore.QSize(150, 28))
        self.Intensidade_label.setMaximumSize(QtCore.QSize(150, 28))
        self.Intensidade_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.Intensidade_label.setObjectName("Intensidade_label")
        self.gridLayout.addWidget(self.Intensidade_label, 4, 0, 1, 1)
        self.Clareza_Slider = QtWidgets.QSlider(parent=self.b_Mid)
        self.Clareza_Slider.setAutoFillBackground(True)
        self.Clareza_Slider.setMaximum(100)
        self.Clareza_Slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.Clareza_Slider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBothSides)
        self.Clareza_Slider.setObjectName("Clareza_Slider")
        self.gridLayout.addWidget(self.Clareza_Slider, 5, 1, 1, 1)
        self.Resetar_Tom_Button = QtWidgets.QPushButton(parent=self.b_Mid)
        self.Resetar_Tom_Button.setMinimumSize(QtCore.QSize(115, 0))
        self.Resetar_Tom_Button.setObjectName("Resetar_Tom_Button")
        self.gridLayout.addWidget(self.Resetar_Tom_Button, 7, 2, 1, 1)
        self.Resetar_Clareza_Button = QtWidgets.QPushButton(parent=self.b_Mid)
        self.Resetar_Clareza_Button.setMinimumSize(QtCore.QSize(115, 0))
        self.Resetar_Clareza_Button.setObjectName("Resetar_Clareza_Button")
        self.gridLayout.addWidget(self.Resetar_Clareza_Button, 5, 2, 1, 1)
        self.Traduzir_Button = QtWidgets.QPushButton(parent=self.b_Mid)
        self.Traduzir_Button.setMinimumSize(QtCore.QSize(115, 0))
        self.Traduzir_Button.setObjectName("Traduzir_Button")
        self.gridLayout.addWidget(self.Traduzir_Button, 0, 2, 1, 1)
        self.Estilo_comboBox = QtWidgets.QComboBox(parent=self.b_Mid)
        self.Estilo_comboBox.setMinimumSize(QtCore.QSize(0, 25))
        self.Estilo_comboBox.setObjectName("Estilo_comboBox")
        self.gridLayout.addWidget(self.Estilo_comboBox, 3, 1, 1, 1)
        self.Velocidade_Slider = QtWidgets.QSlider(parent=self.b_Mid)
        self.Velocidade_Slider.setAutoFillBackground(True)
        self.Velocidade_Slider.setMaximum(100)
        self.Velocidade_Slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.Velocidade_Slider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBothSides)
        self.Velocidade_Slider.setObjectName("Velocidade_Slider")
        self.gridLayout.addWidget(self.Velocidade_Slider, 6, 1, 1, 1)
        self.Tradutor_comboBox = QtWidgets.QComboBox(parent=self.b_Mid)
        self.Tradutor_comboBox.setMinimumSize(QtCore.QSize(0, 25))
        self.Tradutor_comboBox.setObjectName("Tradutor_comboBox")
        self.gridLayout.addWidget(self.Tradutor_comboBox, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.b_Mid)
        self.c_Bot = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c_Bot.sizePolicy().hasHeightForWidth())
        self.c_Bot.setSizePolicy(sizePolicy)
        self.c_Bot.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.c_Bot.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.c_Bot.setObjectName("c_Bot")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.c_Bot)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Modo_Noturno_Button = QtWidgets.QPushButton(parent=self.c_Bot)
        self.Modo_Noturno_Button.setMinimumSize(QtCore.QSize(110, 30))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(resource_path("noturn_on_off_icons.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Modo_Noturno_Button.setIcon(icon1)
        self.Modo_Noturno_Button.setIconSize(QtCore.QSize(20, 20))
        self.Modo_Noturno_Button.setCheckable(True)
        self.Modo_Noturno_Button.setChecked(False)
        self.Modo_Noturno_Button.setObjectName("Modo_Noturno_Button")
        self.gridLayout_2.addWidget(self.Modo_Noturno_Button, 0, 4, 1, 1)
        self.Criar_Audio_Button = QtWidgets.QPushButton(parent=self.c_Bot)
        self.Criar_Audio_Button.setMinimumSize(QtCore.QSize(100, 0))
        self.Criar_Audio_Button.setObjectName("Criar_Audio_Button")
        self.gridLayout_2.addWidget(self.Criar_Audio_Button, 0, 0, 1, 1)
        self.Reproduzir_Previa_Button = QtWidgets.QPushButton(parent=self.c_Bot)
        self.Reproduzir_Previa_Button.setEnabled(False)
        self.Reproduzir_Previa_Button.setMinimumSize(QtCore.QSize(111, 0))
        self.Reproduzir_Previa_Button.setObjectName("Reproduzir_Previa_Button")
        self.gridLayout_2.addWidget(self.Reproduzir_Previa_Button, 0, 1, 1, 1)
        self.Remover_Previa_Button = QtWidgets.QPushButton(parent=self.c_Bot)
        self.Remover_Previa_Button.setEnabled(False)
        self.Remover_Previa_Button.setMinimumSize(QtCore.QSize(100, 0))
        self.Remover_Previa_Button.setObjectName("Remover_Previa_Button")
        self.gridLayout_2.addWidget(self.Remover_Previa_Button, 0, 2, 1, 1)
        self.Salvar_Audio_Button = QtWidgets.QPushButton(parent=self.c_Bot)
        self.Salvar_Audio_Button.setEnabled(False)
        self.Salvar_Audio_Button.setMinimumSize(QtCore.QSize(85, 0))
        self.Salvar_Audio_Button.setObjectName("Salvar_Audio_Button")
        self.gridLayout_2.addWidget(self.Salvar_Audio_Button, 0, 3, 1, 1)
        self.verticalLayout.addWidget(self.c_Bot)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Traduzir_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Conversor de Texto em Áudio - Giovanne"))
        self.microphoneButton.setText(_translate("MainWindow", " Gravar Áudio do Microfone"))
        self.Traduzir_tabWidget.setTabText(self.Traduzir_tabWidget.indexOf(self.Texto_atual), _translate("MainWindow", "Texto atual"))
        self.Traduzir_tabWidget.setTabText(self.Traduzir_tabWidget.indexOf(self.Texto_original), _translate("MainWindow", "Texto original"))
        self.Tradutor_label.setText(_translate("MainWindow", "Tradutor de texto:"))
        self.Clareza_label.setText(_translate("MainWindow", "Clareza da voz: 0%"))
        self.Velocidade_label.setText(_translate("MainWindow", "Velocidade da voz: 0%"))
        self.Tom_label.setText(_translate("MainWindow", "Tom da voz: 0%"))
        self.Estilo_label.setText(_translate("MainWindow", "Estilo de fala:"))
        self.Resetar_Estilo_Button.setText(_translate("MainWindow", "Resetar Estilo"))
        self.Resetar_Velocidade_Button.setText(_translate("MainWindow", "Resetar Velocidade"))
        self.Vozes_label.setText(_translate("MainWindow", "Vozes disponíveis:"))
        self.Intensidade_label.setText(_translate("MainWindow", "Intensidade do Estilo: 100%"))
        self.Resetar_Tom_Button.setText(_translate("MainWindow", "Resetar Tom"))
        self.Resetar_Clareza_Button.setText(_translate("MainWindow", "Resetar Clareza"))
        self.Traduzir_Button.setText(_translate("MainWindow", "Traduzir"))
        self.Modo_Noturno_Button.setText(_translate("MainWindow", " Modo Noturno"))
        self.Criar_Audio_Button.setText(_translate("MainWindow", "Criar Áudio"))
        self.Reproduzir_Previa_Button.setText(_translate("MainWindow", "Reproduzir Prévia"))
        self.Remover_Previa_Button.setText(_translate("MainWindow", "Remover Prévia"))
        self.Salvar_Audio_Button.setText(_translate("MainWindow", "Salvar Áudio"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())