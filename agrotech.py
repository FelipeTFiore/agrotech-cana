import json
import cx_Oracle


def conectar_oracle():
    """Conecta ao banco Oracle."""
    try:
        # Forma 1 - Direto com a string de conexão completa
        conn = cx_Oracle.connect(
            user="RM560763",
            password="fiap25",
            dsn="oracle.fiap.com.br:1521/ORCL"
        )

        # Forma alternativa - Se a anterior não funcionar
        # dsn = cx_Oracle.makedsn("oracle.fiap.com.br", "1521", service_name="ORCL")
        # conn = cx_Oracle.connect(user="RM560763", password="fiap25", dsn=dsn)

        print("✅ Conexão com Oracle estabelecida com sucesso!")
        return conn
    except Exception as e:
        print(f"❌ Erro ao conectar ao Oracle: {e}")
        return None


def calcular_perdas(toneladas_colhidas, toneladas_perdidas):
    """Calcula o percentual de perdas."""
    try:
        if toneladas_colhidas <= 0:
            raise ValueError("Toneladas colhidas deve ser maior que zero")
        return (toneladas_perdidas / toneladas_colhidas) * 100
    except Exception as e:
        print(f"❌ Erro no cálculo de perdas: {e}")
        return None

def salvar_json(dados, arquivo="colheitas.json"):
    """Salva dados em JSON."""
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)

def carregar_json(arquivo="colheitas.json"):
    """Carrega dados do JSON."""
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def menu_principal():
    """Exibe o menu interativo."""
    print("\n--- SISTEMA DE MONITORAMENTO DE PERDAS ---")
    print("1. Registrar nova colheita")
    print("2. Visualizar relatório")
    print("3. Sair")
    return input("Escolha uma opção: ")

# Exemplo de uso
if __name__ == "__main__":
    historico = carregar_json()
    conexao_oracle = conectar_oracle()

    while True:
        opcao = menu_principal()
        if opcao == "1":
            # Lógica para registrar colheita (usando dicionários)
            colheita = {
                "data": input("Data (DD/MM/AAAA): "),
                "area_hectares": float(input("Área (ha): ")),
                "toneladas_colhidas": float(input("Toneladas colhidas: ")),
                "toneladas_perdidas": float(input("Toneladas perdidas: "))
            }
            colheita["percentual_perdas"] = calcular_perdas(
                colheita["toneladas_colhidas"],
                colheita["toneladas_perdidas"]
            )
            historico.append(colheita)
            salvar_json(historico)
            print("Dados salvos!")

        elif opcao == "2":
            # Gerar relatório (usando listas/dicionários)
            print("\n--- RELATÓRIO ---")
            for registro in historico:
                print(f"Data: {registro['data']} | Perdas: {registro['percentual_perdas']:.2f}%")

        elif opcao == "3":
            break