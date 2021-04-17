from typing import Dict

from flask import Flask
from flask_restful import Resource, Api, request
from models import  Pessoas

app =  Flask(__name__)
api = Api(app)

class Pessoa(Resource):
     def get (self, nome):
         try:
             pessoa = Pessoas.query.filter_by(nome=nome).first()
             response = {
                 'nome':pessoa.nome,
                 'idade':pessoa.idade,
                 'id':pessoa.id
              }

         except AttributeError:
             response = {
                 'status':'error',
                 'mensagem':'Pessoa nao encontrada'
              }
             return response
     def put(self, nome ):
                pessoa = Pessoas.query.filter_by(nome=nome).first()
                dados = request.json
                if 'nome' in dados:
                    pessoa.nome = dados['nome']
                if 'idade' in dados:
                     pessoa.idade =dados['idade']
                pessoa.save()
                response ={
                    'nome' : pessoa.nome ,
                    'idade' : pessoa.idade ,
                    'id' : pessoa.id
                }
                return response

     def __delete__(self,nome):
         pessoa = Pessoas.query.filter_by(nome=nome).first()
         mensagem = 'Pessoa{} excluida  com sucesso'.format(pessoa.nome)
         pessoa.delete()
         return {'status':'sucesso', 'mensagem': mensagem}

class Listar_pessoas(Resource):
    def get( self ):
        pessoa = Pessoas.query,all()
         for i  in pessoa:
             
        return pessoa









api.add_resource(Pessoa, '/pessoa/<string:nome>/')

if __name__ == '__main__':
    app.run(debug = True)
