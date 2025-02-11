# PPTXSlice
# 📂 Divisor de Apresentações PowerPoint

**Link: https://pptxslice.onrender.com**

Este projeto é uma aplicação web desenvolvida com **Flask** no backend e **HTML, CSS e JavaScript** no frontend. Ele permite que os usuários façam **upload de um arquivo PowerPoint**, escolham em **quantas partes** desejam dividi-lo e façam o **download automático dos arquivos gerados. Essa tarefa é frequentemente utilizada no meu ambiente de trabalho devido a grandes quantidades de relatórios e a necessidade de envio de partes para outros setores**.

## 🚀 Funcionalidades

✅ Upload de arquivos PowerPoint (`.pptx`)  
✅ Escolha do número de divisões  
✅ Configuração manual dos intervalos de slides  
✅ Nomeação personalizada dos arquivos gerados  
✅ Geração automática de múltiplos PowerPoints  
✅ Download direto de um arquivo ZIP contendo os arquivos gerados  

---

## 🛠️ Tecnologias Utilizadas

### **Frontend**
- **HTML** → Estrutura da interface
- **CSS** → Estilização responsiva
- **JavaScript** → Manipulação de DOM e comunicação com o backend

### **Backend**
- **Flask** → Framework para criação da API
- **Gunicorn** → Servidor para rodar o Flask em produção
- **python-pptx** → Manipulação e edição de arquivos PowerPoint

---

## 📌 Como Rodar o Projeto Localmente

### **1️⃣ Clonar o Repositório**
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### **2️⃣ Criar um Ambiente Virtual**
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### **3️⃣ Instalar as Dependências**
```bash
pip install -r requirements.txt
```

### **4️⃣ Rodar a Aplicação**
```bash
python app.py
```
Agora, acesse no navegador: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---
