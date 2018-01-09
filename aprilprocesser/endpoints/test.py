from aprilprocesser import aprilprocesser_app

@aprilprocesser_app.route("/")
def hello_world_example():
    return "Hello World!"