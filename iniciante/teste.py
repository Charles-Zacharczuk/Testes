from manim import *


class TesteTexto(Scene):
    def construct(self):
        texto = Text("Olá, Manim!")
        self.play(Write(texto))
        self.wait(1)
