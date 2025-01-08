# Conversor de Texto em Áudio - Giovanne

[![Versão](https://img.shields.io/badge/vers%C3%A3o-2.0-blue.svg)](https://shields.io/) [![python](https://img.shields.io/badge/python-3.12.2-blue.svg)](https://shields.io/) [![Versão](https://img.shields.io/badge/PyQt6-6.6.1-blue.svg)](https://shields.io/)

## 🚀 Sobre o Projeto

Olá a todos! 🙋‍♂️

Estou extremamente animado em compartilhar com vocês a versão 2.0 do meu projeto pessoal, o "Conversor de Texto em Áudio - Giovanne". Este é um software desenvolvido em Python utilizando a interface gráfica PyQt6, projetado para converter texto em áudio com uma variedade de opções e funcionalidades. Após muito esforço e dedicação, consegui implementar diversas melhorias e novos recursos que gostaria de destacar:

## ✨ Novidades da Versão 2.0

*   **Layout Aprimorado com Qt Designer**: O software foi completamente redesenhado com o auxílio do Qt Designer, trazendo um layout mais limpo, organizado e intuitivo. A interface agora é mais amigável e visualmente agradável, tornando a experiência do usuário mais fluida e agradável.
*   **Ícones Customizados**: Para melhorar ainda mais a experiência do usuário, adicionei ícones customizados para a janela principal, janelas de alerta e botões. Esses ícones tornam o software mais intuitivo e fácil de navegar, além de darem um toque especial ao design.
*   **Modo Noturno On/Off**: Pensando no conforto visual, implementei um modo noturno que pode ser facilmente ativado ou desativado com um clique. Este recurso é ideal para uso em ambientes com pouca luz, reduzindo o cansaço visual e proporcionando uma experiência mais confortável.
*   **Gravação de Áudio por Microfone**: Agora, além de digitar o texto, você também pode simplesmente falar que o software se encarrega de converter sua voz em texto! Isso é possível graças à integração com o serviço Speech to Text da Microsoft Azure, que traz mais praticidade e acessibilidade ao projeto.
*   **30 Vozes em Diversas Línguas**: Expandindo as capacidades do software, incluí uma seleção de 30 vozes diferentes, separadas por gênero e idioma (Português, Inglês e Espanhol). Essa diversidade permite que os usuários escolham a voz que melhor se adapta às suas preferências ou necessidades.
*   **Tradução Multilíngue**: Adicionei a funcionalidade de tradução de texto para três idiomas: Inglês, Espanhol e Português. O software não só traduz o texto digitado ou falado, como também mantém o texto original para comparação. Essa função é alimentada pelo serviço Translator Text da Microsoft Azure.
*   **Controle Total sobre o Áudio**: Com a adição de novos sliders, agora é possível ajustar o estilo de fala (para vozes selecionadas que suportam essa funcionalidade) e a clareza (volume) do áudio. Isso permite uma personalização ainda maior do áudio gerado, oferecendo aos usuários controle total sobre as características da voz.
*   **Arquivo Executável**: Para simplificar a distribuição e o uso do software, transformei o projeto em um arquivo executável (.exe). Isso significa que agora o conversor pode ser executado diretamente do desktop, sem a necessidade de ter um ambiente de desenvolvimento Python configurado ou de rodar o código pelo editor.

## 🛠️ Tecnologias Utilizadas

*   **Python**: Linguagem de programação principal.
*   **PyQt6**: Para a interface gráfica.
*   **Microsoft Azure Cognitive Services**: Para reconhecimento de fala (Speech to Text) e tradução (Translator Text).

## 💻 Pré-requisitos

Antes de começar, você precisará ter instalado:

*   Python 3.12.2
*   As bibliotecas listadas no arquivo [requirements.txt](requirements.txt)
*   Uma conta da Microsoft Azure e as chaves de API para os serviços Speech e Translator (veja a seção "Configuração das Chaves de API" abaixo).

## 🚀 Como Instalar

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/GiooooBotelho/conversor-gio.git
    cd conversor-gio
    ```

2. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Modificar a Interface (opcional):**
   * Se você quiser modificar a interface gráfica, você pode editar o arquivo `meu_layout.ui` usando o **Qt Designer**.
   * Depois de modificar o arquivo `.ui`, você precisará convertê-lo para um script Python. Use o seguinte comando no terminal, estando na pasta onde se encontra o arquivo `meu_layout.ui`:

     ```bash
     pyuic6 -x meu_layout.ui -o meu_layout.py
     ```

     Isso atualizará o arquivo `meu_layout.py` com as suas modificações.

## ⚙️ Configuração das Chaves de API

Para usar os serviços da Microsoft Azure, você precisará configurar suas chaves de API:

**1. Criar uma conta no Azure:**

* Acesse o portal do Azure: [portal.azure.com](https://portal.azure.com) 
* Se você ainda não tem uma conta, crie uma gratuitamente.

**2. Criar recursos para os serviços:**

* **Speech service:**
    * No portal do Azure, procure por "Speech" e selecione "Speech".
    * Clique em "Criar".
    * Escolha uma assinatura, crie um novo grupo de recursos e dê um nome ao seu recurso.
    * Selecione a região mais próxima de você.
    * Escolha o plano de preços (o plano gratuito é uma boa opção para começar).
    * Clique em "Revisar + criar" e depois em "Criar".
    * Após a criação do recurso, acesse-o no portal do Azure.
    * No menu à esquerda, em "Gerenciamento de recursos", clique em "Chaves e Ponto de Extremidade".
    * Copie a chave (uma das duas listadas) e a região. Anote esses valores.
    * A `SPEECH_SUBS_KEY` será essa chave que você copiou.
    * A `REGION` será a região que você selecionou ao criar o recurso.

* **Translator service:**
    * No portal do Azure, procure por "Translator" e selecione "Translator".
    * Repita os passos acima para criar o recurso do Translator.
    * Copie a chave e a região. A `TRANSL_SUBS_KEY` será essa chave que você copiou.

**3. Criar o arquivo `.env`:**
1. Crie um arquivo chamado `.env` na raiz do projeto.
2. Abra o arquivo `.env` e adicione suas chaves de API e a região, substituindo os valores pelas chaves e região que você obteve, como mostrado abaixo:

    ```
    SPEECH_SUBS_KEY=sua_chave_do_speech_service
    TRANSL_SUBS_KEY=sua_chave_do_translator_text
    REGION=sua_regiao
    AZURE_ENDPOINT=https://api.cognitive.microsofttranslator.com
    ```

    Substitua `sua_chave_do_speech_service`, `sua_chave_do_translator_text` e `sua_regiao` pelas informações da sua conta do Azure.

**4. Proteger suas chaves:**

* **Segurança:** Mantenha suas chaves de API em segredo. Não as compartilhe publicamente e não as inclua diretamente no código-fonte do seu projeto.
* **.gitignore:** Adicione o arquivo `.env` ao seu `.gitignore` para que ele não seja incluído no seu repositório Git.

## ▶️ Como Executar

Para executar o aplicativo, use o seguinte comando no terminal:

    ```bash
    python azure_pyqt6.py
    ```

## 📦 Como Gerar o Executável (Avançado)
Se você quiser criar um arquivo executável (.exe) para distribuir o aplicativo sem que os usuários precisem instalar o Python e as dependências, siga estas etapas:

Certifique-se de ter o cx_Freeze instalado. Se não tiver, instale-o com o seguinte comando:

    ```bash
    pip install cx_Freeze
    ```
    
Execute o script setup.py usando o seguinte comando no terminal, estando na pasta raiz do projeto onde o setup.py se encontra:

    ```bash
    python setup.py build
    ```

Isso criará uma pasta build contendo o executável e os arquivos necessários.

**Observação: Você precisará incluir manualmente a DLL Microsoft.CognitiveServices.Speech.core.dll na pasta do executável, se ela não for incluída automaticamente pelo cx_Freeze.**

## 🤝 Contribuições

Contribuições são sempre bem-vindas! Se você quiser contribuir, por favor, siga os passos abaixo:

1. Faça um fork do projeto.
2. Crie uma nova branch para sua funcionalidade (`git checkout -b feature/sua-funcionalidade`).
3. Faça commit das suas alterações (`git commit -am 'Adiciona funcionalidade'`).
4. Faça push para a branch (`git push origin feature/sua-funcionalidade`).
5. Abra um Pull Request.

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para detalhes.

## 📫 Contato

Giovanne - giovannebotelho1@gmail.com

Link do Projeto: [\[conversor-gio\]](https://github.com/GiooooBotelho/conversor-gio.git)