let Tilfeldig_mellom_1_og_6 = 0
let Svaret_er_tallet_1 = 0
input.onButtonPressed(Button.A, function () {
    Tilfeldig_mellom_1_og_6 = randint(0, 6)
    if (Tilfeldig_mellom_1_og_6 == 3) {
        basic.showNumber(Tilfeldig_mellom_1_og_6)
        music.playMelody("C5 B C5 B A G A - ", 120)
    } else if (Tilfeldig_mellom_1_og_6 == 5) {
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
    } else {
        basic.showNumber(Tilfeldig_mellom_1_og_6)
        basic.showString("Bent")
    }
})
input.onButtonPressed(Button.B, function () {
    Svaret_er_tallet_1 = 1
    basic.showString("" + (Svaret_er_tallet_1))
})
