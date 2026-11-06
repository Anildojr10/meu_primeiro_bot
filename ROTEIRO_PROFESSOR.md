# 🎓 Roteiro do professor: Python para IA, do zero ao seu primeiro assistente

**Junta as aulas originais:** Aula 1 (Variáveis · Tipos · Condicionais · Funções) + Aula 2 (Listas · Loops · Dicionários · Git)
**Formato:** o projeto pronto vem **primeiro** e depois a aula desmonta ele, peça por peça
**Duração recomendada:** 2 encontros de 4h. Se só tiver 4h, veja a versão compacta no fim.

**Arquivos:**
- 📦 Para os alunos: `entrega-alunos/byte-assistente-ia.zip` (notebook com exercícios em branco + testes ✅/❌)
- 🔑 Só seu: `Aula_Python_para_IA_Byte_GABARITO.ipynb` (mesma aula, com todas as soluções)

---

## 🧠 A ideia central
A aula **começa com a IA funcionando**. Cada fundamento aparece como resposta a uma pergunta: *"como o Byte faz isso?"*. A frase que guia tudo, para repetir no começo, no meio e no fim:

> **"O LLM é a parte inteligente, mas tudo em volta dele é Python básico."**

## 🔁 O ciclo de cada bloco (sempre igual)
A turma se acostuma com o ritmo e para de se perder:

1. **Pergunta-gancho** (1 min): *"como uma IA toma decisões?"*
2. **Conceito curto** (5 a 10 min): analogia + 1 célula simples
3. **"No Byte"** (5 min): a mesma ideia rodando dentro do `byte.py`
4. **🔮 Previsão** quando houver: todos escrevem o palpite **antes** de você rodar
5. **🎯 Sua vez** (5 a 15 min): você circula pela sala; quem termina ajuda o vizinho
6. **Fechamento** (2 min): mostre a solução do gabarito no projetor e diga uma frase de ponte com a IA real

**Termômetro da turma:** a cada "Sua vez", peça ✅ no chat (ou um polegar para cima) quando der tudo verde no corretor. Se menos da metade conseguir, faça a solução junto com a turma antes de seguir.

---

## ✅ Preparação

**Uma semana antes**
- [ ] Envie o zip e peça para os alunos fazerem o checklist "Antes da aula" do README (Python, VS Code, Git, **conta no GitHub**, mostrar extensões de arquivo)
- [ ] Crie uma chave de API **sua** no Groq (plano gratuito), para a abertura do encontro 1. Os alunos criam as deles em casa, depois do encontro 1 (passo a passo no README do aluno)

**Na véspera**
- [ ] Rode o notebook do aluno do início ao fim: nenhuma célula pode dar erro (os ❌ dos exercícios são esperados)
- [ ] Rode o gabarito: tudo tem que dar ✅
- [ ] Deixe o `.env` pronto na **sua** pasta e teste `python byte.py` com **✨ LLM conectado**

**30 minutos antes**
- [ ] Projetor com o terminal do VS Code ou o Windows Terminal, para os emojis aparecerem
- [ ] Fonte grande (Ctrl + `+` no VS Code)
- [ ] Gabarito aberto numa segunda janela, **fora do projetor**
- [ ] ⚠️ **Nunca mostre o conteúdo do `.env` no projetor.** Sua chave vale como um cartão de crédito

---

# 📅 ENCONTRO 1: "O Byte ganha uma personalidade"
*Blocos 0 a 4 · objetivo: o aluno sai com o próprio bot rodando e a primeira mudança no `byte.py`*

| Tempo | Bloco | Resumo |
|---|---|---|
| 0:00–0:10 | 🎬 Abertura de impacto | LLM ligado × desligado |
| 0:10–0:20 | 🎬 Conheça o Byte | demo, votação, caça ao 🧩 |
| 0:20–0:35 | ⚙️ Setup + corretor | todo mundo com ✅ |
| 0:35–1:10 | 📦 Variáveis e tipos | 4 tipos, f-string, conversão, ficha do bot |
| 1:10–1:50 | 🔀 Condicionais | sentimento, operadores, guardrail, porteiro |
| 1:50–2:05 | ☕ Intervalo | |
| 2:05–2:50 | 🧰 Funções | temperatura, composição, tools, classificador |
| 2:50–3:30 | 📚 Listas | tokens, janela de contexto, avaliações |
| 3:30–3:50 | 🟢 Primeiro desafio | nova intenção no `byte.py` |
| 3:50–4:00 | 🏁 Fechamento | tarefa de casa |

### 0:00–0:10 · 🎬 Abertura de impacto (não pule!)
1. **Antes de dizer qualquer coisa**, rode `python byte.py` na sua pasta (com o `.env`). O banner mostra **✨ LLM conectado**.
2. Digite: *"qual a capital da França?"*. Ele acerta.
3. Digite: *"me explica o que é uma variável em Python, com uma analogia de futebol"*. Ele responde bem.
4. Digite `sair`. **Renomeie o `.env` para `.env.off`** e rode de novo: agora o banner mostra **🧠 cérebro offline**.
5. Repita *"qual a capital da França?"*. Ele não sabe.

> 🎤 *"Esse aqui tem um cérebro de verdade, um LLM. E esse aqui é o mesmo programa, com um cérebro que eu escrevi à mão. Hoje vocês vão aprender a construir **tudo em volta** do cérebro. E no fim do curso, vão ligar o de vocês."*

⚠️ Volte o nome para `.env` depois. Você vai precisar dele no encontro 2.

### 0:10–0:20 · 🎬 Conheça o Byte
1. Peça para abrirem o notebook e rodarem a primeira célula (`byte.demo()`). Você roda junto no projetor.
2. **Votação:** cada um anota **no papel** quantas linhas acha que o Byte tem e quanto acha que vai entender até o fim. Escreva alguns palpites no quadro. *Só depois* deixe abrirem o "👀 Clique só depois de votar".
3. **Caça ao 🧩:** *"Abram o `byte.py` e deem Ctrl+F no 🧩. Cada um é algo que vocês vão aprender. Quantos acharam?"*

### 0:20–0:35 · ⚙️ Setup + corretor
1. `python --version` (ou `py --version` no Windows)
2. Rodar a célula "Olá, mundo"
3. **Rodar a célula do corretor:** precisa aparecer `✅ o corretor está funcionando`
> 🎤 *"Daqui pra frente, vários exercícios têm um corretor automático. ❌ não é bronca: é o Python dizendo o que ele esperava. Igual a um teste de verdade numa empresa."*

🐞 **Se travar:** quem não tem Python instalado faz em dupla com o vizinho e instala no intervalo. **Não pare a aula por isso.**

### 0:35–1:10 · 📦 Variáveis e tipos: *as configurações de uma IA*
| Passo | Célula | O que dizer ou fazer |
|---|---|---|
| Gancho | markdown inicial | 🎤 *"Quando uma empresa chama o ChatGPT, ela manda exatamente 4 tipos de informação. Vocês vão aprender esses 4 nos próximos 10 minutos."* |
| Os 4 tipos | `modelo = "gpt-4o-mini"...` | Mostre a tabela str/int/float/bool. Erro clássico: `true` minúsculo |
| No Byte | `print(byte.NOME_BOT, type(...))` | Peça para abrirem o bloco 1 do `byte.py` e acharem as mesmas variáveis |
| Nomes | tabela de regras | Rápido, 2 min. Pergunte: *"`2026ano` pode?"* |
| F-string | `prompt = f"Explique {assunto}..."` | 🎤 *"Isso é engenharia de prompt de verdade: um molde fixo e dados que mudam."* Mostre o `PROMPT_SISTEMA` |
| Conversão | `digitado = "8.5"` | Descomente o `print(digitado + 1)` **ao vivo**, deixe dar o TypeError e leia o erro com a turma |
| No Byte | `byte.cmd_media(["7", "8,5", "9"]...)` | *"Brasileiro digita vírgula. O Byte troca por ponto."* |
| 🎯 Sua vez | **ficha do bot** (5 a 8 min) | Peça para 2 ou 3 alunos lerem o prompt do bot em voz alta. **Diga que esse bot volta no fim** |

### 1:10–1:50 · 🔀 Condicionais: *como uma IA toma decisões*
| Passo | Célula | O que dizer ou fazer |
|---|---|---|
| Gancho | markdown | Analogia do guarda-chuva. Mostre a sintaxe: `:` e 4 espaços |
| Simples | `pontuacao = 2` | Peça para trocarem por -3 e 0 e rodarem de novo |
| No Byte | `frases = [...]` sentimento | 🎤 **Pergunta:** *"Como ele sabe que 'não gostei' é negativo, se 'gostei' é positivo?"* Deixe procurarem `"nao" in tokens` no `byte.py` (2 min) |
| F-string | 🔍 **Decifrando a f-string** | 3 min, só para reconhecer. *"Não precisa decorar."* |
| Operadores | tabela de comparação | Destaque: `=` guarda, `==` compara |
| and/or/not | 2 células | Ligue cada um ao Byte: temperatura entre 0 e 1, LLM ou Ollama, `/cerebro` |
| Guardrail | `byte.gerar_resposta("minha senha é 123456"...)` | 🎤 *"Empresas colocam `if` na frente do modelo. Isso se chama guardrail."* |
| 🎯 Sua vez | **porteiro** (10 min) | Depois do tempo, pergunte: *"quem testou 'Qual é a minha SENHA?' com maiúscula? Passou?"* É a pegadinha: a solução usa `.lower()` |

### 1:50–2:05 · ☕ Intervalo
Ajude quem ficou para trás no setup.

### 2:05–2:50 · 🧰 Funções: *as habilidades da IA*
| Passo | Célula | O que dizer ou fazer |
|---|---|---|
| Gancho | analogia da receita | Nome, ingredientes = parâmetros, bolo = `return` |
| Valor padrão | `saudar(...)` | |
| 🔮 Temperatura | `escolher_resposta(..., 0.0)` | **Previsão:** *"iguais ou diferentes?"* Depois: 🎤 *"Isso é o slider de temperatura do ChatGPT. Lá o sorteio é entre palavras."* |
| Composição | árvore do `responder_offline` | 🎤 *"A função principal não sabe fazer nada sozinha: ela só chama quem sabe."* |
| Tools | `byte.COMANDOS.items()` + `/tabuada` | 🎤 *"Um agente de IA recebe uma lista de funções e decide qual chamar. Isso aqui é a versão manual."* |
| 🔮 `None` | `somar_errado` | **Previsão** antes de rodar. Quase todo mundo erra, e é bom que erre |
| 🎯 Sua vez | **classificador em dupla** (15 min) | O corretor mostra ✅/❌ por caso. *"Roteamento de intenção: o primeiro passo de todo chatbot de atendimento."* |

### 2:50–3:30 · 📚 Listas: *como uma IA lê uma frase*
| Passo | Célula | O que dizer ou fazer |
|---|---|---|
| Tokens | `byte.tokenizar(...)` | 🎤 *"Quando dizem que um modelo aceita 128 mil tokens, é o tamanho máximo de uma lista."* |
| Tokenizador real | link no markdown | Abra o tokenizador da OpenAI **no projetor** e cole a mesma frase. Compare o número de tokens |
| 🔮 Fatiamento | `tokens[0]`, `[-1]`, `[1:3]`... | Todos escrevem no papel antes. Descomente o `tokens[50]` e mostre o IndexError |
| Janela | `historico_gigante[-5:]` | 🎤 *"Sabe quando o ChatGPT esquece o começo de uma conversa longa? É um `[-N:]`."* |
| Métodos | `append`, `remove`, `sort` | Rápido |
| List comprehension | tradicional × comprehension | Leia de dentro para fora em voz alta |
| 🎯 Sua vez | **avaliações** (10 min) | 🎤 *"Isso é o que um time de dados faz antes de treinar um modelo: entender os dados."* |

### 3:30–3:50 · 🟢 Primeiro desafio no `byte.py`
Desafio 1 (nova intenção `"comida"`): copiar o padrão de uma intenção que já existe e mudar.
1. Mostre no projetor onde fica o `INTENCOES` e copie a intenção `"elogio"` como modelo.
2. Alunos fazem, salvam e testam no terminal: `python byte.py` → *"tô com fome"*
3. 🎤 *"Vocês acabaram de ensinar algo novo a uma IA. Do jeito antigo: escrevendo a regra."*

### 3:50–4:00 · 🏁 Fechamento do encontro 1
- Volte à frase-guia: *"O LLM é a parte inteligente..."*
- **Tarefa de casa:**
  1. Desafio 3 (*transforme o Byte no seu bot*, usando a ficha do bloco 1). No próximo encontro, alguns vão mostrar.
  2. **Criar a chave do Groq** seguindo o README (seção "✨ Ligando um LLM de verdade"). Peça para **ainda não colocarem a chave no `.env`**: isso vai ser feito juntos, depois da aula de Git.
- Peça uma palavra no chat: *"como foi a aula de hoje?"*

---

# 📅 ENCONTRO 2: "O Byte conversa, lembra e se conecta"
*Blocos 5 a 8 + desafios · objetivo: o aluno sai com o Byte turbinado no GitHub*

| Tempo | Bloco | Resumo |
|---|---|---|
| 0:00–0:15 | 🎭 Vitrine dos bots | 2 a 3 alunos mostram o desafio 3 |
| 0:15–0:55 | 🔁 Loops | streaming, loop de conversa, detector |
| 0:55–1:45 | 🗂️ Dicionários | JSON da API, Quebre o Byte, ética, relatório |
| 1:45–2:00 | ☕ Intervalo | |
| 2:00–2:30 | 🔐 Git + GitHub + .env | primeiro push, com calma |
| 2:30–2:45 | ✨ LLM + o vazamento | cada aluno liga a própria chave + gancho do desafio 🕵️ |
| 2:45–3:40 | 🏁 Turbine o Byte | mão na massa, um commit por desafio |
| 3:40–3:55 | 🎭 Vitrine final | 3 alunos, 1 min cada + palpites |
| 3:55–4:00 | 🎟️ Bilhete de saída | |

### 0:00–0:15 · 🎭 Vitrine dos bots
Dois ou três alunos rodam o bot deles no projetor (desafio 3). Peça para a turma mandar uma mensagem para cada bot. Ligue o `/cerebro` em um deles e pergunte: *"o que vocês lembram do que aparece aqui?"*. É a revisão do encontro 1 sem parecer revisão.

### 0:15–0:55 · 🔁 Loops: *como uma IA conversa sem parar*
| Passo | Célula | O que dizer ou fazer |
|---|---|---|
| for | `for palavra in [...]` | |
| Streaming | `byte.digitar(...)` | 🎤 *"Esse efeito de letra por letra tem nome: streaming. O ChatGPT faz isso."* |
| range/enumerate | tabuada + modelos | |
| while | esqueleto do chatbot | 🎤 *"Todo chatbot do mundo tem esse esqueleto."* Peça para acharem a `conversar()` no `byte.py` |
| break/continue | lista simulada | Explique por que é simulado: `input()` não funciona bem no notebook |
| Ternário | ✨ **if em uma linha** | 2 min. Ele aparece no exercício seguinte |
| 🎯 Sua vez | **detector de palavrões** (10 min) | O teste "Professor IDIOTA!" mostra por que vale usar `byte.tokenizar` em vez de `.split()` |

### 0:55–1:45 · 🗂️ Dicionários: *como uma IA lembra da conversa*
| Passo | Célula | O que dizer ou fazer |
|---|---|---|
| Conceito | `aluno = {...}` | Ficha de cadastro. Mostre o KeyError e depois o `.get()` |
| Lista de dicts | `historico = [...]` | 🎤 *"Uma conversa com o ChatGPT é literalmente isso."* |
| ⭐ **Momento "uau"** | `json.dumps(pedido)` | Pause. 🎤 *"Isso aqui é exatamente o que sai do seu computador quando você usa uma IA. Olhem: str, float, int, lista, dicionário. Tudo o que vimos, num objeto só."* Peça para apontarem cada tipo |
| Base | `INTENCOES.items()` | |
| Tupla | 💡 nota sobre `intencao, confianca =` | 1 min |
| Intenção | `detectar_intencao` (4 frases) | Mostre que *"tô travado nesse for"* empata: ganha quem vem primeiro no dicionário |
| 🔮 **Quebre o Byte** | 4 frases que dão errado | **Previsão primeiro.** Depois leia o "Por que errou?" com a turma. 🎤 *"Cada erro pede mais uma regra, e cada regra cria outro erro."* |
| ⚖️ Ética | box no fim | 1 min. Pergunte: *"quem decidiu que 'chato' é negativo?"* Deixe 1 ou 2 responderem |
| Capital da França | markdown "Isso é IA?" | 🎤 *"Ninguém escreveu essa regra. É por isso que os LLMs mudaram o jogo."* |
| 🎯 Sua vez | **relatório da conversa em dupla** (15 min) | Pegadinha: a maior mensagem é a do `system`, não a do usuário |

### 1:45–2:00 · ☕ Intervalo
Confira quem **ainda não tem conta no GitHub** e peça para criarem agora.

### 2:00–2:30 · 🔐 Git, GitHub e .env (com calma: é onde mais trava)
1. Mostre a tabela "vai pro GitHub?" e rode a célula do `.gitignore`.
2. 🎤 *"Robôs varrem o GitHub 24 horas por dia atrás de chaves esquecidas. Uma chave vazada pode virar uma conta de milhares de reais."*
3. `git config --global user.name / user.email` (todos juntos)
4. **Caminho recomendado: VS Code → Source Control (Ctrl+Shift+G)** → Initialize Repository → mensagem → Commit → **Publish Branch** (o VS Code faz o login no GitHub pelo navegador)
5. **Checagem obrigatória:** no GitHub, o `.env` **não** pode aparecer na lista de arquivos. Peça para 2 vizinhos conferirem um ao outro.

🐞 **Se travar:** quem não conseguir publicar faz só o commit local e publica em casa. **Não segure a turma inteira.**

### 2:30–2:45 · ✨ Plugar o LLM + o vazamento (o gancho mais forte da aula)
1. No **seu** computador: `python byte.py` → **✨ LLM conectado**. Ligue `/cerebro` e mande uma mensagem.
   🎤 *"Olhem o pacote indo para o modelo: é o mesmo dicionário que vocês viram há uma hora."*
2. **Agora é a vez deles (5 min):** cada aluno cria o `.env` a partir do `.env.exemplo`, cola a **própria** chave do Groq e roda `python byte.py`. Quem esqueceu de criar a chave em casa cria agora (leva 2 min). Antes de seguir, peça para rodarem `git status`: o `.env` **não** pode aparecer.
   🎤 *"Agora o seu bot tem um cérebro de verdade. E o código não mudou uma linha."*
3. Mostre a tabela "🧠 offline × ✨ LLM" do notebook.
4. **Agora o gancho.** Digite *"minha senha é 123456"*. O Byte bloqueia. 🎤 *"Ótimo, o guardrail funcionou... certo?"*
5. Digite `/historico`. **A senha está lá.**
   🎤 *"Ela foi bloqueada na resposta, mas ficou guardada. E na próxima mensagem, o histórico inteiro vai para o LLM. **Temos um vazamento.** Quem achar e consertar é o desafio 🕵️ de hoje."*

⚠️ **Não mostre a solução.** Ela está no gabarito: revele só no próximo encontro, ou depois do prazo do entregável.

### 2:45–3:40 · 🏁 Turbine o Byte (mão na massa)
- Cada aluno escolhe **pelo menos 2 desafios**. Sugestão: um 🟢 ou 🟡 para garantir e um 🔵 ou 🕵️ para crescer.
- Regra: **um commit por desafio** (`git commit -m "desafio 4: comando /contar"`).
- Você circula. Os primeiros que terminarem viram "monitores" e ajudam a sala.
- Aos **3:20**, avise: *"faltam 20 minutos: commitem o que têm."*
- Quem fizer o 🕵️ roda a célula de teste no notebook. O ✅ ali vale comemoração pública 🎉

### 3:40–3:55 · 🎭 Vitrine final
1. Três alunos, **1 minuto cada**: o que mudaram + uma conversa ao vivo. Prefira desafios diferentes entre si.
2. **Volte aos palpites do encontro 1** que estão no quadro (ou na sua anotação): *"Abram o `byte.py` agora. Quanto vocês reconhecem?"*
3. Frase-guia pela última vez: 🎤 *"O LLM é a parte inteligente, mas tudo em volta dele, vocês já sabem fazer."*

### 3:55–4:00 · 🎟️ Bilhete de saída + entregável
- Bilhete no chat (está no fim do notebook): **uma surpresa, uma dúvida, uma nota de 0 a 10.** Leia antes da próxima aula: as dúvidas viram os primeiros 10 minutos dela.
- Entregável: link do GitHub no chat em até **1 semana** (mesmo dia da semana, até 23h59). Diga a data em voz alta e escreva no quadro. A rubrica está no fim do notebook.
- No meio da semana, mande um lembrete no chat da turma: *"Faltam 3 dias! Já fez o primeiro commit?"*

---

## ⏱️ Versão compacta (só 4h)
O original junta tudo em 4h. Dá para fazer, mas corte assim:

| Tempo | Bloco | O que cortar |
|---|---|---|
| 0:00–0:15 | Abertura de impacto + demo + votação | caça ao 🧩 vira tarefa de casa |
| 0:15–0:25 | Setup + corretor | |
| 0:25–0:50 | Variáveis | tabela de nomes; ficha do bot em 5 min |
| 0:50–1:20 | Condicionais | "Decifrando a f-string" só citado |
| 1:20–1:50 | Funções | classificador vira individual (10 min) |
| 1:50–2:00 | ☕ Intervalo | |
| 2:00–2:25 | Listas | métodos `append/sort`; avaliações vira tarefa de casa |
| 2:25–2:50 | Loops | range/enumerate rápidos |
| 2:50–3:20 | Dicionários | relatório vira tarefa de casa; **mantenha o JSON e o Quebre o Byte** |
| 3:20–3:35 | LLM + vazamento | **não corte: é o fechamento** |
| 3:35–3:50 | Git (só commit local) | o push vai para casa, com o README como guia |
| 3:50–4:00 | Palpites + bilhete de saída | os desafios viram o entregável de casa (prazo: 1 semana) |

**Nunca corte:** a abertura de impacto, o JSON do pedido, o Quebre o Byte e o vazamento. São os quatro momentos que a turma vai lembrar.

---

## 🐞 Onde a turma costuma travar
- **`python` não é reconhecido (Windows):** tente `py`. Se nenhum funcionar, a instalação não marcou "Add Python to PATH"; reinstale marcando essa opção
- **Emojis quebrados:** use o terminal do VS Code ou o Windows Terminal (o `cmd` antigo mostra quadradinhos, mas o código funciona)
- **`ModuleNotFoundError: byte` no notebook:** o notebook não foi aberto **de dentro** da pasta `byte-assistente-ia`
- **`input()` no notebook:** por isso o loop de conversa é simulado com uma lista. A conversa de verdade é no terminal
- **"Mudei o `byte.py` e o notebook não mudou":** o notebook guarda a versão antiga. Reinicie o kernel (ou use a célula de teste do 🕵️, que já faz `importlib.reload`)
- **"Meu `.env` não funciona":** o nome tem que ser exatamente `.env` (sem `.txt`), na mesma pasta do `byte.py`, com as linhas **sem** `#` na frente
- **LLM retorna erro:** o Byte avisa e volta sozinho para o cérebro offline. Confira a chave e o nome do modelo no painel do provedor
- **IndentationError depois de colar código:** o VS Code misturou tabs e espaços. Selecione tudo e use "Convert Indentation to Spaces"
- **Empates na intenção:** *"tô travado nesse for"* empata entre `motivacao` e `python` (1 palavra cada), e ganha quem vem primeiro no dicionário. É um ótimo gancho para o desafio 🔵 7

## 🔑 Quando usar o gabarito
- **Durante a aula:** depois do tempo de cada "Sua vez", mostre a célula do gabarito no projetor por 2 minutos e explique uma linha-chave
- **Não distribua o arquivo** antes do prazo do entregável
- **Desafio 🕵️:** a solução fica guardada até o encontro seguinte. É um ótimo jeito de abrir a próxima aula

## 📦 Entregável
Byte turbinado (pelo menos 2 desafios) no GitHub, com README descrevendo as mudanças e `.env` fora do repositório. A rubrica está no fim do notebook do aluno. Substitui o "Sistema de cadastro de alunos" da Aula 2 original.

> Os exercícios originais das Aulas 1 e 2 (cartão de apresentação, `verifica_elegibilidade`, `processar_turma`) continuam válidos como fixação extra ou tarefa de casa.
