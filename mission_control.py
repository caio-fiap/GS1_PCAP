NOME_MISSAO = "Projeto Aurora"
NOME_EQUIPE = "Equipe Netuno"

# Matriz principal: linha = ciclo; coluna = parametro
# Ordem: [temperatura (ºC), comunicacao (%), bateria (%), oxigenio (%), estabilidade (%)]

dados_missao = [
    [24, 92, 88, 96, 90],
    [27, 80, 72, 94, 85],
    [31, 65, 58, 91, 70],
    [36, 42, 38, 87, 55],
    [39, 28, 19, 78, 35],
    [34, 55, 32, 82, 50]
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicacao com a base",
    "Sistema de energia",
    "Suporte de oxigenio",
    "Estabilidade operacional"
]

RECOMENDACOES = {
    "temperatura": "Verificar controle térmico da missão",
    "comunicacao": "Tentar restabelecer contato com a base",
    "bateria": "Ativar modo de economia de energia",
    "oxigenio": "Acionar protocolo de suporte a vida",
    "estabilidade": "Redzir operacoes nao essenciais"
}

# funcoes de analise

def analisar_temperatura(valor):
    """Classifica a temperatura interna no modilo (ºC)."""
    if valor > 35:
        return "CRITICO", 2
    elif valor > 30 or valor < 18:
        return "ATENCAO", 1
    else:
        return "NORMAL", 0

def analisar_comunicacao(valor):
    """Classifica a qualidade do sinal de comunicacao (%)"""
    if valor < 30:
        return "CRITICO", 2
    elif valor < 60:
        return "ATENCAO", 1
    else:
        return "NORMAL", 0

def analisar_bateria(valor):
    """Classifica o nivel de bateria (%)"""
    if valor < 20:
        return "CRITICO", 2
    elif valor < 50:
        return "ATENCAO", 1
    else:
        return "NORMAL", 0

def analisar_oxigenio(valor):
    """Classifica o nivel de oxigenio (%)"""
    if valor < 80:
        return "CRITICO", 2
    elif valor < 90:
        return "ATENCAO", 1
    else:
        return "NORMAL", 0

def analisar_estabilidade(valor):
    """Classifica o estabilidade do sistema(%)"""
    if valor < 40:
        return "CRITICO", 2
    elif valor < 70:
        return "ATENCAO", 1
    else:
        return "NORMAL", 0

def classificar_ciclo(pontuacao_total):
    """Retorna o status do ciclo com base na pontuacao de risco"""
    if pontuacao_total <= 2:
        return "MISSAO ESTAVEL"
    elif pontuacao_total <= 5:
        return "MISSAO EM ATENCAO"
    else:
        return "MISSAO CRITICA"

def analisar_tendencia(risco_primeiro, risco_ultimo):
    """Compara o risco do primeiro e do ultimo ciclo para indicar tendencia"""
    if risco_ultimo > risco_primeiro:
        return "A missao apresentou tendencia de PIORA"
    elif risco_primeiro > risco_ultimo:
        return "A missao apresentou tendencia de MELHORA"
    else:
        return "A missao permaneceu ESTAVEL"

def area_mais_afetada(pontuacao_por_area):
    """Retorna a área com maior risco."""
    max_pontos = max(pontuacao_por_area)
    indice = pontuacao_por_area.index(max_pontos)
    return areas_monitoradas[indice], max_pontos

def gerar_recomendacao(alertas_ciclo):
    """Recebe um dicionario e retorna lista de recomendacao"""
    recomendacoes = []
    mapa = {
        "temperatura": "temperatura",
        "comunicacao": "comunicacao",
        "bateria": "bateria",
        "oxigenio": "oxigenio",
        "estabilidade": "estabilidade",
    }
    for chave, status in alertas_ciclo.items():
        if status == "CRITICO":
            recomendacoes.append(f" ^ {RECOMENDACOES[mapa[chave]]}")
    return recomendacoes

# funcao principal - relatorio final
def gerar_relatorio_final(dados, areas):
    """Percorre todos os ciclos e exibe o relatorio final"""
    separador = "=" * 62
    linha = "-" * 62

    print(separador)
    print(f" MISSION CONTROL AI | {NOME_MISSAO}")
    print(f" Equipe: {NOME_EQUIPE}")
    print(separador)

    riscos_por_ciclo = []
    pontuacao_por_area = [0] * 5        # acumulador por coluna

    for numero_ciclo, ciclo in enumerate(dados, start=1):
        temperatura, comunicacao, bateria, oxigenio, estabilidade = ciclo

        #analisar cada parametro
        status_temp, pts_temp = analisar_temperatura(temperatura)
        status_com, pts_com = analisar_comunicacao(comunicacao)
        status_bat, pts_bat = analisar_bateria(bateria)
        status_oxi, pts_oxi = analisar_oxigenio(oxigenio)
        status_est, pts_est = analisar_estabilidade(estabilidade)

        pontos_ciclo = pts_temp + pts_com + pts_bat + pts_oxi + pts_est
        riscos_por_ciclo.append(pontos_ciclo)

        #acumular pontos por area
        pontuacao_por_area[0] += pts_temp
        pontuacao_por_area[1] += pts_com
        pontuacao_por_area[2] += pts_bat
        pontuacao_por_area[3] += pts_oxi
        pontuacao_por_area[4] += pts_est

        classificacao = classificar_ciclo(pontos_ciclo)

        #exibir cabecalho
        print(f"\n CICLO {numero_ciclo}")
        print(linha)
        print(f" {'Parametro':<30} {'valor':>8} {'Status'}")
        print(linha)
        print(f" {'Temperatura interna':<30} {temperatura:>6}ºC {status_temp}")
        print(f" {'Comunicacao com a base':<30} {comunicacao:>7}% {status_com}")
        print(f" {'Sistema de energia':<30} {bateria:>7}% {status_bat}")
        print(f" {'Suporte de oxigenio':<30} {oxigenio:>7}% {status_oxi}")
        print(f" {'Estabilidade operacional':<30} {estabilidade:>7}% {status_est}")
        print(linha)
        print(f" Pontuacao de risco: {pontos_ciclo}/10   ->   {classificacao}")

        #recomendacoes do ciclo
        alertas = {
            "temperatura": status_temp,
            "comunicacao": status_com,
            "bateria": status_bat,
            "oxigenio": status_oxi,
            "estabilidade": status_est,
        }
        recomendacoes = gerar_recomendacao(alertas)
        if recomendacoes:
            print(" Recomendacoes:")
            for rec in recomendacoes:
                print(rec)

    #Resumo geral
    print(f"\n{separador}")
    print(" RESUMO GERAL DA MISSAO")
    print(separador)

    #tendencia
    tendencia = analisar_tendencia(riscos_por_ciclo[0], riscos_por_ciclo[-1])
    print(f" \n Tendencia da missao:")
    print(f" {tendencia}")

    #area mais afetada
    area_critica, total_area = area_mais_afetada(pontuacao_por_area)
    print(f"\n Area mais afetada: {area_critica} ({total_area} pontos acumulados)")

    #pontos acumulados por area
    print(f"\n Pontuacao acumulada por area:")
    for i, r in enumerate(riscos_por_ciclo, start=1):
        barra = "\u25A0" * r
        print(f" Ciclo {i}: {r:>2}/10  {barra}")

    print(f"\n {separador}")
    print(" Relatorio concluido!")
    print(separador)

#execucao

if __name__ == "__main__":
    gerar_relatorio_final(dados_missao, areas_monitoradas)