# Contact Manager

A simple **Python command-line contact manager** that allows you to add, list, edit, and remove contacts.  
All contact data is stored in a local `contacts.json` file.


## 📋 Features

- ➕ Add new contacts (name, phone, and email)  
- 📜 List all saved contacts  
- 📝 Edit existing contacts  
- ❌ Remove contacts  
- 💾 Persistent storage using a JSON file


## 🧠 How It Works

Contacts are saved in the file `contacts.json`, located in the same directory as the script.  
Each contact is stored in JSON format with the following structure:

```json
[
    {
        "name": "JOHN DOE",
        "phone": "123456789",
        "email": "john@email.com"
    }
]
```

## 🚀 Usage

### 1. Clone this repository

```
git clone https://github.com/deboraheringer/contact-manager.git
cd contact-manager
```

### 2. Run the script
```
python3 contact_manager.py
```

### 3. Follow the on-screen menu
```
=== MENU DE CONTATOS ===
1 - Adicionar contato
2 - Listar contatos
3 - Remover contato
4 - Editar contato
0 - Sair
```


## 🧩 Requirements

- Python 3.8+

## 🧑‍💻 Author

**Débora Heringer**   
💻 [GitHub: deboraheringer](https://github.com/deboraheringer)
