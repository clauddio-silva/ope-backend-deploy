from src.main.config import app, api
import os


if __name__ == "__main__":
    port = int(os.getenv('PORT'), '5000')
    api.init_app(app)
    app.run(host='0.0.0.0', port=port)