from routes.routes import application

@application.route("/")
def test():
    return "Welcome!", 200

if __name__ == "__main__":
    application.run(debug=True)

