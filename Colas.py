
from collections import deque
print("las colas funcionan bajo la premisa de <primero en entrar, primero en salir>")
print("expliquemoslo con el siguiente ejemplo: llegan tres personas a una consulta médica, sus nombres son:")

cola = deque()

# Llegan tres personas: Ana, María y Héctor
cola.append("Ana")
cola.append("María")
cola.append("Héctor")

# Imprimir el estado inicial de la cola
print("Estado inicial de la cola:", list(cola))

print("Ana, al entrar primero a la consulta por llegar más temprano, es eliminada de la lista primero")

# Ana entra a la consulta y es eliminada de la cola
cola.popleft()

# Imprimir el estado de la cola después de que Ana entra
print("Después de que Ana entra:", list(cola))
print("ahora llega una cuarta persona llamada Gabriel a la consulta")
# Llega una cuarta persona llamada Gabriel
cola.append("Gabriel")

# Imprimir el estado de la cola después de que Gabriel llega
print("Después de que Gabriel llega:", list(cola))

print("la siguiente persona entra en la consulta y es borrada de la lista")
# La siguiente persona en la lista entra a la consulta
cola.popleft()

# Imprimir el estado final de la cola
print("Estado final de la cola:", list(cola))

print("de este modo, la última persona en llegar al consultorio, esa última en salir")


