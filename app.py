from flask import Flask, render_template, request

app = Flask(__name__)

# FORMULÁRIO (GET)
@app.route("/form_get_curriculo")
def form_get_curriculo():
    return render_template("form_get_curriculo.html")


# RESULTADO (POST)
@app.route("/form_post_result", methods=["POST"])
def form_post_result():
    nome = request.form.get("nome")
    area = request.form.get("area")
    experiencia = request.form.get("experiencia")
    ingles = request.form.get("ingles")
    disponibilidade = request.form.get("disponibilidade")
    salario = request.form.get("salario")
    skills = request.form.getlist("skills")

    return render_template(
        "form_post_result.html",
        nome=nome,
        area=area,
        experiencia=experiencia,
        ingles=ingles,
        disponibilidade=disponibilidade,
        salario=salario,
        skills=skills
    )


if __name__ == "__main__":
    app.run(debug=True)
