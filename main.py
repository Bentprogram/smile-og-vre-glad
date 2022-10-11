let Tilfeldig_mellom_1_og_6 = 0
input.onButtonPressed(Button.A, function () {
    Tilfeldig_mellom_1_og_6 = randint(1, 6)
    if (Tilfeldig_mellom_1_og_6 == 1) {
        basic.showNumber(Tilfeldig_mellom_1_og_6)
        music.playSoundEffect(music.createSoundEffect(
        WaveShape.Sawtooth,
        3752,
        2875,
        186,
        186,
        4242,
        SoundExpressionEffect.None,
        InterpolationCurve.Curve
        ), SoundExpressionPlayMode.UntilDone)
    } else if (Tilfeldig_mellom_1_og_6 == 2) {
        basic.showNumber(Tilfeldig_mellom_1_og_6)
        basic.showLeds(`
            # # . # #
            . . # . .
            . . # . .
            # . . . #
            . # # # .
            `)
    } else if (Tilfeldig_mellom_1_og_6 == 3) {
        basic.showNumber(Tilfeldig_mellom_1_og_6)
        music.playMelody("C5 B C5 B A G A - ", 120)
    } else if (Tilfeldig_mellom_1_og_6 == 4) {
        basic.showNumber(Tilfeldig_mellom_1_og_6)
        basic.showString("Hello!")
    } else if (Tilfeldig_mellom_1_og_6 == 5) {
        basic.showString("Bent")
        basic.showNumber(Tilfeldig_mellom_1_og_6)
    } else {
        basic.showNumber(Tilfeldig_mellom_1_og_6)
        music.startMelody(music.builtInMelody(Melodies.Blues), MelodyOptions.Once)
    }
})
input.onButtonPressed(Button.AB, function () {
    for (let index = 0; index < 3; index++) {
        Tilfeldig_mellom_1_og_6 = randint(1, 6)
        if (Tilfeldig_mellom_1_og_6 == 1) {
            basic.showNumber(Tilfeldig_mellom_1_og_6)
            music.playSoundEffect(music.createSoundEffect(
            WaveShape.Sawtooth,
            3752,
            2875,
            186,
            186,
            4242,
            SoundExpressionEffect.None,
            InterpolationCurve.Curve
            ), SoundExpressionPlayMode.UntilDone)
        } else if (Tilfeldig_mellom_1_og_6 == 2) {
            basic.showNumber(Tilfeldig_mellom_1_og_6)
            basic.showLeds(`
                # # . # #
                . . # . .
                . . # . .
                # . . . #
                . # # # .
                `)
        } else if (Tilfeldig_mellom_1_og_6 == 3) {
            basic.showNumber(Tilfeldig_mellom_1_og_6)
            music.playMelody("C5 B C5 B A G A - ", 120)
        } else if (Tilfeldig_mellom_1_og_6 == 4) {
            basic.showNumber(Tilfeldig_mellom_1_og_6)
            basic.showString("Hello!")
        } else if (Tilfeldig_mellom_1_og_6 == 5) {
            basic.showString("Bent")
            basic.showNumber(Tilfeldig_mellom_1_og_6)
        } else {
            basic.showNumber(Tilfeldig_mellom_1_og_6)
            music.startMelody(music.builtInMelody(Melodies.Blues), MelodyOptions.Once)
        }
    }
})
input.onButtonPressed(Button.B, function () {
    basic.pause(1000)
    basic.showString(""TRYKK A")
})
