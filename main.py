from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt6.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt
import azure.cognitiveservices.speech as speechsdk
import tempfile
import subprocess
import shutil
import sys
import os
import requests
import uuid
from config import SPEECH_SUBS_KEY, TRANSL_SUBS_KEY, REGION, AZURE_ENDPOINT
from meu_layout import Ui_MainWindow

def resource_path(relative_path):
    """Retorna o caminho absoluto do recurso, para uso no modo 'congelado'."""
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), "img_source", relative_path)

def texto_audio_azure_sslm(texto, voz, nome_arquivo=None, velocidade="0%", tom="0%", estilo_fala='default', intensidade_estilo="1", clareza="0dB", parent=None, effect=None):
    speech_config = speechsdk.SpeechConfig(subscription=SPEECH_SUBS_KEY, region=REGION)
    audio_config = speechsdk.audio.AudioOutputConfig(filename=nome_arquivo) if nome_arquivo else None

    if estilo_fala is None or estilo_fala == 'default':
        express_as = ''
    else:
        express_as = f"<mstts:express-as style='{estilo_fala}' styledegree='{intensidade_estilo}'>"

    ssml_text = f"""
    <speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xmlns:mstts='https://www.w3.org/2001/mstts' xml:lang='pt-BR'>
        <voice name='{voz}'>
            {express_as}
                <prosody rate='{velocidade}' pitch='{tom}' volume='{clareza}'>
                    {texto}
                </prosody>
            {'</mstts:express-as>' if express_as else ''}
        </voice>
    </speak>
    """

    if effect:
        ssml_text = ssml_text.replace(f"<voice name='{voz}'>", f"<voice name='{voz}' effect='{effect}'>")

    try:
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
        result = speech_synthesizer.speak_ssml_async(ssml_text).get()
        
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            if parent:
                parent.show_success("Sucesso!", "Áudio gerado com sucesso!")
            return True
        else:
            if parent:
                parent.show_warning("Falha!", "Falha ao gerar o áudio.")
            return False
    except Exception as e:
        if parent:
            parent.show_warning("Erro", f"Ocorreu um erro ao gerar o áudio: {e}")
        return False

class MainWindow(QMainWindow, Ui_MainWindow):
    update_text_signal = QtCore.pyqtSignal(str)
    update_button_state_signal = QtCore.pyqtSignal(bool)  # Novo sinal para atualizar o estado do botão
    recording_finished_signal = QtCore.pyqtSignal(str)
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        # Conecta o sinal personalizado ao slot que atualiza o texto
        self.update_text_signal.connect(self.updateText)
        
        self.recording_finished_signal.connect(self.show_recording_finished)
        
        self.setWindowTitle("Conversor de Texto em Áudio - Giovanne")
        # Configure o ícone da janela
        self.setWindowIcon(QIcon(resource_path('QIcon_window.png')))
        
        # Inicializações adicionais
        self.temp_audio_file = None
        self.is_night_mode = False
        self.isRecording = False  # Adicione esta linha
        self.speech_recognizer = None  # Adicione esta linha para manter o reconhecedor de fala
        
        self.update_button_state_signal.connect(self.update_button)
        
        self.vozes_estilos = {
            "en-US-AriaNeural": ["default", "angry", "chat", "cheerful", "customerservice", "empathetic", "excited", "friendly", "hopeful", "narration-professional", "newscast-casual", "newscast-formal", "sad", "shouting", "terrified", "unfriendly", "whispering"],
            "en-US-NancyNeural": ["default", "angry", "cheerful", "excited", "friendly", "hopeful", "sad", "shouting", "terrified", "unfriendly", "whispering"],
            "en-US-JaneNeural": ["default", "angry", "cheerful", "excited", "friendly", "hopeful", "sad", "shouting", "terrified", "unfriendly", "whispering"],
            "en-US-SaraNeural": ["default", "angry", "cheerful", "excited", "friendly", "hopeful", "sad", "shouting", "terrified", "unfriendly", "whispering"],
            "en-US-JennyNeural": ["default", "angry", "assistant", "chat", "cheerful", "customerservice", "excited", "friendly", "hopeful", "newscast", "sad", "shouting", "terrified", "unfriendly", "whispering"],
            "en-US-GuyNeural": ["default", "angry", "cheerful", "excited", "friendly", "hopeful", "newscast", "sad", "shouting", "terrified", "unfriendly", "whispering"],
            "en-US-TonyNeural": ["default", "angry", "cheerful", "excited", "friendly", "hopeful", "sad", "shouting", "terrified", "unfriendly", "whispering"],
            "en-US-DavisNeural": ["default", "angry", "chat", "cheerful", "excited", "friendly", "hopeful", "sad", "shouting", "terrified", "unfriendly", "whispering"],
            "en-US-JasonNeural": ["default", "angry", "cheerful", "excited", "friendly", "hopeful", "sad", "shouting", "terrified", "unfriendly", "whispering"],
            "pt-BR-FranciscaNeural": ["default", "calm"]}
        
        self.estilos_traduzidos = {
            "default": "padrão",
            "angry": "zangado",
            "chat": "conversação",
            "cheerful": "alegre",
            "customerservice": "atendimento ao cliente",
            "empathetic": "empático",
            "excited": "animado",
            "friendly": "amigável",
            "hopeful": "esperançoso",
            "narration-professional": "narração profissional",
            "newscast-casual": "noticiário casual",
            "newscast-formal": "noticiário formal",
            "sad": "triste",
            "shouting": "gritando",
            "terrified": "aterrorizado",
            "unfriendly": "não amigável",
            "whispering": "sussurrando",
            "calm": "calmo"
        }

        # Conexões de sinais e slots
        
        self.microphoneButton.toggled.connect(self.toggleRecording)
        
        self.Traduzir_Button.clicked.connect(self.translate_text)
        
        self.Modo_Noturno_Button.toggled.connect(self.toggle_night_mode)
        
        self.Resetar_Estilo_Button.clicked.connect(lambda: self.Intensidade_Slider.setValue(10))
        
        self.Resetar_Clareza_Button.clicked.connect(lambda: self.Clareza_Slider.setValue(0))
        
        self.Resetar_Velocidade_Button.clicked.connect(lambda: self.Velocidade_Slider.setValue(0))
        
        self.Resetar_Tom_Button.clicked.connect(lambda: self.Tom_Slider.setValue(0))
        
        self.Criar_Audio_Button.clicked.connect(self.create_audio)
        
        self.Reproduzir_Previa_Button.clicked.connect(self.play_audio)
        
        self.Remover_Previa_Button.clicked.connect(self.remove_audio_preview)
        
        self.Salvar_Audio_Button.clicked.connect(self.save_audio)
        
        # Configuração dos QComboBox
        self.Tradutor_comboBox.addItem("Inglês (US)", "en")
        self.Tradutor_comboBox.addItem("Espanhol (ES)", "es")
        self.Tradutor_comboBox.addItem("Português (BR)", "pt")
        
        self.voice_model = QStandardItemModel()
        self.Vozes_comboBox.setModel(self.voice_model)
        self.add_voices_to_model()
        self.Vozes_comboBox.currentIndexChanged.connect(self.atualizar_estilos_para_voz_selecionada)
        
        # Configuração dos Sliders
        self.Intensidade_Slider.setMinimum(1)  # O valor mínimo é 1
        self.Intensidade_Slider.setMaximum(20)  # O valor máximo é 20
        self.Intensidade_Slider.setValue(10)  # Valor padrão é 10
        self.Intensidade_Slider.valueChanged.connect(self.update_intensidade_label)
        
        self.Clareza_Slider.setMinimum(-50)  # -50%
        self.Clareza_Slider.setMaximum(50)   # 50%
        self.Clareza_Slider.setValue(0)      # valor padrão (sem ajuste)
        self.Clareza_Slider.valueChanged.connect(self.update_clareza_label)
        
        self.Velocidade_Slider.setMinimum(-100)  # -50%
        self.Velocidade_Slider.setMaximum(100)   # 50%
        self.Velocidade_Slider.setValue(0)      # valor padrão (sem ajuste)
        self.Velocidade_Slider.valueChanged.connect(self.update_velocidade_label)
        
        self.Tom_Slider.setMinimum(-100)  # -50%
        self.Tom_Slider.setMaximum(100)   # 50%
        self.Tom_Slider.setValue(0)      # valor padrão (sem ajuste)
        self.Tom_Slider.valueChanged.connect(self.update_tom_label)
        
        #----------
        # Aplicar estilos e outras configurações iniciais
        self.apply_styles()
        
    def show_recording_finished(self, message):
        msg_box = QMessageBox(self)
        msg_box.setWindowIcon(QIcon(resource_path('QIcon_alertOK.png')))  # ou qualquer ícone que você prefira
        msg_box.setIcon(QMessageBox.Icon.Information)  # Altere conforme necessário
        msg_box.setWindowTitle("Gravação Concluída")
        msg_box.setText(message)
        msg_box.exec()
        
    def update_intensidade_label(self, value):
            # Atualiza o label com o valor do slider, convertendo para porcentagem
            # Assumindo que você tem um QLabel para mostrar o valor da intensidade
            self.Intensidade_label.setText(f'Intensidade do Estilo: {value*10}%')
            
    def update_clareza_label(self, value):
            # Atualiza o label com o valor do slider, convertendo para porcentagem
            # Assumindo que você tem um QLabel para mostrar o valor da intensidade
            self.Clareza_label.setText(f'Clareza da voz: {value}%')
            
    def update_velocidade_label(self, value):
            # Atualiza o label com o valor do slider, convertendo para porcentagem
            # Assumindo que você tem um QLabel para mostrar o valor da intensidade
            self.Velocidade_label.setText(f'Velocidade da voz: {value}%')
            
    def update_tom_label(self, value):
            # Atualiza o label com o valor do slider, convertendo para porcentagem
            # Assumindo que você tem um QLabel para mostrar o valor da intensidade
            self.Tom_label.setText(f'Tom da voz: {value}%')
        
    def translate_text(self):
        # Obtém o texto da aba "Texto Atual"
        original_text = self.Texto_textEdit.toPlainText()
        
        if not original_text:
            self.show_warning("Aviso!", "Por favor, insira algum texto antes de traduzir.")
            return

        # Obtenha o código do idioma de destino selecionado no QComboBox
        target_language = self.Tradutor_comboBox.currentData()

        # Configuração da requisição
        path = '/translate'
        constructed_url = AZURE_ENDPOINT + path
        params = {
            'api-version': '3.0',
            'to': [target_language]
        }
        headers = {
            'Ocp-Apim-Subscription-Key': TRANSL_SUBS_KEY,
            'Ocp-Apim-Subscription-Region': REGION,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }
        body = [{
            'text': original_text
        }]

        # Executa a requisição de tradução
        try:
            response = requests.post(constructed_url, params=params, headers=headers, json=body)
            response.raise_for_status()  # Isso vai levantar um erro se a requisição falhar

            # Processa a resposta
            translation_results = response.json()
            translated_text = translation_results[0]['translations'][0]['text']

            # Atualiza as caixas de texto das abas
            # Define o texto traduzido na aba "Texto Atual"
            self.Texto_textEdit.setPlainText(translated_text)
            # Move o texto original para a aba "Texto Original"
            self.Original_textEdit.setPlainText(original_text)

        except requests.exceptions.RequestException as e:
            print("Erro ao fazer requisição de tradução:", e)
            self.show_warning("Erro de Tradução", "Não foi possível traduzir o texto. Verifique sua conexão com a internet e tente novamente.")
        
    def atualizar_estilos_para_voz_selecionada(self):
        voz_selecionada_index = self.Vozes_comboBox.currentIndex()  # Obtém o índice selecionado
        if voz_selecionada_index != -1:
            voz_selecionada_id = self.voice_model.item(voz_selecionada_index).data(Qt.ItemDataRole.UserRole)
            estilos_suportados = self.vozes_estilos.get(voz_selecionada_id, [])
            self.Estilo_comboBox.clear()
            for estilo in estilos_suportados:
                nome_traduzido = self.estilos_traduzidos.get(estilo, estilo)  # Traduz o estilo
                self.Estilo_comboBox.addItem(nome_traduzido.capitalize(), estilo)  # Adiciona o nome traduzido, mas mantém o valor original em inglês
        else:
            self.Estilo_comboBox.clear()
    
    def add_voices_to_model(self):
        sections = [
            ("----- Português (Brasil) -----", [
                ("----- Masculino -----", None),
                ("Antonio - M (BR)", "pt-BR-AntonioNeural"),
                ("Donato - M (BR)", "pt-BR-DonatoNeural"),
                ("Fabio - M (BR)", "pt-BR-FabioNeural"),
                ("Humberto - M (BR)", "pt-BR-HumbertoNeural"),
                ("Julio - M (BR)", "pt-BR-JulioNeural"),
                ("----- Feminino -----", None),
                ("Francisca - F (BR) - Estilos disponíveis", "pt-BR-FranciscaNeural"),
                ("Brenda - F (BR)", "pt-BR-BrendaNeural"),
                ("Elza - F (BR)", "pt-BR-ElzaNeural"),
                ("Giovanna - F (BR)", "pt-BR-GiovannaNeural"),
                ("Leila - F (BR)", "pt-BR-LeilaNeural")
            ]),
        
            ("----- Inglês (EUA) -----", [
                ("----- Masculino -----", None),
                ("Guy - M (US) - Estilos disponíveis", "en-US-GuyNeural"),
                ("Tony - M (US) - Estilos disponíveis", "en-US-TonyNeural"),
                ("Davis - M (US) - Estilos disponíveis", "en-US-DavisNeural"),
                ("Jason - M (US) - Estilos disponíveis", "en-US-JasonNeural"),
                ("Brian - M (US)", "en-US-BrianNeural"),
                ("----- Feminino -----", None),
                ("Aria - F (US) - Estilos disponíveis", "en-US-AriaNeural"),
                ("Nancy - F (US) - Estilos disponíveis", "en-US-NancyNeural"),
                ("Jane - F (US) - Estilos disponíveis", "en-US-JaneNeural"),
                ("Sara - F (US) - Estilos disponíveis", "en-US-SaraNeural"),
                ("Jenny - F (US) - Estilos disponíveis", "en-US-JennyNeural")
            ]),
            
            ("----- Espanhol (Espanha) -----", [
                ("----- Masculino -----", None),
                ("Alvaro - M (ES)", "es-ES-AlvaroNeural"),
                ("Arnau - M (ES)", "es-ES-ArnauNeural"),
                ("Dario - M (ES)", "es-ES-DarioNeural"),
                ("Elias - M (ES)", "es-ES-EliasNeural"),
                ("Nil - M (ES)", "es-ES-NilNeural"),
                ("----- Feminino -----", None),
                ("Elvira - F (ES)", "es-ES-ElviraNeural"),
                ("Abril - F (ES)", "es-ES-AbrilNeural"),
                ("Estrella - F (ES)", "es-ES-EstrellaNeural"),
                ("Irene - F (ES)", "es-ES-IreneNeural"),
                ("Laia - F (ES)", "es-ES-LaiaNeural")
            ]),
        ]
        
        for language, voices in sections:
            self.add_language_section(language, voices)

    def add_language_section(self, language, voices):
    # Cria um item de seção (não selecionável) para o idioma
        language_item = QStandardItem(language)
        language_item.setSelectable(False)
        language_item.setEnabled(False)  # Faz com que o idioma não seja selecionável
        self.voice_model.appendRow(language_item)

        # Adiciona as vozes ao modelo
        for name, voice_id in voices:
            item = QStandardItem(name)
            if voice_id is None:  # Para "Masculino" e "Feminino"
                item.setSelectable(False)
                item.setEnabled(False)  # Faz com que "Masculino" e "Feminino" não sejam selecionáveis
            else:
                item.setData(voice_id, Qt.ItemDataRole.UserRole)  # Associa o ID da voz ao item
            self.voice_model.appendRow(item)
        
    def show_warning(self, title, message):
        msg_box = QMessageBox(self)
        msg_box.setWindowIcon(QIcon(resource_path('QIcon_alertNOK.png')))
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()
        
    def show_success(self, title, message):
        msg_box = QMessageBox(self)
        msg_box.setWindowIcon(QIcon(resource_path('QIcon_alertOK.png')))
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()
      
    def toggleRecording(self):
        self.isRecording = not self.isRecording  # Atualiza o estado de gravação
        if self.isRecording:
            self.startRecording()
            self.microphoneButton.setText(" **Gravando** - Fale sua frase e aguarde alguns segundos!")
        else:
            self.stopRecording()
            self.microphoneButton.setText(" Gravar Áudio do Microfone")

    def startRecording(self):
        # Configuração do serviço de reconhecimento de fala
        speech_config = speechsdk.SpeechConfig(subscription=SPEECH_SUBS_KEY, region=REGION)
        speech_config.speech_recognition_language = "pt-BR"
        audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)

        self.speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

        # Definindo os eventos
        self.speech_recognizer.recognizing.connect(self.onRecognizing)
        self.speech_recognizer.recognized.connect(self.onRecognized)
        self.speech_recognizer.canceled.connect(self.onCanceled)

        # Inicia o reconhecimento contínuo
        self.speech_recognizer.start_continuous_recognition()
        self.isRecording = True

    def onRecognizing(self, event):
        print(f"Reconhecendo: {event.result.text}")
        
    def update_button(self, isRecording):
        self.microphoneButton.setChecked(isRecording)

    def onRecognized(self, event):
        if event.result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print(f"Reconhecido: {event.result.text}")
            # Emite o sinal com o texto reconhecido
            self.update_text_signal.emit(event.result.text)
            self.update_button_state_signal.emit(False)
            self.recording_finished_signal.emit("A gravação do áudio foi concluída. Clique novamente no botão se deseja gravar mais.")
            self.stopRecording()  # Para o reconhecimento

    def onCanceled(self, event):
        if event.reason == speechsdk.CancellationReason.Error:
            print(f"Erro: {event.error_details}")
        self.update_button_state_signal.emit(False)
        self.recording_finished_signal.emit("A gravação do áudio foi concluída. Clique novamente no botão se deseja gravar mais.")
        self.stopRecording()  # Para o reconhecimento em caso de erro

    def stopRecording(self):
        if self.speech_recognizer:
            self.speech_recognizer.stop_continuous_recognition()
            self.speech_recognizer = None
            # Atualiza o estado e o texto do botão para indicar que a gravação foi concluída
            self.microphoneButton.setChecked(False)
            self.microphoneButton.setText(" Gravar Áudio do Microfone")
            self.isRecording = False
 
    def updateText(self, text):
        # Este método agora é seguro para ser chamado de outro thread
        self.Texto_textEdit.setPlainText(text)
    
    def create_audio(self):
        # Assume que Texto_textEdit é o QTextEdit na primeira aba (Texto Atual)
        texto = self.Texto_textEdit.toPlainText().strip()
        if not texto:
            self.show_warning("Aviso!", "Por favor, insira algum texto antes de criar o áudio.")
            return

        voz = self.Vozes_comboBox.currentData()
        velocidade = f"{self.Velocidade_Slider.value()}%"
        tom = f"{self.Tom_Slider.value()}%"
        estilo_fala = self.Estilo_comboBox.currentData()
        if estilo_fala is None:
            estilo_fala = 'default'  # Define 'default' se não houver estilo selecionado
        clareza = f"{self.Clareza_Slider.value()}%"
        intensidade_estilo = str(self.Intensidade_Slider.value() / 10)  # Ajusta o valor para o formato correto

        # Verifica se existe um arquivo temporário anterior e remove se necessário
        if self.temp_audio_file and os.path.exists(self.temp_audio_file):
            try:
                os.remove(self.temp_audio_file)
            except OSError as e:
                print(f"Erro ao remover o arquivo temporário: {e}")

        self.temp_audio_file = tempfile.mktemp(suffix='.wav')

        sucesso = texto_audio_azure_sslm(
            texto, voz, nome_arquivo=self.temp_audio_file, velocidade=velocidade,
            tom=tom, estilo_fala=estilo_fala, intensidade_estilo=intensidade_estilo, clareza=clareza, parent=self
        )

        if sucesso:
            self.Reproduzir_Previa_Button.setEnabled(True)
            self.Remover_Previa_Button.setEnabled(True)
            self.Salvar_Audio_Button.setEnabled(True)
        else:
            if self.temp_audio_file and os.path.exists(self.temp_audio_file):
                os.remove(self.temp_audio_file)
            self.temp_audio_file = None

    def play_audio(self):
        # Verifique se o arquivo temporário existe antes de tentar reproduzir
        if self.temp_audio_file and os.path.exists(self.temp_audio_file):
            if sys.platform.startswith('darwin'):
                subprocess.call(['open', self.temp_audio_file])
            elif sys.platform.startswith('win32'):
                os.startfile(self.temp_audio_file)
            elif sys.platform.startswith('linux'):
                subprocess.call(['xdg-open', self.temp_audio_file])
            else:
                self.show_warning("Erro!", "Não foi possível reproduzir o áudio no seu sistema operacional.")
        else:
            self.show_warning("Erro!", "O arquivo de áudio não existe ou não foi gerado corretamente.")
            
    def remove_audio_preview(self):
        if self.temp_audio_file and os.path.exists(self.temp_audio_file):
            os.remove(self.temp_audio_file)  # Remove o arquivo de áudio temporário
            self.temp_audio_file = None
            self.show_success("Prévia Removida", "A prévia do áudio foi removida com sucesso.")
            self.Reproduzir_Previa_Button.setEnabled(False)  # Desabilita o botão de reproduzir prévia
            self.Remover_Previa_Button.setEnabled(False)  # Desabilita o botão de remover prévia
            self.Salvar_Audio_Button.setEnabled(False)  # Desabilita o botão de salvar áudio
        else:
            self.show_warning("Erro", "Não existe uma prévia de áudio para remover.")
            self.Reproduzir_Previa_Button.setEnabled(False)  # Desabilita o botão de reproduzir prévia
            self.Remover_Previa_Button.setEnabled(False)  # Desabilita o botão de remover prévia
            self.Salvar_Audio_Button.setEnabled(False)  # Desabilita o botão de salvar áudio

    def save_audio(self):
        if self.temp_audio_file:
            file_path, _ = QFileDialog.getSaveFileName(self, "Salvar Áudio", filter="MP3 Files (*.mp3)")
            if file_path:
                shutil.move(self.temp_audio_file, file_path)
                self.show_success("Sucesso!", "Áudio salvo com sucesso!")
                self.Reproduzir_Previa_Button.setEnabled(False)  # Desabilita o botão de reproduzir prévia
                self.Salvar_Audio_Button.setEnabled(False)  # Desabilita o botão de salvar áudio após o salvamento
                self.Remover_Previa_Button.setEnabled(False)  # Desabilita o botão de remover prévia após o salvamento
        else:
            self.show_warning("Aviso", "Não há áudio para salvar.")
                
    def toggle_night_mode(self, checked):
        self.is_night_mode = checked
        self.apply_styles()
            
    def apply_styles(self):
        if self.is_night_mode:
            # Estilos para o modo noturno
            widget_bg_color = '#444650'
            text_color = '#ecf0f1'
            btn_hover_color = '#3e4e60'
            btn_press_color = '#2c3e50'
            btn_disabled_bg_color = '#939393'
            btn_disabled_text_color = '#474747'
            add_page_color = "#C0C0C0"
            sub_page_color = "#939393"
            slider_color = "#474747"
        else:
            # Estilos para o modo claro
            widget_bg_color = '#ffffff'
            text_color = '#333333'
            btn_hover_color = '#d3e7f2'
            btn_press_color = '#c3d7e5'
            btn_disabled_bg_color = '#e0e0e0'
            btn_disabled_text_color = '#a0a0a0'
            add_page_color = "#C0C0C0"
            sub_page_color = "#c3d7e5"
            slider_color = "#fffafa"
        
        # Aplica os estilos baseados nos valores acima
        self.setStyleSheet(f"""
            QLabel, QComboBox QAbstractItemView {{
                 color: {text_color};
            }}
            QTextEdit, QComboBox, QSlider, QMessageBox {{
                background-color: {widget_bg_color};
                color: {text_color};
                border: 1px solid #b6b6b6;
                border-radius: 3px;
            }}
            QWidget {{
                background-color: {widget_bg_color};
            }}
            QComboBox::drop-down {{
                border: 1px solid #b6b6b6;
            }}
            QPushButton {{
                background-color: {widget_bg_color};
                color: {text_color};
                padding: 6px;
                border-radius: 5px;
                border: 1px solid #b6b6b6;
                font-weight: normal;
            }}
            QPushButton:hover {{
                background-color: {btn_hover_color};
            }}
            QPushButton:pressed {{
                background-color: {btn_press_color};
            }}
            QPushButton:disabled {{
                background-color: {btn_disabled_bg_color};
                color: {btn_disabled_text_color};
            }}
            QSlider::groove:horizontal {{
                border: 1px solid #999999;
                height: 4px;
                background: qlineargradient(x1:0, x2:0, stop:0 {widget_bg_color}, stop:1 {widget_bg_color});
                margin: 2px 0;
            }}
            QSlider::handle:horizontal {{
                background: {slider_color};
                border: 1.2px solid #000000;
                width: 12px;
                margin: -3px 0;
                border-radius: 1px;
            }}
            QSlider::add-page:horizontal {{
                background: {add_page_color};
            }}
            QSlider::sub-page:horizontal {{
                background: {sub_page_color};
            }}
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
