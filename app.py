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

        if year == 4:
            lateral = request.form.get('lateral')
            if lateral in ['Y', 'y']:
                ygpa2 = float(request.form['ygpa2'])
                ygpa3 = float(request.form['ygpa3'])
                ygpa4 = float(request.form['ygpa4'])
                dgpa = (ygpa2 + (1.5 * ygpa3) + (1.5 * ygpa4)) / 4
            elif lateral in ['N', 'n']:
                ygpa1 = float(request.form['ygpa1'])
                ygpa2 = float(request.form['ygpa2'])
                ygpa3 = float(request.form['ygpa3'])
                ygpa4 = float(request.form['ygpa4'])
                dgpa = (ygpa1 + ygpa2 + (1.5 * ygpa3) + (1.5 * ygpa4)) / 5
            else:
                return render_template('result.html', result="Invalid input for lateral entry.")
        
        elif year == 3:
            ygpa1 = float(request.form['ygpa1'])
            ygpa2 = float(request.form['ygpa2'])
            ygpa3 = float(request.form['ygpa3'])
            dgpa = (ygpa1 + ygpa2 + ygpa3) / 3

        elif year == 2:
            ygpa1 = float(request.form['ygpa1'])
            ygpa2 = float(request.form['ygpa2'])
            dgpa = (ygpa1 + ygpa2) / 2

        elif year == 1:
            ygpa1 = float(request.form['ygpa1'])
            dgpa = ygpa1
            percentage = (dgpa - 0.75) * 10
            return render_template('result.html',
                result=f"Your DGPA is your YGPA itself: {round(dgpa, 2)} | Percentage: {round(percentage, 2)}%"
            )

        else:
            return render_template('result.html', result="Invalid course duration.")

        convert = request.form.get('convert')
        if convert in ['Y', 'y']:
            percentage = (dgpa - 0.75) * 10
            return render_template('result.html',
                result=f"Your DGPA is: {round(dgpa, 2)} | Percentage: {round(percentage, 2)}%"
            )
        else:
            return render_template('result.html',
                result=f"Your DGPA is: {round(dgpa, 2)}"
            )

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
