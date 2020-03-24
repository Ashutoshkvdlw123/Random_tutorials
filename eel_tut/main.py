import eel


eel.init("static")

@eel.expose
def say_hello_from_js(x):
    print(f"Hello from {x}")

eel.say_hello_from_python("Python!")

eel.start("index.html", size=(500, 500))