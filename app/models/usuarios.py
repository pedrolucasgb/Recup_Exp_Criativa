from models.db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Usuario(UserMixin, db.Model):
    __tablename__ = "usuarios"
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(256), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)  # 'cliente', 'atendente', 'caixa'
    ativo = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    # Relacionamentos
    comandas = db.relationship('Comanda', back_populates='cliente', lazy=True, foreign_keys='Comanda.cliente_id')
    
    def __init__(self, nome, email, senha, tipo='cliente'):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.tipo = tipo
    
    @staticmethod
    def save_usuario(nome, email, senha, tipo='cliente'):
        """Salvar um novo usuário"""
        try:
            usuario = Usuario(
                nome=nome,
                email=email,
                senha=generate_password_hash(senha),
                tipo=tipo
            )
            db.session.add(usuario)
            db.session.commit()
            return True, usuario
        except Exception as e:
            db.session.rollback()
            return False, str(e)
    
    @staticmethod
    def get(user_id):
        """Buscar usuário por ID"""
        return Usuario.query.get(int(user_id))
    
    @staticmethod
    def get_by_email(email):
        """Buscar usuário por email"""
        return Usuario.query.filter_by(email=email).first()
    
    @staticmethod
    def get_usuarios():
        """Listar todos os usuários"""
        return Usuario.query.all()
    
    @staticmethod
    def get_by_tipo(tipo):
        """Buscar usuários por tipo"""
        return Usuario.query.filter_by(tipo=tipo, ativo=True).all()
    
    @staticmethod
    def get_usuarios_by_tipo(tipo):
        """Buscar usuários por tipo (alias para get_by_tipo)"""
        return Usuario.get_by_tipo(tipo)
    
    @staticmethod
    def atualizar_usuario(usuario_id, nome=None, email=None, senha=None, tipo=None):
        """Atualizar dados de um usuário"""
        try:
            usuario = Usuario.query.get(int(usuario_id))
            if not usuario:
                return False, "Usuário não encontrado"
            
            if nome:
                usuario.nome = nome
            if email:
                # Verificar se email já existe em outro usuário
                usuario_existente = Usuario.query.filter_by(email=email).first()
                if usuario_existente and usuario_existente.id != usuario.id:
                    return False, "Email já cadastrado para outro usuário"
                usuario.email = email
            if senha:
                usuario.senha = generate_password_hash(senha)
            if tipo:
                usuario.tipo = tipo
            
            db.session.commit()
            return True, usuario
        except Exception as e:
            db.session.rollback()
            return False, str(e)
    
    @staticmethod
    def desativar_usuario(usuario_id):
        """Desativar um usuário"""
        try:
            usuario = Usuario.query.get(int(usuario_id))
            if not usuario:
                return False, "Usuário não encontrado"
            
            usuario.ativo = False
            db.session.commit()
            return True, usuario
        except Exception as e:
            db.session.rollback()
            return False, str(e)
    
    @staticmethod
    def ativar_usuario(usuario_id):
        """Ativar um usuário"""
        try:
            usuario = Usuario.query.get(int(usuario_id))
            if not usuario:
                return False, "Usuário não encontrado"
            
            usuario.ativo = True
            db.session.commit()
            return True, usuario
        except Exception as e:
            db.session.rollback()
            return False, str(e)
    
    @staticmethod
    def remover_usuario(usuario_id):
        """Remover permanentemente um usuário do banco de dados"""
        try:
            usuario = Usuario.query.get(int(usuario_id))
            if not usuario:
                return False, "Usuário não encontrado"
            
            db.session.delete(usuario)
            db.session.commit()
            return True, f"Usuário {usuario.nome} removido com sucesso"
        except Exception as e:
            db.session.rollback()
            return False, str(e)
    
    def check_password(self, senha):
        """Verificar se a senha está correta"""
        return check_password_hash(self.senha, senha)
    
    def is_cliente(self):
        return self.tipo == 'cliente'
    
    def is_atendente(self):
        return self.tipo == 'atendente'
    
    def is_caixa(self):
        return self.tipo == 'caixa'
    
    def __repr__(self):
        return f'<Usuario {self.nome} ({self.tipo})>'
