print("hola!, Bienvenido a la historia")
print("\ndeseas comenzar?, pon 'vamos'")
player=input("\n R:")
player = "vamos"
if player == "vamos":
   
   print(f"comenzemos!")

else:
   print("sera la proxima")
print("antes de iniciar para ganar debes obtener el emblema del ganador")
print("\n\n\n es un bosque por la noche y luego de un rato luego de una ardua caminata encuentras una antorcha y una linterna")

player=input("que escojeras?\n 1=antorcha , 2=linterna:    ")

player1= "1"


if player == player1:
   
   print("\n has hagarrado la antorcha y has visto a un oso " "\n luego se apaga la antorchas... que escojes") 
   player= input("\n 3=corre, 4=escondete 5=distraer al oso")
   player2="3"
   player3="4"
   player4="5"
   if player == player2:
    print("\n\n estas corriendo y de repente caes a un lago \n y cuando caes vez un pueblo y estas a salvo \n o eso crees")
   
   elif player == player3:
    print("te has escondido pero... el oso te atrapo y ahora debes escapar")
    player=input("vas por el 6=barranco o por 7=la montaña:  ")
    
    player5 = "6"
    
    player6 =  "7"
    
    if player == player5:
      print("has caido en un lago y has hallado un pueblo")
      print("estos no son pueblerinos comunes \n O NO SON MALOS aaahhhhhh!...")
      player=input("escoje!. 8=te dejas capturar y pierdes o 9= sales del juego y reinicias ")
      player7= "8"
      player8= "9"
      if player == player7:
        print("te has dejado capturar asi que HAS PERDIDO!")
      elif player == player8:
        print("HAS \n TERMINADO \n  ESTA \n   HISTORIA \n    DE \n     MANERA \n      INCOMPLETA ")
    
    
    
    elif player == player6:
      print("hivas a subir pero a caido una gran roca y te a eliminado\n\n\n YOU LOSE")
    else:
      print("")  
 
  
   elif player==player4:
   
    print("le has tirado muchas piedras al oso pero... \n lo siento has sido hallado por el oso y te a eliminado \n\n\n INTENTA DE NUEVO")  
   else:
     print("")

player20="2"


if player == player20:
  
  print("\n\nhas escojido la linterna \n\n el camino se a iluminado pero has escuchado un fuerte ruido")
  
  player=input("\n\n escoje! 10= seguir el camino, 11= buscar, 12= ignorar y salir del juego:    ")
 
  player9="10"
 
  player10="11"
 
  player11="12"
 
  if player == player9:
 
    print("\n seguiste el camino pero te has conseguido una manada de lobos ostiles \n  HAS SIDO ELIMINADO")
 
 
  elif player == player10:
    print("\n has buscado y conseguiste el emblema del ganador \n\n FELIZIDADES HAS FINALIZADO LA HISTORIA DE MANERA EFECTIVA :) \n\n")
 
  elif player == player11:
    print("\n has ignorado el ruido y decidiste salir del juego \n\n NO HAS COMPLETADO LA HISTORIA \n\n\n\n\n\n\n\n\n")
 
else:
  print("")
  
























































































































