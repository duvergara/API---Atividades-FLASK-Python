from models import Pessoas


def insere_pessoas():
        pessoa = Pessoas(nome='eduardo', idade=23)
        print(pessoa)
        pessoa.save()

def consulta():
    pessoa = Pessoas.query.all()
    print (pessoa)


if __name__=='__main__':
    insere_pessoas()
    consulta()