from flask import Flask, request, make_response, send_file

app = Flask(__name__)


@app.route("/pdf")
def serve_pdf():
    pdf_path = "poc.pdf"
    try:
        response = make_response(send_file(pdf_path, mimetype="application/pdf"))
        response.headers["Access-Control-Allow-Origin"] = "*"
        return response
    except FileNotFoundError:
        return {"error": "PDF not found"}, 404


@app.route("/flag", methods=["POST", "OPTIONS"])
def receive_flag():
    resp = make_response()
    if request.method == "OPTIONS":
        resp.headers["Access-Control-Allow-Origin"] = "*"
        resp.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        resp.headers["Access-Control-Allow-Headers"] = "Content-Type"
        return resp

    try:
        pdf_data = request.data
        with open("flag.pdf", "wb") as f:
            f.write(pdf_data)
    except Exception as error:
        print(error)
    finally:
        return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
