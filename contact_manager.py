import json
import os

FILE_PATH = "contacts.json"

def load_contacts():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []  
    return []

def save_contacts(contacts):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=4, ensure_ascii=False)

contacts = load_contacts()

def show_menu():
    print("\n=== MENU DE CONTATOS ===")
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Remover contato")
    print("4 - Editar contato")
    print("0 - Sair")

def edit_options():
    print("1 - Nome")
    print("2 - Telefone")
    print("3 - E-mail")
    print("0 - Sair")

def add_contact():
    name = input("Nome: ")
    phone = input("Telefone: ")
    email = input("E-mail: ")
    contact = {
        "name": name.upper(),
        "phone": phone,
        "email": email,
    }
        
    contacts.append(contact)
    save_contacts(contacts)
    print(f"\nContato {name} foi adicionado com sucesso!")

def list_contacts():
    if not contacts:
        print("\nAinda não há contatos cadastrados.")
        return
    
    print("\n=== LISTA DE CONTATOS ===")
    for i, contact_item in enumerate(contacts, start = 1):
        print(f"{i}. {contact_item['name']}")
        print(f"   Telefone: {contact_item['phone']}")
        print(f"   E-mail: {contact_item['email']}\n")
        print("-" * 30)

def remove_contact():  
    list_contacts()
    remove_number = input("Informe o número do contato que deseja remover (ou digite 0 para cancelar): ")

    if remove_number == "0":
        print("\nVoltando ao menu principal...")
        return
    
    try:
        index = int(remove_number) - 1
        if 0 <= index < len(contacts):
            removed_contact = contacts.pop(index)
            save_contacts(contacts)
            print(f"\nContato {removed_contact['name']} removido com sucesso!")
        else:
            print("\nNúmero inválido. Tente novamente.")
    except ValueError:
        print("\nEntrada inválida. Por favor, digite um número.")

def edit_contact():
    list_contacts()
    edit_number = input("Informe o número do contato que deseja editar (ou digite 0 para cancelar): ")

    if edit_number == "0":
        print("\nVoltando ao menu principal...")
        return
    
    try:
        index = int(edit_number) - 1
        if 0 <= index < len(contacts):
            contact_item = contacts[index]
            print(f"\n=== O que você deseja editar em {contact_item['name'].upper()}? ===")
            edit_options()
            edit_choice = input("Escolha uma opção: ")

            if edit_choice == "1":
                new_name = input(f"Digite o novo nome para alterar {contact_item['name']}: ")
                print(f"\nNome atualizado de {contact_item['name']} para {new_name}.")
                contact_item['name'] = new_name.upper()
            elif edit_choice == "2":
                new_phone = input(f"Digite o novo telefone para alterar {contact_item['phone']}: ")
                print(f"\nTelefone atualizado de {contact_item['phone']} para {new_phone}.")
                contact_item['phone'] = new_phone
            elif edit_choice == "3":
                new_email = input(f"Digite o novo e-mail para alterar {contact_item['email']}: ")
                print(f"\nE-mail atualizado de {contact_item['email']} para {new_email}.")
                contact_item['email'] = new_email
            elif edit_choice == "0":
                print("\nVoltando ao menu principal...")
                return
            else:
                print("\nOpção inválida!")
                return
            
            save_contacts(contacts)

        else:
            print("\nNúmero inválido. Tente novamente.")

    except ValueError:
        print("\nEntrada inválida. Por favor, digite um número.")

while True:
    show_menu()
    option = input("Escolha uma opção: ")

    if option == "1": #cadastrar
        add_contact()

    elif option == "2": #listar
        list_contacts()

    elif option == "3": #remover
        remove_contact()     

    elif option == "4": #editar
        edit_contact()

    elif option == "0":
        print("\nEncerrando o programa. Até logo!")
        break
    else:
        print("\nOpção inválida!")