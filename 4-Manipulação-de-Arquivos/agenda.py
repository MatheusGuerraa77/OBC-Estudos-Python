import os

def add_contact():
    name = input("Informe o nome :\n")
    address = input("Informe o endereço :\n")
    phone = input("Informe o celular :\n")
    
    contact = f"Nome: {name} \nEndereço: {address} \nCelular: {phone}\n"
    
    with open("dados/contatos.txt", "a", encoding="utf-8") as file:
        file.write(contact)
        
def view_contacts():
    if not os.path.exists("dados/contatos.txt"):
        print("Lista de contatos está vazia!")
        return
    with open("dados/contatos.txt", "r", encoding="utf-8") as file:
        contacts = file.read()
    print("Lista de contatos")
    print(contacts)
    
def delete_contacts():
    if not os.path.exists("contatos.txt"):
        print("Lista de contatos está vazia!")
        return
    with open("dados/contatos.txt", "w", encoding="utf-8") as file:
        contacts = file.write("")
        
    print("Contatos excluídos com sucesso!")