import rpyc
import time
from rpyc.utils.server import ThreadedServer

class MyService(rpyc.Service):
	# método ao se conectar
	def on_connect(self, conn):
		print("SERVIDOR - Cliente conectado ao Servidor! \n")
		pass
	
	# método ao se desconectar
	def on_disconnect(self, conn):
		print("SERVIDOR - Cliente desconectado ao Servidor! Adeus! \n")
		pass
	
	# este é um método exposto
	def exposed_get_answer(self):
		return 42
	
	# este é um atributo exposto
	exposed_the_real_answer_though = 43

	# este não é um método exposto
	def get_question(self):
		return "Qual é a cor do cavalo branco do Napoleão?"
	
  # método exposto para somar os elementos do vetor
	def exposed_somaVetor(self, vetor):
		start = time.time()
		soma = sum(vetor)
		end = time.time()
		print(f"O tempo para execução da função no servidor foi de: {end-start} segundos \n")
		return soma

# para inciar o servidor
if __name__ == "__main__":
	t = ThreadedServer(MyService, port =18861)
	t.start()
