import csv

def separar_data_e_horas(arquivo_entrada, arquivo_saida, coluna_data_hora):
    with open(arquivo_entrada, 'r', encoding='utf-8') as arquivo_csv, open(arquivo_saida, 'w', newline='', encoding='utf-8') as arquivo_saida_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        cabecalho = leitor_csv.fieldnames + ['Data', 'Hora']
        escritor_csv = csv.DictWriter(arquivo_saida_csv, fieldnames=cabecalho)
        escritor_csv.writeheader()

        for linha in leitor_csv:
            data_hora = linha[cabecalho[coluna_data_hora - 1]].strip() if coluna_data_hora <= len(cabecalho) else ''
            if data_hora:
                data, hora = data_hora.split()
            else:
                data, hora = '', ''
            linha['Data'] = data
            linha['Hora'] = hora
            escritor_csv.writerow(linha)

# Exemplo de uso
arquivo_entrada = 'Trabalhador CRAB Comentários + IBM - Comentários + IBM CRAB.csv'
arquivo_saida = 'dados_separados2.csv'
coluna_data_hora = 2  # Assumindo que a data e hora estão na terceira coluna
separar_data_e_horas(arquivo_entrada, arquivo_saida, coluna_data_hora)
