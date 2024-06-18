class ContactBook:
    def __init__(self):
        self.contacts = [] 
        
    def add_contact(self, contact):# Método para adicionar contatos
        self.contacts.append(contact)
        
    def remove_contact(self, contact):# Método para remover contatos
        self.contacts.remove(contact)
        
    def display_contact(self):# Método para Listar contatos
        if not self.contacts:
            print("Lista de Contatos está Vazia")
        else:
            for contact in self.contacts:
                print(contact)
                print("---------------")
                
    def search_contact(self, name):# Método para buscar contatos
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(contact)
                return contact
        print("Contato não foi encontrado")