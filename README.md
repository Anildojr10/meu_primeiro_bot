# 🤖 Byte — o assistente de IA da turma

Um assistente de conversa feito **só com fundamentos de Python** (variáveis, condicionais, funções, listas, loops e dicionários) que pode, opcionalmente, se conectar a um LLM de verdade.

## O que ele faz
- Entende a **intenção** da mensagem (saudação, Python, IA, piada, motivação...)
- Faz **análise de sentimento** (😀 😐 😟), inclusive com negação ("não gostei")
- Bloqueia **dados sensíveis** (guardrail)
- Tem **ferramentas**: `/media`, `/tabuada`, `/historico`, `/resumo`, `/temperatura`, `/cerebro`, `/dado`
- Guarda o histórico no **mesmo formato das APIs de LLM** (lista de dicionários)
- Com um `.env` configurado, passa a responder usando um **LLM** (Groq, Gemini, OpenAI ou Ollama)

## Como rodar
Não precisa instalar nada além do Python 3.11+.

```bash
python byte.py          # conversa com o Byte
python byte.py --demo   # o Byte conversa sozinho (modo apresentação)
```

## Ligando um LLM (opcional)
1. Copie `.env.exemplo` e renomeie a cópia para `.env`
2. Descomente as linhas de **um** provedor e cole sua chave
3. Rode `python byte.py`: o banner mostra **✨ LLM conectado**

> 🔐 O `.env` está no `.gitignore` e **nunca** deve ir para o GitHub.

## Estrutura
```
byte-assistente-ia/
├── byte.py                          # o assistente (procure por 🧩 para achar cada fundamento)
├── Aula_Python_para_IA_Byte.ipynb   # notebook da aula: desmonta o Byte peça por peça
├── ROTEIRO_PROFESSOR.md             # tempos, falas e dicas para conduzir a aula
├── .env.exemplo                     # modelo de configuração do LLM (sem chave)
├── .gitignore                       # impede que o .env vá para o GitHub
└── README.md
```

## O que eu mudei
_(aluno: descreva aqui os desafios "Turbine o Byte" que você fez)_
