from exercício3 import Trip
trip0 = Trip("Orlando")
trip1= Trip("Rio de Janeiro")
trip2 = Trip("Paris")
trip3 = Trip("Londres")
trip4 = Trip("Gramado")

print("E aí viajantes. Temos algumas ofertas para você.")
traveler = input("Digite seu nome para começar\n")
print(f"{traveler} temos 5 destinos que combinam com você"
      """
      [0] - Orlando
      [1] - Rio de Janeiro
      [2] - Paris
      [3] - Londres
      [4] - Gramado
      
      """
      )

choice = int(input("Selecione o destino da viagem\n"))
list_trip = [trip0, trip1, trip2, trip3, trip4]

for option in list_trip:
    if choice >= 5:
        print("Esta opção não está incluída em nossos destinos")
        break
    else:
        print(f"{traveler} sua viagem para {list_trip[choice].destiny} está marcada!")
        print("Boa viagem!")
        break
