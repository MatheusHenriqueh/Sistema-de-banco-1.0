# 🏦 Projeto Banco em Python

### 💡 Descrição
O **Projeto Banco** é um sistema simples feito em **Python**, criado para simular as funções básicas de um banco digital.  
O objetivo é praticar **lógica de programação**, uso de **condicionais (`if`, `elif`, `else`)** e **manipulação de variáveis numéricas**.

Com este projeto, o usuário pode:
- 👤 Entrar com nome e senha;
- 💸 Fazer **PIX** (com verificação de saldo antes da transferência);
- 💰 Realizar **depósitos**;
- 💵 Efetuar **saques**;
- 💳 Consultar o **saldo atualizado**;
- 🚪 Sair do sistema com segurança.

---

### ⚙️ Como Funciona
1. O usuário digita seu **nome** e **senha** para acessar o sistema.  
2. O programa pergunta se ele deseja **entrar** ou **sair**.  
3. Dentro do sistema, o usuário escolhe entre:
   - Fazer um **PIX** (transferência);
   - Fazer um **saque**;
   - Fazer um **depósito**;
4. O saldo é atualizado automaticamente a cada operação.  
5. O programa mostra mensagens diferentes conforme a escolha do usuário (usando `if`, `elif`, `else`).

---

### 🧠 Conceitos Aprendidos
- Estruturas condicionais (`if`, `elif`, `else`);
- Tipos de dados (`str`, `float`);
- Operadores aritméticos (`+=`, `-=`);  
- Entrada e saída de dados (`input()`, `print()`);
- Organização de fluxo lógico em Python.

---

### 📸 Exemplo de Uso
```python
Seja bem-vindo(a) ao banco!
Digite seu nome: Matheus
Digite sua senha: 1234
Carregando...
Seja bem-vindo(a) de volta Matheus!
Quanto de saldo tem na sua conta atualmente? 500
Quer entrar no banco? digite: entrar, se quiser sair digite: sair. entrar
Você entrou no painel do banco!
Matheus, você quer efetuar qual? pix, saque ou deposito?
se quiser fazer pix, digite: pix
pix
Carregando..
Matheus, qual número pretende fazer o pix? 11999999999
Qual o valor que deseja? 200
✅ PIX ENVIADO COM SUCESSO!
💰 Valor enviado: R$200.00
Saldo atual: R$300.00
