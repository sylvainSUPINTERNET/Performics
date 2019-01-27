from flask import Flask, Blueprint
from router.user import api_users_router
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.register_blueprint(api_users_router)

# run server
if __name__ == '__main__':
    app.run(debug=True)
