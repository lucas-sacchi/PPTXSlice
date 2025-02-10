from flask import Flask, render_template, request, send_file, jsonify
from pptx import Presentation
import io
import zipfile
import os

app = Flask(__name__, static_folder="static", template_folder="templates")

def remove_unwanted_slides(prs, keep_slides):
    """
    Remove todos os slides da apresentação, exceto os especificados.
    """
    xml_slides = prs.slides._sldIdLst  # Acessa a lista de slides internos do XML
    slides_to_remove = [s for i, s in enumerate(xml_slides) if (i + 1) not in keep_slides]

    for slide in slides_to_remove:
        xml_slides.remove(slide)  # Remove os slides indesejados

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/split_pptx", methods=["POST"])
def split_pptx():
    if "file" not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Nenhum arquivo selecionado"}), 400

    # Salva o arquivo original temporariamente
    temp_file = "temp.pptx"
    file.save(temp_file)

    slide_ranges = request.form.getlist("slideRanges[]")
    file_names = request.form.getlist("fileNames[]")
    slide_ranges = [tuple(map(int, r.split("-"))) for r in slide_ranges]

    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
        for i, (start, end) in enumerate(slide_ranges):
            prs = Presentation(temp_file)  # Reabre o arquivo original
            keep_slides = list(range(start, end + 1))  # Lista de slides a manter
            
            remove_unwanted_slides(prs, keep_slides)  # Remove os slides que não fazem parte da seleção
            
            output_pptx = io.BytesIO()
            prs.save(output_pptx)
            output_pptx.seek(0)

            zipf.writestr(f"{file_names[i]}.pptx", output_pptx.getvalue())

    zip_buffer.seek(0)
    os.remove(temp_file)  # Apaga o arquivo temporário original

    return send_file(zip_buffer, mimetype="application/zip", as_attachment=True, download_name="arquivos_divididos.zip")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
