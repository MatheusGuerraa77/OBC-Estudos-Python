from contato import Contact
from contato_agenda import ContactBook

contato_agenda = ContactBook()

while True:
    print("\n --- Opções Agenda de Contatos ---")
    print("1. Adicionar Contato")
    print("2. Remover Contato")
    print("3. Listar Contatos")
    print("4. Buscar Contato")
    print("5. Sair")
    
    choice = input("Escolha a opção:\n ")
    
    if choice == "1":
        name = input("Digite o nome: \n")
        phone = input("Digite o telefone: \n")
        email= input("Digite o email: \n")
        
        contact = Contact(name, phone, email)
        contato_agenda.add_contact(contact)
        print("Contato foi adicionado com sucesso")
    elif choice == "2":
        name = input("Informe o nome para remover contato: \n")
        contact = contato_agenda.search_contact(name)
        if contact:
            contato_agenda.remove_contact(contact)
            print("Contato removido com sucesso")
    elif choice == "3":
        contato_agenda.display_contact()
        
    elif choice == "4":
        name = input("Informe o nome para buscar contato : \n")
        contact = contato_agenda.search_contact(name)
    elif choice == "5":
        break
    else:
        print("Opção Inválida. Utilize uma opção de 1 a 5 !")