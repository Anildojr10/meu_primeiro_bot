"""
🤖 BYTE — o assistente de IA da turma
=====================================

Um assistente de conversa feito SÓ com os fundamentos de Python:
variáveis, tipos, condicionais, funções, listas, loops e dicionários.

Ele tem dois "cérebros":
  🧠 Cérebro offline  → regras + palavras-chave (como as IAs de texto antigas)
  ✨ Cérebro LLM      → um modelo de linguagem de verdade (ChatGPT, Llama, Gemini...)
                        Só liga se você colocar uma chave no arquivo .env

Como rodar (no terminal, dentro desta pasta):
    python byte.py           → conversa com o Byte
    python byte.py --demo    → o Byte conversa sozinho (ótimo para projetar na aula)

🔎 DICA PARA A AULA: procure por "🧩" neste arquivo.
   Cada marcação mostra qual fundamento de Python está sendo usado ali.
"""

import json             # transforma dicionário Python ⇄ texto JSON (o idioma das APIs)
import os               # acessa variáveis de ambiente (onde mora a chave da API)
import random           # sorteios — é a "criatividade" do Byte
import sys              # argumentos do terminal e saída de texto
import time             # pausas para o efeito de digitação
import urllib.request   # faz chamadas pela internet (sem instalar nada!)


# ════════════════════════════════════════════════════════════════════
# 1. CONFIGURAÇÃO
# 🧩 VARIÁVEIS E TIPOS — toda IA começa com configurações.
#    Repare: são exatamente os mesmos parâmetros que você passa para o ChatGPT!
# ════════════════════════════════════════════════════════════════════

NOME_BOT = "Byte"          # str   → o nome do assistente
VERSAO = 1                 # int   → número inteiro
TEMPERATURA = 0.7          # float → 0.0 = previsível · 1.0 = criativo (igualzinho aos LLMs)
MODO_DEBUG = False         # bool  → mostrar ou não o "cérebro" funcionando
MAX_HISTORICO = 20         # int   → quantas mensagens a IA "lembra" (janela de contexto)
VELOCIDADE_DIGITACAO = 0.012  # float → segundos entre cada letra

# 🧩 F-STRING — o "prompt de sistema": a personalidade do Byte quando usa um LLM.
PROMPT_SISTEMA = (
    f"Você é o {NOME_BOT}, um assistente bem-humorado de uma turma que está "
    f"aprendendo Python para Inteligência Artificial. Responda em português do Brasil, "
    f"em no máximo 3 frases, com leveza e um emoji de vez em quando."
)


# ════════════════════════════════════════════════════════════════════
# 2. BASE DE CONHECIMENTO
# 🧩 DICIONÁRIOS + LISTAS — cada intenção é uma chave; dentro dela,
#    uma lista de palavras-gatilho e uma lista de respostas possíveis.
# ════════════════════════════════════════════════════════════════════

INTENCOES = {
    "saudacao": {
        "palavras": ["oi", "ola", "eae", "salve", "opa", "hello", "hey", "bom", "boa"],
        "respostas": [
            "Olá! Eu sou o Byte 🤖 Bora aprender Python?",
            "E aí! Pronto pra programar umas IAs hoje?",
            "Salve! Manda a pergunta que eu tô ligado ⚡",
        ],
    },
    "python": {
        "palavras": ["python", "variavel", "variaveis", "lista", "listas", "funcao",
                     "funcoes", "loop", "for", "while", "if", "dicionario", "codigo", "programar"],
        "respostas": [
            "Python é a língua oficial da IA 🐍 Quase todo modelo famoso é treinado usando Python (PyTorch, TensorFlow)!",
            "Fun fact: eu mesmo sou feito só de variáveis, listas, loops, funções e dicionários.",
            "Dica de ouro: programação se aprende programando. Abre o VS Code e quebra tudo! 💥",
        ],
    },
    "ia": {
        "palavras": ["ia", "inteligencia", "artificial", "chatgpt", "gpt", "llm", "modelo",
                     "claude", "gemini", "robo", "robos", "token", "tokens", "prompt"],
        "respostas": [
            "Um LLM lê sua frase como uma LISTA de pedaços (tokens) e prevê o próximo, um de cada vez 🧩",
            "Sabia que o histórico de uma conversa com o ChatGPT é só uma lista de dicionários? Eu guardo o meu igualzinho!",
            "Temperatura é só uma variável float: baixa = respostas certinhas, alta = respostas criativas 🌡️",
        ],
    },
    "piada": {
        "palavras": ["piada", "piadas", "rir", "engracado", "zoeira", "humor", "graca"],
        "respostas": [
            "Por que o Python não vai à praia? Porque ele tem medo de IndentationError na areia 🏖️",
            "Qual o animal favorito do programador? O bug. Ele aparece em todo lugar 🐛",
            "Eu ia contar uma piada sobre loop infinito... eu ia contar uma piada sobre loop infinito... eu ia...",
            "Existem 10 tipos de pessoas: as que entendem binário e as que não entendem.",
        ],
    },
    "motivacao": {
        "palavras": ["dificil", "desistir", "cansado", "cansada", "medo", "travado",
                     "travada", "perdido", "perdida", "consigo", "ajuda"],
        "respostas": [
            "Todo dev sênior já foi o júnior que não entendia o 'for'. Você está no caminho certo 💪",
            "Erro não é fracasso, é o Python te dando uma dica de graça. Lê a mensagem com calma!",
            "Respira, quebra o problema em pedaços menores (funções!) e resolve um de cada vez 🧘",
        ],
    },
    "elogio": {
        "palavras": ["obrigado", "obrigada", "valeu", "top", "show", "incrivel", "demais", "massa"],
        "respostas": [
            "Valeu! Mas o mérito é de quem escreveu meu código 😎",
            "Tamo junto! 🤝",
        ],
    },
}

# Respostas para quando o Byte não entende nada (intenção desconhecida)
RESPOSTAS_CONFUSO = [
    "Hmm, não entendi 🤔 Tenta falar de Python, IA, pedir uma piada ou digitar /ajuda.",
    "Meu cérebro offline é pequeno! Liga um LLM no arquivo .env e eu fico bem mais esperto ✨",
    "Essa eu não sei... ainda! Que tal você me ensinar adicionando uma intenção no dicionário INTENCOES?",
]

# 🧩 LISTAS — vocabulário do analisador de sentimento
PALAVRAS_POSITIVAS = ["bom", "boa", "otimo", "otima", "legal", "feliz", "amei", "gostei",
                      "adorei", "incrivel", "top", "show", "massa", "demais", "consegui", "facil"]
PALAVRAS_NEGATIVAS = ["ruim", "pessimo", "triste", "odiei", "chato", "chata", "dificil",
                      "erro", "bug", "cansado", "cansada", "medo", "travado", "travada", "raiva"]

# 🧩 LISTA — guardrail: palavras que o Byte se recusa a processar
PALAVRAS_BLOQUEADAS = ["senha", "cartao", "cpf"]

# 🧩 DICIONÁRIO — tabela para remover acentos (pré-processamento de texto)
ACENTOS = {"á": "a", "à": "a", "ã": "a", "â": "a", "é": "e", "ê": "e", "í": "i",
           "ó": "o", "ô": "o", "õ": "o", "ú": "u", "ü": "u", "ç": "c"}


# ════════════════════════════════════════════════════════════════════
# 3. PRÉ-PROCESSAMENTO DE TEXTO
# Antes de qualquer IA entender um texto, ela limpa e quebra em pedaços.
# ════════════════════════════════════════════════════════════════════

# 🧩 FUNÇÃO com parâmetro e return
def limpar_texto(texto):
    """Deixa o texto minúsculo, sem acentos e sem pontuação."""
    texto = texto.lower()
    # 🧩 FOR em dicionário com .items() — troca cada letra acentuada
    for com_acento, sem_acento in ACENTOS.items():
        texto = texto.replace(com_acento, sem_acento)
    # 🧩 FOR em string — uma string também é uma sequência!
    for sinal in "?!.,;:()\"'":
        texto = texto.replace(sinal, " ")
    return texto


def tokenizar(texto):
    """Quebra o texto em uma LISTA de palavras (tokens). É o 1º passo de todo LLM."""
    # 🧩 LISTA — .split() devolve uma lista de strings
    return limpar_texto(texto).split()


# ════════════════════════════════════════════════════════════════════
# 4. O CÉREBRO OFFLINE
# ════════════════════════════════════════════════════════════════════

def detectar_intencao(tokens):
    """Descobre O QUE a pessoa quer, contando palavras-gatilho. Devolve (intencao, confianca)."""
    melhor_intencao = "desconhecida"   # str
    melhor_pontuacao = 0               # int

    # 🧩 FOR em dicionário — testa cada intenção
    for intencao, dados in INTENCOES.items():
        # 🧩 LIST COMPREHENSION — quais tokens da frase estão na lista de gatilhos?
        acertos = [t for t in tokens if t in dados["palavras"]]
        pontuacao = len(acertos)

        # 🧩 CONDICIONAL — guarda a intenção com mais acertos
        if pontuacao > melhor_pontuacao:
            melhor_pontuacao = pontuacao
            melhor_intencao = intencao

    # 🧩 CONDICIONAL + DIVISÃO → confiança é um float entre 0 e 1
    if len(tokens) > 0:
        confianca = melhor_pontuacao / len(tokens)
    else:
        confianca = 0.0

    return melhor_intencao, round(confianca, 2)


def analisar_sentimento(tokens):
    """Classifica o 'clima' da mensagem: positivo, negativo ou neutro."""
    positivos = len([t for t in tokens if t in PALAVRAS_POSITIVAS])
    negativos = len([t for t in tokens if t in PALAVRAS_NEGATIVAS])
    pontuacao = positivos - negativos

    # 🧩 OPERADOR LÓGICO — "não" inverte o sentimento ("não gostei" ≠ "gostei")
    if "nao" in tokens and pontuacao != 0:
        pontuacao = -pontuacao

    # 🧩 IF / ELIF / ELSE — três caminhos possíveis
    if pontuacao > 0:
        rotulo, emoji = "positivo", "😀"
    elif pontuacao < 0:
        rotulo, emoji = "negativo", "😟"
    else:
        rotulo, emoji = "neutro", "😐"

    # 🧩 DICIONÁRIO como retorno — várias informações num pacote só
    return {"rotulo": rotulo, "emoji": emoji, "pontuacao": pontuacao}


# 🧩 PARÂMETRO COM VALOR PADRÃO — se ninguém informar, usa 0.7
def escolher_resposta(respostas, temperatura=TEMPERATURA):
    """Temperatura baixa = sempre a 1ª resposta. Alta = sorteia. Igual a um LLM!"""
    if temperatura < 0.3:
        return respostas[0]           # 🧩 ÍNDICE de lista: sempre a primeira
    return random.choice(respostas)   # sorteio = "criatividade"


def tem_conteudo_bloqueado(tokens):
    """Guardrail: a IA não deve receber dados sensíveis."""
    # 🧩 FOR + BREAK — parou de procurar assim que achou
    bloqueado = False
    for token in tokens:
        if token in PALAVRAS_BLOQUEADAS:
            bloqueado = True
            break
    return bloqueado


def responder_offline(texto, estado):
    """🧩 COMPOSIÇÃO DE FUNÇÕES — a função principal só chama quem sabe fazer cada parte."""
    tokens = tokenizar(texto)
    intencao, confianca = detectar_intencao(tokens)
    sentimento = analisar_sentimento(tokens)

    if estado["debug"]:
        mostrar_cerebro(tokens, intencao, confianca, sentimento)

    # 🧩 NOT — se NÃO entendeu nada, resposta de "confuso"
    if intencao not in INTENCOES:
        return escolher_resposta(RESPOSTAS_CONFUSO, estado["temperatura"])

    resposta = escolher_resposta(INTENCOES[intencao]["respostas"], estado["temperatura"])

    # 🧩 AND — empatia: sentimento negativo E não pediu motivação → acrescenta apoio
    if sentimento["rotulo"] == "negativo" and intencao != "motivacao":
        resposta = "Senti um clima meio pesado aí... " + resposta
    return resposta


def mostrar_cerebro(tokens, intencao, confianca, sentimento):
    """Mostra o que o Byte 'pensou' — ligue com /cerebro."""
    print("   ┌─ 🧠 cérebro do Byte ───────────────")
    print(f"   │ tokens     : {tokens}")
    print(f"   │ intenção   : {intencao} (confiança {confianca:.0%})")
    print(f"   │ sentimento : {sentimento['emoji']} {sentimento['rotulo']} ({sentimento['pontuacao']:+d})")
    print("   └────────────────────────────────────")


# ════════════════════════════════════════════════════════════════════
# 5. O CÉREBRO LLM (opcional)
# 🧩 GIT/.ENV — a chave da API mora no arquivo .env, que está no .gitignore.
# ════════════════════════════════════════════════════════════════════

def carregar_env(caminho=None):
    """Lê o arquivo .env linha por linha e guarda cada CHAVE=VALOR no ambiente."""
    if caminho is None:   # por padrão, procura o .env na mesma pasta do byte.py
        caminho = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    if not os.path.exists(caminho):
        return
    with open(caminho, encoding="utf-8") as arquivo:
        # 🧩 FOR em arquivo + CONTINUE para pular linhas vazias e comentários
        for linha in arquivo:
            linha = linha.strip()
            if linha == "" or linha.startswith("#") or "=" not in linha:
                continue
            chave, valor = linha.split("=", 1)
            os.environ.setdefault(chave.strip(), valor.strip().strip('"').strip("'"))


def config_llm():
    """🧩 os.environ é um DICIONÁRIO! E .get() evita KeyError quando a chave não existe."""
    return {
        "chave": os.environ.get("LLM_API_KEY", ""),
        "url": os.environ.get("LLM_BASE_URL", "https://api.openai.com/v1"),
        "modelo": os.environ.get("LLM_MODELO", "gpt-4o-mini"),
    }


def llm_disponivel():
    cfg = config_llm()
    # 🧩 OR — tem chave OU é um modelo local (Ollama não precisa de chave)
    return cfg["chave"] != "" or "localhost" in cfg["url"]


def montar_requisicao(historico, temperatura):
    """O pedido enviado ao LLM é... um DICIONÁRIO com uma LISTA DE DICIONÁRIOS dentro!"""
    cfg = config_llm()
    mensagem_sistema = {"role": "system", "content": PROMPT_SISTEMA}
    # 🧩 FATIAMENTO [-N:] — só as últimas N mensagens (janela de contexto)
    mensagens = [mensagem_sistema] + historico[-MAX_HISTORICO:]
    return {
        "model": cfg["modelo"],       # str
        "messages": mensagens,        # list de dict
        "temperature": temperatura,   # float
        "max_tokens": 1024,           # int (modelos que "pensam" antes de responder gastam tokens raciocinando)
    }


def responder_com_llm(historico, estado):
    """Envia o histórico para um LLM compatível com a API da OpenAI e devolve o texto."""
    cfg = config_llm()
    pedido = montar_requisicao(historico, estado["temperatura"])

    if estado["debug"]:
        print("   ┌─ 📦 o que vai para o LLM (é só um dicionário!) ─")
        print("   │ " + json.dumps(pedido, ensure_ascii=False)[:300] + "...")
        print("   └────────────────────────────────────────────────")

    requisicao = urllib.request.Request(
        url=cfg["url"].rstrip("/") + "/chat/completions",
        data=json.dumps(pedido).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {cfg['chave']}",
            "User-Agent": "byte-aula-python/1.0",
        },
        method="POST",
    )
    # (spoiler de aula futura: try/except trata erros sem o programa quebrar)
    try:
        with urllib.request.urlopen(requisicao, timeout=30) as resposta_http:
            dados = json.loads(resposta_http.read().decode("utf-8"))
        # 🧩 DICIONÁRIOS e LISTAS aninhados — o "caminho" até o texto da resposta
        texto = dados["choices"][0]["message"]["content"] or ""
        if texto.strip() == "":
            print("   ⚠️  O LLM respondeu vazio. Voltando ao cérebro offline.")
            return None
        return texto.strip()
    except Exception as erro:
        print(f"   ⚠️  O LLM não respondeu ({erro}). Voltando ao cérebro offline.")
        return None


# ════════════════════════════════════════════════════════════════════
# 6. COMANDOS ESPECIAIS (as "ferramentas" do Byte)
# Em agentes de IA, isso se chama "tools" ou "function calling":
# o modelo decide qual FUNÇÃO chamar. Aqui, um dicionário liga nome → função.
# ════════════════════════════════════════════════════════════════════

def cmd_ajuda(argumentos, estado, historico):
    print("   📋 Comandos do Byte:")
    # 🧩 FOR em dicionário — a própria lista de comandos gera a ajuda!
    for nome, info in COMANDOS.items():
        print(f"      {nome:<14} {info['descricao']}")
    print("      sair           encerra a conversa")


def cmd_media(argumentos, estado, historico):
    """/media 7 8.5 9 → calcula a média e classifica (lembra da Aula 1?)"""
    if len(argumentos) == 0:
        print("   Use assim: /media 7 8.5 9")
        return
    # 🧩 CONVERSÃO DE TIPO — tudo que vem do teclado é str; float() transforma em número
    # (troca vírgula por ponto para aceitar "8,5" também)
    try:
        notas = [float(a.replace(",", ".")) for a in argumentos]
    except ValueError:
        print("   Ops! Só aceito números 😅  Exemplo: /media 7 8.5 9")
        return
    media = sum(notas) / len(notas)

    if media >= 9:
        conceito = "Excelente 🏆"
    elif media >= 7:
        conceito = "Bom 👍"
    elif media >= 5:
        conceito = "Regular 😬"
    else:
        conceito = "Insuficiente 📚"
    print(f"   Notas: {notas} → média {media:.2f} · {conceito}")


def cmd_tabuada(argumentos, estado, historico):
    """/tabuada 7 → 🧩 FOR com RANGE"""
    # 🧩 AND — tem argumento E é um número inteiro?
    if len(argumentos) > 0 and argumentos[0].isdigit():
        numero = int(argumentos[0])
    else:
        numero = 7
    for i in range(1, 11):
        print(f"   {numero} x {i:>2} = {numero * i}")


def cmd_historico(argumentos, estado, historico):
    """🧩 ENUMERATE — número + item ao mesmo tempo"""
    if not historico:
        print("   (ainda não conversamos 😶)")
        return
    for i, mensagem in enumerate(historico, start=1):
        quem = "Você" if mensagem["role"] == "user" else NOME_BOT
        print(f"   {i:>2}. {quem}: {mensagem['content']}")


def cmd_resumo(argumentos, estado, historico):
    """Estatísticas da conversa com 🧩 LIST COMPREHENSION + funções nativas"""
    falas = [m["content"] for m in historico if m["role"] == "user"]
    palavras = [len(tokenizar(f)) for f in falas]
    sentimentos = estado["sentimentos"]
    print(f"   💬 Você mandou {len(falas)} mensagens")
    if palavras:
        print(f"   📏 Média de {sum(palavras) / len(palavras):.1f} palavras por mensagem (maior: {max(palavras)})")
    # 🧩 DICIONÁRIO como contador
    contagem = {"positivo": 0, "neutro": 0, "negativo": 0}
    for s in sentimentos:
        contagem[s] = contagem[s] + 1
    print(f"   🌡️ Clima: 😀 {contagem['positivo']} · 😐 {contagem['neutro']} · 😟 {contagem['negativo']}")


def cmd_temperatura(argumentos, estado, historico):
    """/temperatura 0.1 → muda a criatividade"""
    if len(argumentos) == 0:
        print(f"   Temperatura atual: {estado['temperatura']}")
        return
    try:
        nova = float(argumentos[0].replace(",", "."))
    except ValueError:
        print("   Use um número entre 0 e 1. Ex.: /temperatura 0.2")
        return
    # 🧩 OPERADORES LÓGICOS — o valor precisa estar entre 0 E 1
    if nova >= 0 and nova <= 1:
        estado["temperatura"] = nova
        print(f"   🌡️ Temperatura agora é {nova}. {'Modo robô certinho 🤖' if nova < 0.3 else 'Modo criativo 🎨'}")
    else:
        print("   A temperatura precisa estar entre 0 e 1.")


def cmd_cerebro(argumentos, estado, historico):
    """🧩 NOT — inverte um bool: liga ↔ desliga"""
    estado["debug"] = not estado["debug"]
    print(f"   🧠 Modo cérebro {'LIGADO' if estado['debug'] else 'DESLIGADO'}")


def cmd_dado(argumentos, estado, historico):
    """/dado → sorteia um número de 1 a 6 (random + int)"""
    print(f"   🎲 Deu {random.randint(1, 6)}!")


# 🧩 DICIONÁRIO DE FUNÇÕES — o "menu de ferramentas" do agente.
#    Os valores são as próprias funções (sem parênteses = não chama, só guarda).
COMANDOS = {
    "/ajuda":       {"funcao": cmd_ajuda,       "descricao": "mostra esta lista"},
    "/media":       {"funcao": cmd_media,       "descricao": "calcula média: /media 7 8.5 9"},
    "/tabuada":     {"funcao": cmd_tabuada,     "descricao": "tabuada de um número: /tabuada 7"},
    "/historico":   {"funcao": cmd_historico,   "descricao": "mostra a conversa até agora"},
    "/resumo":      {"funcao": cmd_resumo,      "descricao": "estatísticas da conversa"},
    "/temperatura": {"funcao": cmd_temperatura, "descricao": "muda a criatividade: /temperatura 0.1"},
    "/cerebro":     {"funcao": cmd_cerebro,     "descricao": "liga/desliga a visão do 'cérebro'"},
    "/dado":        {"funcao": cmd_dado,        "descricao": "rola um dado de 6 lados"},
}


def executar_comando(texto, estado, historico):
    partes = texto.split()           # "/media 7 8" → ["/media", "7", "8"]
    nome = partes[0].lower()         # 🧩 ÍNDICE [0]
    argumentos = partes[1:]          # 🧩 FATIAMENTO [1:]
    comando = COMANDOS.get(nome)     # 🧩 .get() → None se não existir (sem KeyError)
    if comando is None:
        print(f"   Comando '{nome}' não existe. Digite /ajuda")
    else:
        comando["funcao"](argumentos, estado, historico)


# ════════════════════════════════════════════════════════════════════
# 7. CONVERSA
# ════════════════════════════════════════════════════════════════════

def digitar(texto, velocidade=VELOCIDADE_DIGITACAO):
    """Efeito de digitação — 🧩 FOR em cada letra. (É o 'streaming' que o ChatGPT faz!)"""
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()


def gerar_resposta(texto, historico, estado):
    """Decide qual cérebro usar."""
    tokens = tokenizar(texto)
    estado["sentimentos"].append(analisar_sentimento(tokens)["rotulo"])

    if tem_conteudo_bloqueado(tokens):
        return "🔒 Opa! Não compartilhe dados sensíveis (senha, cartão, CPF) com uma IA."

    if estado["usar_llm"]:
        resposta = responder_com_llm(historico, estado)
        if resposta is not None:
            return resposta
        estado["usar_llm"] = False   # deu erro? desliga o LLM e segue offline
    return responder_offline(texto, estado)


def apresentar(estado):
    cerebro = "✨ LLM conectado" if estado["usar_llm"] else "🧠 cérebro offline"
    print()
    print("═" * 50)
    print(f"   🤖  {NOME_BOT} v{VERSAO} — o assistente da turma")
    print("═" * 50)
    print(f"   Modo: {cerebro} · temperatura {estado['temperatura']}")
    print("   Digite /ajuda para ver comandos ou 'sair' para encerrar.\n")


def processar_mensagem(texto, historico, estado):
    """Processa UMA mensagem. Devolve False quando é hora de encerrar."""
    texto = texto.strip()

    # 🧩 IN em lista — várias formas de dizer tchau
    if limpar_texto(texto).strip() in ["sair", "tchau", "exit", "quit", "fui"]:
        digitar(f"{NOME_BOT}: Até mais! Foram {len(historico) // 2} trocas de mensagem. Bons códigos! 👋")
        return False

    if texto.startswith("/"):
        executar_comando(texto, estado, historico)
        return True

    # 🧩 LISTA DE DICIONÁRIOS — exatamente o formato das APIs de LLM
    historico.append({"role": "user", "content": texto})
    resposta = gerar_resposta(texto, historico, estado)
    historico.append({"role": "assistant", "content": resposta})

    digitar(f"{NOME_BOT}: {resposta}")
    return True


def conversar():
    """🧩 WHILE TRUE + BREAK + CONTINUE — o 'loop de conversa' de todo chatbot."""
    carregar_env()
    estado = {
        "temperatura": TEMPERATURA,
        "debug": MODO_DEBUG,
        "usar_llm": llm_disponivel(),
        "sentimentos": [],
    }
    historico = []
    apresentar(estado)

    while True:
        try:
            texto = input("Você: ")
        except (EOFError, KeyboardInterrupt):   # Ctrl+C / Ctrl+D também encerram
            print()
            break
        if texto.strip() == "":
            continue                             # mensagem vazia? ignora e pergunta de novo
        continuar = processar_mensagem(texto, historico, estado)
        if not continuar:
            break


def demo():
    """Modo apresentação: o Byte conversa sozinho com mensagens prontas."""
    random.seed(42)   # sempre os mesmos sorteios → demo previsível
    estado = {"temperatura": TEMPERATURA, "debug": False, "usar_llm": False, "sentimentos": []}
    historico = []
    apresentar(estado)

    roteiro = [
        "Oi Byte!",
        "o que é um LLM?",
        "/cerebro",
        "tô achando python muito difícil, dá vontade de desistir",
        "me conta uma piada",
        "/cerebro",
        "/media 7 8,5 9.5",
        "minha senha é 123456",
        "valeu, você é top!",
        "/resumo",
        "sair",
    ]
    for mensagem in roteiro:
        print("Você: ", end="")
        digitar(mensagem, velocidade=0.03)
        time.sleep(0.4)
        if not processar_mensagem(mensagem, historico, estado):
            break
        print()
        time.sleep(0.6)


# 🧩 CONDICIONAL de entrada — só roda se o arquivo for executado diretamente
#    (se alguém fizer "import byte", nada roda sozinho)
if __name__ == "__main__":
    if "--demo" in sys.argv:
        demo()
    else:
        conversar()
