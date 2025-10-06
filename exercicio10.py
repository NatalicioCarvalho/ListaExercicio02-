nome = input("Digite o nome completo: ")
idade = int(input("Digite a idade: ")) 
curso = input("Digite o curso: ")
evento = input("Digite o nome do evento: ")
mensagem_confirmacao = (
    f"Confirmado! {nome}, {idade} anos, estudante de {curso}, "
    f"está inscrito no evento {evento}."
)
print("\n" + "=" * 60)
print("              INSCRIÇÃO REALIZADA COM SUCESSO!")
print("=" * 60)
print(mensagem_confirmacao)
print("=" * 60)
