from flask import Flask, Blueprint
from router.user import api_users_router

app = Flask(__name__)
app.register_blueprint(api_users_router)


# run server
if __name__ == '__main__':
    app.run(debug=True)
