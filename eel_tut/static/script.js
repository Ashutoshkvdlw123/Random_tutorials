eel.say_hello_from_js("Javascript!");

eel.expose(say_hello_from_python)
function say_hello_from_python(x){
    console.log("Hello from {}".replace("{}", x))
}