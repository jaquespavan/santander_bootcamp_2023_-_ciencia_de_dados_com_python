import json
from flask import Flask, jsonify, render_template

app = Flask(__name__)

'''
http://127.0.0.1:5000/loterias/megasena
http://127.0.0.1:5000/loterias/lotofacil
http://127.0.0.1:5000/loterias/diadesorte
http://127.0.0.1:5000/loterias/quina
http://127.0.0.1:5000/loterias/maismilionaria

API de resultados de loterias
Criada para fins didáticos, para o "Santander Bootcamp 2023".
Limitada a poucos concursos e resultados.

'''

def links():
    return '<a href="http://127.0.0.1:5000/loterias/megasena">Megasena</a><br>' \
           '<a href="http://127.0.0.1:5000/loterias/lotofacil">Lotofácil</a><br>' \
           '<a href="http://127.0.0.1:5000/loterias/diadesorte">Dia de Sorte</a><br>' \
           '<a href="http://127.0.0.1:5000/loterias/quina">Quina</a><br>' \
           '<a href="http://127.0.0.1:5000/loterias/maismilionaria">+ Milionária</a>'

@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/loterias')
def loteria():
    return links()


@app.route('/loterias/megasena')
def megasena():
    import pandas as pd

    df = pd.read_csv('APIs/arquivos_CSV/MEGASENA_resultados_CSV.csv', sep=';')

    lista_dics = []

    for linha in df.index:

        dic_res = {}

        concurso = df.loc[linha, 'Concurso']
        key, value = 'Concurso', int(concurso)
        dic_res[key] = value

        data_concurso = df.loc[linha, 'Data_concurso']
        key, value = 'Data_concurso', data_concurso
        dic_res[key] = value

        '''
        Exemplo:
        dezena_01 = df.loc[linha, 'Dezena_01']
        key, value = 'Dezena_01', int(dezena_01)
        dic_res[key] = value
        '''

        for i in range(1, 7):
            nome_coluna = 'Dezena_' + str(i).rjust(2, '0')
            dezena_var = df.loc[linha, nome_coluna]
            key, value = nome_coluna, int(dezena_var)
            dic_res[key] = value

        lista_dics.append(dic_res)

    return jsonify(lista_dics)


@app.route('/loterias/lotofacil')
def lotofacil():
    import pandas as pd

    df = pd.read_csv('APIs/arquivos_CSV/LOTOFÁCIL_resultados_CSV.csv', sep=';')

    lista_dics = []

    for linha in df.index:

        dic_res = {}

        concurso = df.loc[linha, 'Concurso']
        key, value = 'Concurso', int(concurso)
        dic_res[key] = value

        data_concurso = df.loc[linha, 'Data_concurso']
        key, value = 'Data_concurso', data_concurso
        dic_res[key] = value

        for i in range(1, 16):
            nome_coluna = 'Dezena_' + str(i).rjust(2, '0')
            dezena_var = df.loc[linha, nome_coluna]
            key, value = nome_coluna, int(dezena_var)
            dic_res[key] = value

        lista_dics.append(dic_res)

    return jsonify(lista_dics)


@app.route('/loterias/diadesorte')
def diadesorte():
    import pandas as pd

    df = pd.read_csv('APIs/arquivos_CSV/DIA_DE_SORTE_resultados_CSV.csv', sep=';')

    lista_dics = []

    for linha in df.index:

        dic_res = {}

        concurso = df.loc[linha, 'Concurso']
        key, value = 'Concurso', int(concurso)
        dic_res[key] = value

        data_concurso = df.loc[linha, 'Data_concurso']
        key, value = 'Data_concurso', data_concurso
        dic_res[key] = value

        for i in range(1, 8):
            nome_coluna = 'Dezena_' + str(i).rjust(2, '0')
            dezena_var = df.loc[linha, nome_coluna]
            key, value = nome_coluna, int(dezena_var)
            dic_res[key] = value

        mes = df.loc[linha, 'Mes']
        key, value = 'Mes', str(mes)
        dic_res[key] = value

        lista_dics.append(dic_res)

    return jsonify(lista_dics)


@app.route('/loterias/quina')
def quina():
    import pandas as pd

    df = pd.read_csv('APIs/arquivos_CSV/QUINA_resultados_CSV.csv', sep=';')

    lista_dics = []

    for linha in df.index:

        dic_res = {}

        concurso = df.loc[linha, 'Concurso']
        key, value = 'Concurso', int(concurso)
        dic_res[key] = value

        data_concurso = df.loc[linha, 'Data_concurso']
        key, value = 'Data_concurso', data_concurso
        dic_res[key] = value

        for i in range(1, 6):
            nome_coluna = 'Dezena_' + str(i).rjust(2, '0')
            dezena_var = df.loc[linha, nome_coluna]
            key, value = nome_coluna, int(dezena_var)
            dic_res[key] = value

        lista_dics.append(dic_res)

    return jsonify(lista_dics)


@app.route('/loterias/maismilionaria')
def maismilionaria():
    import pandas as pd

    df = pd.read_csv('APIs/arquivos_CSV/+MILIONARIA_resultados_CSV.csv', sep=';')

    lista_dics = []

    for linha in df.index:

        dic_res = {}

        concurso = df.loc[linha, 'Concurso']
        key, value = 'Concurso', int(concurso)
        dic_res[key] = value

        data_concurso = df.loc[linha, 'Data_concurso']
        key, value = 'Data_concurso', data_concurso
        dic_res[key] = value

        for i in range(1, 7):
            nome_coluna = 'Dezena_' + str(i).rjust(2, '0')
            dezena_var = df.loc[linha, nome_coluna]
            key, value = nome_coluna, int(dezena_var)
            dic_res[key] = value

        trevo1 = df.loc[linha, 'Trevo_01']
        key, value = 'Trevo_01', int(trevo1)
        dic_res[key] = value

        trevo2 = df.loc[linha, 'Trevo_02']
        key, value = 'Trevo_02', int(trevo2)
        dic_res[key] = value

        lista_dics.append(dic_res)

    return jsonify(lista_dics)

app.run()