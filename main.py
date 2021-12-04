def on_received_number(receivedNumber):
    if receivedNumber == 0:
        images.create_image("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """).show_image(0)
    elif receivedNumber == 1:
        for index in range(5):
            images.arrow_image(ArrowNames.WEST).show_image(0)
            images.create_image("""
                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
            """).show_image(0)
        images.arrow_image(ArrowNames.WEST).show_image(0)
    elif receivedNumber == 2:
        for index2 in range(5):
            images.arrow_image(ArrowNames.EAST).show_image(0)
            images.create_image("""
                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
            """).show_image(0)
        images.arrow_image(ArrowNames.EAST).show_image(0)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.send_number(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    radio.send_number(0)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    radio.send_number(2)
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(99)