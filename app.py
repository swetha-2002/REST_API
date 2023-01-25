from flask import Flask, request,render_template, send_file,redirect,url_for
from pdfrw import PdfReader, PdfWriter
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')


@app.route('/rotate', methods=['POST'])
def rotate_pdf():
    file_path = request.form['file_path']
    angle = int(request.form['angle_of_rotation'])
    page_number = int(request.form['page_number'])
    
    # open the pdf
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        page = reader.pages[page_number-1]
        page.Rotate = angle
        writer = PdfWriter()
        writer.addpages(reader.pages)
        with open('rotated.pdf', 'wb') as output:
            writer.write(output)
        #return 'rotated.pdf'
        return redirect(url_for('download_pdf'))
        
@app.route('/download')
def download_pdf():
    pdf_file = "rotated.pdf"
    return send_file(pdf_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
