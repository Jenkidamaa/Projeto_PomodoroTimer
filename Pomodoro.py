import os
from time import time, sleep


class pomodoro():
    def __init__(self):
        self.tempo_inicial = time()
        self.tempo_corrent = time()
        self.tempo_maximo = 45

    def tempo_var(self):
        return self.tempo_corrent - self.tempo_inicial

    def uptade(self):
        self.tempo_corrent = time()


    def display_uptade(self):
        print(self.tempo_formatado())


    def tempo_formatado(self):
        T = self.tempo_maximo - self.tempo_var()
        Min = float(T/60)
        sec = float(T - Min*60)
        return "(" + str(Min) + ":" + str(sec) + ")"

    def mainloop(self):
        while True:
            os.system('cls')
            self.uptade()
            self.display_uptade()
            sleep(1)
            if self.tempo_var() > self.tempo_maximo:
                break

m = pomodoro
m.mainloop
