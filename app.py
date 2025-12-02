from flask import Flask, request, render_template
import sympy as sp

app = Flask(__name__)


def calcular_parametros(respostas):
    """
    Converte respostas (0 a 5) em parâmetros A, k e c.
    respostas é um dicionário com:
    sono, energia, foco, familiaridade, dificuldade, stress, distracoes, motivacao
    """
    sono = respostas["sono"]
    energia = respostas["energia"]
    foco = respostas["foco"]
    familiaridade = respostas["familiaridade"]
    dificuldade = respostas["dificuldade"]
    stress = respostas["stress"]
    distracoes = respostas["distracoes"]
    motivacao = respostas["motivacao"]

    # A: retenção máxima (média de energia, foco e motivação)
    A = (energia + foco + motivacao) / 3.0  # varia aproximadamente entre 1 e 5

    # k: taxa de aprendizagem (relaciona familiaridade e motivação)
    k = (familiaridade + motivacao) / 10.0   # varia aproximadamente entre 0.2 e 1.0

    # c: coeficiente de fadiga (stress + distrações + sono ruim)
    c_raw = stress + distracoes + (6 - sono)  # sono ruim aumenta fadiga
    c = c_raw / 50.0  # escala para ficar um valor pequeno (tipo 0.05–0.3)

    return float(A), float(k), float(c)


def calcular_h_otimo(A, k, c):
    h = sp.symbols('h', positive=True)

    R = A * (1 - sp.exp(-k * h))
    F = c * h**2
    L = R - F

    L_prime = sp.diff(L, h)

    # 1) Tentar resolver simbolicamente (solve)
    try:
        solutions = sp.solve(L_prime, h)
        for sol in solutions:
            val = complex(sol)
            if val.real > 0 and abs(val.imag) < 1e-6:
                return float(val.real)
    except Exception:
        pass

    # 2) Se solve falhar, tenta nsolve com vários chutes
    for guess in [0.5, 1, 2, 3, 4, 5, 6]:
        try:
            sol = sp.nsolve(L_prime, h, guess)
            val = float(sol)
            if val > 0:
                return val
        except Exception:
            continue

    return None



@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    explicacao = None

    if request.method == 'POST':
        try:
            # Coletar respostas do formulário (0 a 5)
            respostas = {
                "sono": float(request.form['sono']),
                "energia": float(request.form['energia']),
                "foco": float(request.form['foco']),
                "familiaridade": float(request.form['familiaridade']),
                "dificuldade": float(request.form['dificuldade']),
                "stress": float(request.form['stress']),
                "distracoes": float(request.form['distracoes']),
                "motivacao": float(request.form['motivacao']),
            }

            A, k, c = calcular_parametros(respostas)
            h_star = calcular_h_otimo(A, k, c)

            if h_star is not None:
                result = round(h_star, 2)

                explicacao = (
                    f"Com base nas suas respostas, o sistema estimou um equilíbrio entre "
                    f"retenção de conteúdo (modelo de aprendizado) e fadiga cognitiva. "
                    f"Estudar cerca de {result} horas por dia tende a maximizar o aprendizado "
                    f"antes que o cansaço comece a prejudicar o rendimento."
                )
            else:
                result = "Não foi possível calcular um tempo ótimo com os dados informados."
                explicacao = (
                    "Tente ajustar suas respostas ou revisar os dados inseridos. "
                    "Em condições muito extremas, o modelo pode não encontrar um ponto ótimo claro."
                )

        except Exception:
            result = "Erro ao processar os dados."
            explicacao = "Verifique se todos os campos foram preenchidos corretamente."

    return render_template('index.html', result=result, explicacao=explicacao)


if __name__ == '__main__':
    app.run(debug=True)
