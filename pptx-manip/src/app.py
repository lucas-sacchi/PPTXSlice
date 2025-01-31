from flask import Flask, render_template, request, send_file, jsonify
from pptx import Presentation
import io
import zipfile

app = Flask(__name__, static_folder="static", template_folder="templates")

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

    prs = Presentation(file)

    slide_ranges = request.form.getlist("slideRanges[]")
    file_names = request.form.getlist("fileNames[]")
    slide_ranges = [tuple(map(int, r.split("-"))) for r in slide_ranges]

    # Criar um arquivo ZIP em memória
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
        for i, (start, end) in enumerate(slide_ranges):
            new_prs = Presentation()

            for j in range(start - 1, end):
                slide_layout = new_prs.slide_layouts[0]
                new_slide = new_prs.slides.add_slide(slide_layout)

                for shape in prs.slides[j].shapes:
                    if hasattr(shape, "text"):
                        new_slide.shapes.title.text = shape.text

            output_pptx = io.BytesIO()
            new_prs.save(output_pptx)
            output_pptx.seek(0)

            zipf.writestr(f"{file_names[i]}.pptx", output_pptx.getvalue())

    zip_buffer.seek(0)

    return send_file(zip_buffer, mimetype="application/zip", as_attachment=True, download_name="arquivos_divididos.zip")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
