print("Hola Bienvenido.")
ai = 'Dino'
print("Mi nombre es {}. Gracias por venir, me sentia muy solo :(".format(ai))

username = input('Como te llamas? ')
print( f'Mucho gusto, {username}. Gracias por hablar conmigo.' )

age = int(input('Cuantos años tienes?'))
if age > 18 or age == 18 :
	print("Wow, estas muy viejo. De casualidad no eramos amigos antes?")
else:   
	print("Todavia eres un bebe. Sera mejor que vayas con tus padres, no deberias hablar con desconocidos")
  
s =input('Siguente preguna! Eres hombre o mujer? (m/h)')
if s <= 'h' :
	print("A mi no me engañas, yo lo se todo; es mas ni siquiera eres humano")
else:   
	print("Por que me mientes? te vi hace unos dias y se que eres.")

air = 'Dinosa'
print("No te creas, es solo que mi amigo {} me dejo aqui y eres el primero con quien hablo en años".format(air))

a = input('Quieres ser mi amigo? (s/n)')
if a == 'n':
	  print("No me importa, ya lo somos aun que no quieras ")
else:   
	print("Perfecto :) ...... Sigue queriendo.")

print( f'Oye no te enojes, solo bromeo. No puedes enojarte con un hermoso Dinosaurio' )

print("Oh, es cierto, no puedes verme *o*... bueno que te parece si... ")

adios =input('Escuchaste eso? (s/n)')
if adios == 's' :
	print("Tengo que irme, fue un gusto {}. Espero que nos veamos pronto". format(username))
else:   
	print("Fue una indirecta mi hermoso amigo, nos vemos :)")
