from flask import Flask as F, render_template as render, request as req
import numpy as np

app = F(__name__)

@app.route('/', methods=['GET'])
def index():
    return render('index.html')

@app.route('/calculate', methods=['POST'])
def calculate_dft():
    size = int(req.form['size'])

    # Initialize an empty matrix with the selected size
    f = np.zeros((size, size), dtype=int)

    # get the matrix X from form data
    for i in range(size):
        for j in range(size):
            f[i, j] = int(req.form[f'm{i}{j}'])

    # Compute 2D DFT using NumPy
    F = np.fft.fft2(f)

    np.set_printoptions(precision=2, suppress=True)

    dft_result = F.tolist()

    return render('index.html', dft_result=dft_result, size=size)

if __name__ == '__main__':
    app.run(debug=True)
