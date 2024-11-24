contatos = []

def adicionar_contato(contatos, nome, telefone, email, favorito):
  contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": favorito}
  contatos.append(contato)
  print(f"Contato {nome} foi adicionado com sucessso!")

  return

def vizualizar_contatos(contatos):
  print("\nLista de contatos")
  for indice, contato in enumerate(contatos, start=1):
    nome = contato["nome"]
    telefone = contato["telefone"]
    email = contato["email"]
    favorito = "★" if contato["favorito"] else " "
    print(f"{indice}. {nome} {telefone} {email} {favorito}")
  return

def editar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email, novo_favorito):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contatos[indice_contato_ajustado]["nome"] = novo_nome
    contatos[indice_contato_ajustado]["telefone"] = novo_telefone
    contatos[indice_contato_ajustado]["email"] = novo_email
    contatos[indice_contato_ajustado]["favorito"] = novo_favorito
    print(f"Contato {novo_nome} foi atualizado com sucesso!")
  else:
    print("Índice de contato inválido!")
  return

def adicionar_contato_favorito(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contatos[indice_contato_ajustado]["favorito"] = True
    print(f"contato {indice_contato} marcada como completada")
  else:
    print("Indice de contato inválido")
  return

def deletar_contato(contatos, indice_contato):
  if 1 <= indice_contato <= len(contatos):
      contato = contatos[indice_contato - 1]
      contatos.remove(contato)
      
      print(f"Contato {novo_nome} foi deletado com sucesso!")
  else:
      print("Índice de contato inválido!")
  return

def vizualizar_lista_contato_favorito(tarefas):
  for contato in contatos:
    if contato["favorito"]:
      nome = contato["nome"]
      telefone = contato["telefone"]
      email = contato["email"]
      favorito = "★" if contato["favorito"] else " "
      print(f"{indice}. {nome} {telefone} {email} {favorito}")
  return

while True:
  print("\nMenu de gerencioador de lista de contatos")
  print("1. Adicionar contato")
  print("2. Ver contatos")
  print("3. Atualizar contato")
  print("4. Adicionar um contato ao favorito")
  print("5. Deletar contato")
  print("6. Sair")

  escolha = input("Digite a sua escolha: ")

  if escolha == "1":
    nome = input("Digite a nome do contato: ")
    telefone = input("Digite o numero de telefone: ")
    email = input("Digite o email: ")
    adicionarFavorito = input("Deseja adicioar esse contato nos favoritos? [sim/não]")
    favorito = True if adicionarFavorito == "sim" else False
    adicionar_contato(contatos, nome, telefone, email, favorito)
  elif escolha == "2":
    vizualizar_contatos(contatos)
  elif escolha == "3":
    vizualizar_contatos(contatos)
    indice_contato = input("Digite o número do contato que deseja atualizar: ")
    nome = input("Digite a nome do contato: ")
    telefone = input("Digite o numero de telefone: ")
    email = input("Digite o email: ")
    adicionarFavorito = input("Deseja adicioar esse contato nos favoritos? [sim/não]")
    favorito = True if adicionarFavorito == "sim" else False
    editar_contato(contatos, indice_contato, nome, telefone, email, favorito)
  elif escolha == "4":
    vizualizar_contatos(contatos)
    indice_contato = input("Digite o número da contato que deseja favoritar: ")
    adicionar_contato_favorito(contatos, indice_contato)
  elif escolha == "5":
    vizualizar_contatos(contatos)
    indice_contato = input("Digite o número da contato que deseja excluir: ")
    deletar_contato(contatos, indice_contato)
  elif escolha == "6":
    vizualizar_lista_contato_favorito(contatos)
  elif escolha == "7":
    break
print("Programa finalizado")