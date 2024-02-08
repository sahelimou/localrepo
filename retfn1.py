def display(msg):
    greet="I am outer fn"

    def display_msg():
        print(greet+msg)

    return display_msg

fun=display("I am inner fn")
fun()
