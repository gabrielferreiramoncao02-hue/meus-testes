import random

print("====================================")
print("  BEM-VINDO AO JOGO DA ADIVINHAÇÃO  ")
print("====================================")

# O computador escolhe um número secreto entre 1 e 10
numero_secreto = random.randint(1, 10)
tentativas = 0

while True:
	chute = int(input("Chute um número entre 1 e 10: "))
	tentativas = tentativas + 1

	if chute == numero_secreto:
		print(f"🎉 PARABÉNS! Você acertou em {tentativas} tentativas!")
		break
	elif chute < numero_secreto:
		print("Dica: O número secreto é MAIOR! Tente de novo.")
	else:
		print("Dica: O número secreto é MENOR! Tente de novo.")
