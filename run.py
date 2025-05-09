import os
os.environ["FLASK_SKIP_DOTENV"] = "1"

from app import create_app
import ssl

app = create_app()

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')
    app.run(ssl_context=context, debug=True)
