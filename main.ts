radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 0) {
        images.createImage(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `).showImage(0)
    } else if (receivedNumber == 1) {
        for (let index = 0; index < 5; index++) {
            images.arrowImage(ArrowNames.West).showImage(0)
            images.createImage(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                `).showImage(0)
        }
        images.arrowImage(ArrowNames.West).showImage(0)
    } else if (receivedNumber == 2) {
        for (let index = 0; index < 5; index++) {
            images.arrowImage(ArrowNames.East).showImage(0)
            images.createImage(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                `).showImage(0)
        }
        images.arrowImage(ArrowNames.East).showImage(0)
    }
})
input.onButtonPressed(Button.A, function () {
    radio.sendNumber(1)
})
input.onButtonPressed(Button.AB, function () {
    radio.sendNumber(0)
})
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(2)
})
radio.setGroup(99)
