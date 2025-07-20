
# QR Code Social Engineering

Este projeto demonstra como um atacante pode **coletar dados de um dispositivo móvel** e até **obter acesso remoto via shell reversa** com a simples interação da vítima com um QR Code — **sem root, sem app suspeito**.

> ❗ **ATENÇÃO:** Este repositório tem **fins exclusivamente educacionais**. Todo o teste foi realizado em **ambiente controlado** com dispositivos de laboratório. **Não use este código para fins maliciosos.**

---

## 📌 Objetivo

Alertar sobre os riscos de escanear QR Codes de fontes desconhecidas, mostrando na prática como um simples QR pode iniciar:

- Coleta de dados do dispositivo (user agent, idioma, bateria, localização)
- Download de script com shell reversa sem que o usuário perceba
- Conexão do atacante com o dispositivo Android (via Termux)

---

## 📁 Estrutura dos arquivos

| Arquivo       | Descrição |
|---------------|-----------|
| `index.html`  | Página falsa com imagem de “wallpaper exclusivo” e botão que coleta dados e execução do payload |
| `payload.sh`  | Script Bash que, ao ser executado, abre uma conexão reversa com o atacante |
| `coleta.py`   | Servidor Python que recebe e imprime os dados coletados via POST |
| `imagem.png`  | Imagem ilustrativa usada como isca (você pode usar qualquer imagem aqui) |

---

## ⚙️ Como usar (ambiente local)

### 1. Inicie o servidor de coleta de dados
```bash
python3 coleta.py
# Servidor rodando em http://SEU-IP:9090
```

### 2. Inicie um servidor HTTP simples
```bash
# No diretório onde está o index.html, imagem e rev.sh
python3 -m http.server 8080
```

### 3. Gere o QR Code apontando para a isca
```bash
qrencode -o final_qr.png "http://SEU-IP:8080/index.html"
```

### 4. Deixe seu Kali ouvindo
```bash
nc -lvnp 4444
```

---

## 📲 O que a vítima vê

Ao escanear o QR:
1. O celular acessa a página do "wallpaper"
2. Ao clicar no botão "Baixar", os dados do dispositivo são enviados para o servidor
3. A imagem é exibida normalmente (nada suspeito)
4. O script `payload.sh` é executado ou pode ser baixado e executado de forma manual no Termux (se a vítima for induzida a isso)

---

## ⚠️ Aviso Legal

Este projeto foi criado com a finalidade de **ensinar e alertar** sobre técnicas utilizadas em golpes reais. **Não é um tutorial de invasão**.

**Invadir sistemas sem autorização é crime**. O uso indevido desse conteúdo é de responsabilidade exclusiva do usuário.

---

## 🧠 Créditos

Desenvolvido por [Douglas Lockshield](https://www.youtube.com/@douglaslockshield) para o canal como parte de um conteúdo de conscientização em segurança da informação.
