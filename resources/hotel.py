from flask_restful import Resource, reqparse

hoteis = [
        {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Rio de Janeiro'
        },
        {
        'hotel_id': 'bravo',
        'nome': 'Bravo Hotel',
        'estrelas': 4.4,
        'diaria': 380.90,
        'cidade': 'Santa Catarina'
        },
        {
        'hotel_id': 'charlie',
        'nome': 'Charlie Hotel',
        'estrelas': 3.9,
        'diaria': 320.20,
        'cidade': 'Santa Catarina'
        }
]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}

class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return {'message': 'Hotel not found.'}, 404

    def post(self, hotel_id):
        atributos = reqparse.RequestParser()
        atributos.add_argument('nome')
        atributos.add_argument('estrelas')
        atributos.add_argument('diaria')
        atributos.add_argument('cidade')

        dados = atributos.parse_args()

        novo_hotel = {
                    'hotel_id': hotel_id,
                    'nome': dados['nome'],
                    'estrelas': dados['estrelas'],
                    'diaria': dados['diaria'],
                    'cidade': dados['cidade']
                     }
        hoteis.append(novo_hotel)
        return novo_hotel, 201

    def put(self, hotel_id):
        atributos = reqparse.RequestParser()
        atributos.add_argument('nome')
        atributos.add_argument('estrelas')
        atributos.add_argument('diaria')
        atributos.add_argument('cidade')
        dados = atributos.parse_args()
        novo_hotel = {
                    'hotel_id': hotel_id,
                    'nome': dados['nome'],
                    'estrelas': dados['estrelas'],
                    'diaria': dados['diaria'],
                    'cidade': dados['cidade']
                     }

        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                hotel_encontrado = hotel
            else:
                hotel_encontrado = None

        if hotel_encontrado:
            hotel_encontrado.update(novo_hotel)
            return hotel_encontrado
        hoteis.append(novo_hotel)
        return novo_hotel

    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'message': 'Item deleted.'}
