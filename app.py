from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/",methods = ['GET','POST'])
def index():
    massa = None
    altura = None
    diagnostico = None
    result = None
    if request.method == 'POST':
        massa = float(request.form.get('massa','').replace(",","."))
        altura = float(request.form.get('altura','').replace(",","."))
        imc = massa/(altura**2)
        if imc < 18.5:
            diagnostico = 'Você está abaixo do peso.'
        elif imc < 25:
            diagnostico = 'Peso ideal.'
        elif imc < 30:
            diagnostico = 'Acima do peso.'
        elif imc < 35:
            diagnostico = 'Obeso'
        elif imc < 35:
            diagnostico = 'Obeso nivel II'
        else:
            diagnostico = 'Obsidade Morbida'

        result = f"Seu IMC é {imc:.2f}.{diagnostico}"
    return render_template("index.html", result=result)

    

if __name__ == "__main__":
    app.run(debug=True)


    