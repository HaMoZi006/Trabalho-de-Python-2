########################################
##ANA LUISA RIGOTTI LEITE RA: 22400558##
########################################

########################################
##Felipe Rios dos Santos RA: 22403886###
########################################
class Motor:
    def status(self):
        return "Motor abastecido."

class Pneu:
    def status(self):
        return "Pneu calibrado."

class Veiculo(Motor, Pneu):
    def status(self):
        status_motor = Motor.status(self)
        status_pneu = Pneu.status(self)
        return f"{status_motor}\n{status_pneu}"

veiculo = Veiculo()
print(veiculo.status())