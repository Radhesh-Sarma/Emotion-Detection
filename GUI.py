import toga


def button_handler(widget):
    print("hello")


def build(app):
    box = toga.Box()

    button = toga.Button('Run', on_press=button_handler)
    button.style.padding = 50
    button.style.flex = 1

    mutation_input = toga.TextInput(placeholder = 'Enter Mutation percentage')
    mutation_input.style.padding = 50
    mutation_input.style.flex = 1
    box.add(mutation_input)
    box.add(button)

    return box


def main():
    return toga.App('Emotion Detection using genetic algorithm', 'org.beeware.helloworld', startup=build)


if __name__ == '__main__':
    main().main_loop()