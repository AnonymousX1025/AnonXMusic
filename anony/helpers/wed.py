# web.py
from flask import Flask
import os
import threading

app = Flask("anony")

@app.route("/")
def home():
    return "Bot is alive!"

def run():
    port = int(os.environ.get("PORT", 8080))
    # threaded True يكفي لعمل health check وطلبات بسيطة
    app.run(host="0.0.0.0", port=port, threaded=True)

if __name__ == "__main__":
    run()
