# 📘 Sistema de Otimização do Tempo de Estudo

Este projeto implementa um sistema simples e intuitivo para recomendar o **tempo ideal de estudo diário**, utilizando **modelagem matemática de aprendizado e fadiga**, além de **derivadas via SymPy**.

O sistema foi desenvolvido atendendo aos requisitos do projeto da disciplina *Resolução Diferencial de Problemas (2º Bimestre)*.

---

## 🚀 Tecnologias utilizadas
- **Python 3**
- **Flask** (backend web)
- **SymPy** (cálculo simbólico e otimização)
- **HTML + CSS puro** (frontend simples)

---

## 🎯 Objetivo do Sistema
O sistema calcula o tempo ótimo de estudo \(h^*\) equilibrando dois fatores:

- **Retenção de aprendizado** (curva saturada exponencial)
- **Fadiga cognitiva** (função convexa)

A modelagem considera variáveis subjetivas do usuário como sono, motivação, stress, dificuldade da matéria, etc.

O resultado apresentado é o ponto em que **o ganho cognitivo supera o cansaço**, representando o melhor momento para parar de estudar.

---

## 📂 Estrutura de Pastas
```
projeto/
│
├── app.py              # Backend Flask
├── /templates
│     └── index.html    # Interface web com HTML + CSS + Jinja
└── README.md           # Este arquivo
```

---

## ⚙️ Como executar o projeto

### 1️⃣ Instale as dependências
```bash
pip install flask sympy
```

### 2️⃣ Execute a aplicação
```bash
python app.py
```

### 3️⃣ Abra no navegador
```
http://127.0.0.1:5000/
```

⚠️ **Importante:** Não utilize extensões como *VSCode Live Server*, pois Jinja só funciona via Flask.

---

## 🧠 Como o cálculo funciona
O sistema usa as seguintes funções:

### **Retenção de aprendizado**
\[
R(h) = A(1 - e^{-kh})
\]

### **Fadiga cognitiva**
\[
F(h) = c h^2
\]

### **Aprendizado líquido**
\[
L(h) = R(h) - F(h)
\]

### **Tempo ótimo**
O sistema resolve:
\[
L'(h) = 0
\]
usando SymPy para encontrar \(h*\).

Os parâmetros \(A\), \(k\) e \(c\) são estimados automaticamente com base nas respostas do usuário.

---

## 📋 Campos coletados do usuário
Cada variável é respondida em uma escala simples (1 a 5):

- Qualidade do sono
- Nível de energia
- Foco / concentração
- Familiaridade com o conteúdo
- Dificuldade da matéria
- Nível de stress
- Distrações do ambiente
- Motivação

Essas respostas são convertidas nos parâmetros matemáticos do modelo.

---

## 🎨 Interface
A interface é minimalista, responsiva e amigável, construída apenas com **HTML e CSS**

O resultado aparece em um cartão verde explicando:
- Tempo ótimo recomendado
- Interpretação do modelo

---

## 📚 Fundamentação Teórica (Resumida)
- **Curva de aprendizagem**: Newell & Rosenbloom (1981) — justifica \(R(h)\) saturada.
- **Fadiga cognitiva**: Hancock & Desmond (2001) — justifica \(F(h)\) crescente não linear.
- **Otimização benefício − custo**: modelo clássico de maximização.

---

## 🧪 Possíveis melhorias
- Sistema de histórico por usuário
- Modo "avançado" exibindo parâmetros A, k, c
- Exportar relatório em PDF

---

## 👨‍💻 Autor
Projeto desenvolvido para fins acadêmicos no CESUPA.
Alunos: José Joaquim Valdez, Jorge Lobato e Lucas Mesquita

---

## 📝 Licença
Código livre para uso acadêmico.
