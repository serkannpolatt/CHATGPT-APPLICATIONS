from flask import Flask, Response, request
import qrcode

app = Flask(__name__)

@app.route("/qr", methods=["GET"])
def generate_qr():
    url = request.args.get("url")
    if url is None:
        return "Error: No URL provided.", 400

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    return Response(response=img.tobytes(), content_type="image/png")

if __name__ == "__main__":
    app.run()
