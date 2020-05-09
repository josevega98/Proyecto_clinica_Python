import os
def design():
    print("*******************************************")
    print("*\t\t\t\t\t  *")
    print("* Bienvenidos al sistema Python Pacientes *")
    print("*\t\t\t\t\t  *")
    print("*******************************************")
    print("")
    print("Elija una Opcion \n")
    print("1.- Cargar Paciente nuevo")
    print("2.- Buscar Paciente por nombre")
    print("3.- Listar Pacientes")
    print("4.- Salir")

def upload():

    name = input("Digite el nombre del paciente: ")
    age = int(input("Digite la edad del paciente: "))
    smook = input("Digite si fuma o no: True / False: ")
    print("Datos listos para ingresar: \n")
    print("Nombre: ",name," Edad: ",age, " Fumador: ",smook)
    confirm = input("Desea Confirmar el paciente? Si / No").lower()
    if confirm == "si":
        paciente = {"name: ": name,"age: ": age, "smooker: ": smook}
        pacientes.append(paciente)
        os.system('cls')
        menu()
    else: 
        os.system('cls')
        menu()

def serch(name):
    valor = True
    for x in range(len(pacientes)):
        if pacientes[x]["name: "].lower()==name.lower():
            print("")
            print("Paciente encontrado - > ",pacientes[x]["name: "]," Con edad: ",pacientes[x]["age: "]," Fumador: ",pacientes[x]["smooker: "])
            print("")
        else:
            valor = False
        if not valor:
            print("Paciente no encontrado")
    option=input("presione cualquier tecla para volver al menu")
    os.system('cls')
    menu()

def listar():
    for x in range(len(pacientes)):
        print("")
        print("Paciente N°:",x+1)
        for k,v in pacientes[x].items():
            print(k,"\t\t",v)
    print("")
    option=input("presione cualquier tecla para volver al menu")
    os.system('cls')
    menu()

def menu():
    design()
    response = input("Digite una opcion--> ")
    if response == "1" :
        upload()
    elif response == "2":
        name = input("Ingrese el nombre a buscar: ")
        serch(name)
    elif response == "3":
        listar()
    elif response == "4":
        print("programa finalizado")
    else:
        print("Opcion no valida")

os.system('cls')
pacientes = []
menu()