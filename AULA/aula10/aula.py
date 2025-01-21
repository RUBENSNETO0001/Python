'''
# para instalar a biblioteca de graficos( pip install matplotlib )

# para importa a biblioteca mais so uma função
from matplotlib import pyplot as plt

# colocar em uma lista numeros
eixo_x_dias = [1, 5 , 10 , 15 , 20 , 25, 30, 35, 40] # base
eixo_y_temp_max = [28, 29,25, 32, 34, 36, 31, 30, 20] # altura

# explicitar cada eixo 
plt.plot(eixo_x_dias,eixo_y_temp_max)

# mostrar no garfico
plt.show()

================================================================================================================

from matplotlib import pyplot as plt

eixo_x_dias = [1, 5 , 10 , 15 , 20 , 25, 30, 35, 40] # base
eixo_y_temp_max = [28, 29,25, 32, 34, 36, 31, 30, 20] # altura
eixo_y_temp_min = [27, 19,15, 12, 14, 26, 11, 10, 30] # segunda linha no grafico

plt.plot(eixo_x_dias,eixo_y_temp_max)
# o plot so aceitar 2 variaveis se colocar outra colocar na em outro plot que no final vai se juntar
plt.plot(eixo_x_dias,eixo_y_temp_min)

# mostrar no garfico
plt.show()

================================================================================================================

# aqui vou mudar o estilo de linha do grafico
plt.plot(eixo_x_dias,eixo_y_temp_max, linestyle= '--', marker ="3")# a linha pode ficar em bolinas '..' e no market da de colocar nas pontas um bolinha tbm com 'o' e um numero tbm 1 a 6'

================================================================================================================

#para colocar uma color na linha, e a grosura da linha
plt.plot(eixo_x_dias,eixo_y_temp_min, color='purple', linewidth = 6)

================================================================================================================

# titulo la em cima do grafito
plt.title('Temperatura')

# texto de baixo
plt.xlabel("eixo x")

# txt do lado
plt.ylabel('eixo y')

================================================================================================================

# para mostra oque e cada linha 
plt.legend(['Temp Max', 'Temp min'])

================================================================================================================

# para colocar a grade do fundo
plt.grid()
plt.grid(true)

================================================================================================================

# mostra td os stylos
print(plt.style.available)

# modificar o estilo
plt.style.use('Solarize_Light2')


'''
from matplotlib import pyplot as plt

# modificar o estilo
plt.style.use('seaborn-v0_8-dark')

eixo_x_dias = [1, 5 , 10 , 15 , 20 , 25, 30, 35, 40] # base
eixo_y_temp_max = [28, 29,25, 32, 34, 36, 31, 30, 20] # altura
eixo_y_temp_min = [27, 19,15, 12, 14, 26, 11, 10, 30] # segunda linha no grafico

# aqui vou mudar o estilo de linha do grafico
plt.plot(eixo_x_dias,eixo_y_temp_max, linestyle= '--', marker ="3")# a linha pode ficar em bolinas '..' e no market da de colocar nas pontas um bolinha tbm com 'o' e um numero tbm 1 a 6'

#para colocar uma color na linha, e a grosura da linha
plt.plot(eixo_x_dias,eixo_y_temp_min, color='purple', linewidth = 6)

# titulo la em cima do grafito
plt.title('Temperatura')

# texto de baixo
plt.xlabel("eixo x")

# txt do lado
plt.ylabel('eixo y')

# para mostra oque e cada linha 
plt.legend(['Temp Max', 'Temp min'])
plt.show()