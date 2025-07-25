from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    option = request.form['option']

    if option == 'sgpa_per':
        sgpa = float(request.form['sgpa'])
        percentage = (sgpa - 0.75) * 10
        return render_template('result.html', result=f"Your percentage is: {round(percentage, 2)}%")

    elif option == 'sgpa_back':
        obtained_credits = float(request.form['obtained_credits'])
        total_credits = float(request.form['total_credits'])
        sgpa = obtained_credits / total_credits
        percentage = (sgpa - 0.75) * 10
        return render_template('result.html', result=f"Your SGPA is: {round(sgpa, 2)} | Percentage: {round(percentage, 2)}%")

    elif option == 'ygpa':
        sem1 = float(request.form['sem1'])
        sem2 = float(request.form['sem2'])
        ygpa = (sem1 + sem2) / 2
        percentage = (ygpa - 0.75) * 10
        return render_template('result.html', result=f"Your YGPA is: {round(ygpa, 2)} | Percentage: {round(percentage, 2)}%")

    elif option == 'dgpa':
        year = int(request.form['year'])
        ygpas = []
        for i in range(1, year+1):
            ygpas.append(float(request.form[f'ygpa{i}']))
        dgpa = sum(ygpas) / len(ygpas)
        percentage = (dgpa - 0.75) * 10
        return render_template('result.html', result=f"Your DGPA is: {round(dgpa, 2)} | Percentage: {round(percentage, 2)}%")

    elif option == 'cgpa':
        obtained_credits = float(request.form['obtained_credits'])
        total_credits = float(request.form['total_credits'])
        cgpa = obtained_credits / total_credits
        percentage = (cgpa - 0.75) * 10
        return render_template('result.html', result=f"Your CGPA is: {round(cgpa, 2)} | Percentage: {round(percentage, 2)}%")

    else:
        return render_template('result.html', result="Invalid selection.")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
