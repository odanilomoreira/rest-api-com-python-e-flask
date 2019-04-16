from sql_alchemy import banco

class UsuarioModel(banco.Model):
    __tablename__ = 'usuarios'
    user_id = banco.Column(banco.Integer, primary_key=True)
    login = banco.Column(banco.String(40))
    senha = banco.Column(banco.String(40))

    def __init__(self,login,senha):
        self.login = login
        self.senha = senha

    def json(self):
        return {
            'user_id': self.user_id,
            'login': self.login
            #nao retornar senha
        }

    def save_user(self):
        banco.session.add(self)
        banco.session.commit()

    def delete_user(self):
        banco.session.delete(self)
        banco.session.commit()

    @classmethod
    def find_by_id(cls,user_id):
        return cls.query.filter_by(user_id=user_id).first()
