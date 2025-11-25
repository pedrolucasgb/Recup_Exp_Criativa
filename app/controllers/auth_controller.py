from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from models.usuarios import Usuario
from models.comanda import Comanda

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Página de login"""
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = Usuario.get_by_email(email)
        
        if user and user.check_password(password):
            login_user(user)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('auth.dashboard'))
        else:
            flash('Email ou senha incorretos.', 'error')
    
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """Página de registro de novos clientes"""
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Verificar se email já existe
        if Usuario.get_by_email(email):
            flash('Email já cadastrado.', 'error')
            return redirect(url_for('auth.register'))
        
        # Criar novo cliente
        success, result = Usuario.save_usuario(nome, email, password, 'cliente')
        
        if success:
            flash('Conta criada com sucesso! Faça login.', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash(f'Erro ao criar conta: {result}', 'error')
    
    return render_template('register.html')

@auth_bp.route('/dashboard')
@login_required
def dashboard():
    """Dashboard principal"""
    # Buscar comandas do usuário logado
    if current_user.is_cliente():
        # Cliente vê apenas suas comandas
        comandas = Comanda.get_comandas_by_cliente(current_user.id)
    else:
        # Atendente e Caixa veem todas as comandas
        comandas = Comanda.get_comandas()
    
    # Se for caixa, buscar comandas fechadas para pagamento
    comandas_fechadas = []
    if current_user.is_caixa():
        comandas_fechadas = Comanda.get_comandas_fechadas()
    
    # Se for atendente ou caixa, buscar lista de clientes para seleção
    usuarios_clientes = []
    if current_user.is_atendente() or current_user.is_caixa():
        usuarios_clientes = Usuario.get_usuarios_by_tipo('cliente')
    
    return render_template('dashboard.html', 
                         comandas=comandas, 
                         comandas_fechadas=comandas_fechadas,
                         usuarios_clientes=usuarios_clientes)

@auth_bp.route('/logout')
@login_required
def logout():
    """Logout do usuário"""
    logout_user()
    flash('Logout realizado com sucesso.', 'success')
    return redirect(url_for('auth.login'))

@auth_bp.route('/gerenciar-usuarios')
@login_required
def gerenciar_usuarios():
    """Página de gerenciamento de usuários - exclusivo para caixa"""
    if not current_user.is_caixa():
        flash('Acesso negado. Apenas caixa pode gerenciar usuários.', 'error')
        return redirect(url_for('auth.dashboard'))
    
    # Buscar todos os clientes e atendentes
    clientes = Usuario.query.filter_by(tipo='cliente').all()
    atendentes = Usuario.query.filter_by(tipo='atendente').all()
    
    return render_template('manage_users.html', 
                         clientes=clientes, 
                         atendentes=atendentes)

@auth_bp.route('/cadastrar-usuario', methods=['POST'])
@login_required
def cadastrar_usuario():
    """Cadastrar novo usuário (cliente ou atendente) - exclusivo para caixa"""
    if not current_user.is_caixa():
        flash('Acesso negado. Apenas caixa pode cadastrar usuários.', 'error')
        return redirect(url_for('auth.dashboard'))
    
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    tipo = request.form.get('tipo')
    
    # Validar tipo de usuário
    if tipo not in ['cliente', 'atendente']:
        flash('Tipo de usuário inválido.', 'error')
        return redirect(url_for('auth.gerenciar_usuarios'))
    
    # Verificar se email já existe
    if Usuario.get_by_email(email):
        flash('Email já cadastrado.', 'error')
        return redirect(url_for('auth.gerenciar_usuarios'))
    
    # Criar novo usuário
    success, result = Usuario.save_usuario(nome, email, senha, tipo)
    
    if success:
        flash(f'Usuário {nome} cadastrado com sucesso como {tipo}!', 'success')
    else:
        flash(f'Erro ao cadastrar usuário: {result}', 'error')
    
    return redirect(url_for('auth.gerenciar_usuarios'))

@auth_bp.route('/editar-usuario', methods=['POST'])
@login_required
def editar_usuario():
    """Editar usuário existente - exclusivo para caixa"""
    if not current_user.is_caixa():
        flash('Acesso negado. Apenas caixa pode editar usuários.', 'error')
        return redirect(url_for('auth.dashboard'))
    
    usuario_id = request.form.get('usuario_id')
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    tipo = request.form.get('tipo')
    
    # Validar tipo de usuário
    if tipo not in ['cliente', 'atendente']:
        flash('Tipo de usuário inválido.', 'error')
        return redirect(url_for('auth.gerenciar_usuarios'))
    
    # Não permitir senha vazia na atualização
    senha_para_atualizar = senha if senha else None
    
    # Atualizar usuário
    success, result = Usuario.atualizar_usuario(usuario_id, nome, email, senha_para_atualizar, tipo)
    
    if success:
        flash(f'Usuário atualizado com sucesso!', 'success')
    else:
        flash(f'Erro ao atualizar usuário: {result}', 'error')
    
    return redirect(url_for('auth.gerenciar_usuarios'))

@auth_bp.route('/desativar-usuario/<int:usuario_id>', methods=['POST'])
@login_required
def desativar_usuario(usuario_id):
    """Desativar usuário - exclusivo para caixa"""
    if not current_user.is_caixa():
        flash('Acesso negado. Apenas caixa pode desativar usuários.', 'error')
        return redirect(url_for('auth.dashboard'))
    
    # Não permitir desativar a si mesmo
    if usuario_id == current_user.id:
        flash('Você não pode desativar sua própria conta.', 'error')
        return redirect(url_for('auth.gerenciar_usuarios'))
    
    success, result = Usuario.desativar_usuario(usuario_id)
    
    if success:
        flash(f'Usuário desativado com sucesso!', 'success')
    else:
        flash(f'Erro ao desativar usuário: {result}', 'error')
    
    return redirect(url_for('auth.gerenciar_usuarios'))

@auth_bp.route('/ativar-usuario/<int:usuario_id>', methods=['POST'])
@login_required
def ativar_usuario(usuario_id):
    """Ativar usuário - exclusivo para caixa"""
    if not current_user.is_caixa():
        flash('Acesso negado. Apenas caixa pode ativar usuários.', 'error')
        return redirect(url_for('auth.dashboard'))
    
    success, result = Usuario.ativar_usuario(usuario_id)
    
    if success:
        flash(f'Usuário ativado com sucesso!', 'success')
    else:
        flash(f'Erro ao ativar usuário: {result}', 'error')
    
    return redirect(url_for('auth.gerenciar_usuarios'))

@auth_bp.route('/remover-usuario/<int:usuario_id>', methods=['POST'])
@login_required
def remover_usuario(usuario_id):
    """Remover permanentemente um usuário - exclusivo para caixa"""
    if not current_user.is_caixa():
        flash('Acesso negado. Apenas caixa pode remover usuários.', 'error')
        return redirect(url_for('auth.dashboard'))
    
    # Não permitir remover a si mesmo
    if usuario_id == current_user.id:
        flash('Você não pode remover sua própria conta.', 'error')
        return redirect(url_for('auth.gerenciar_usuarios'))
    
    success, result = Usuario.remover_usuario(usuario_id)
    
    if success:
        flash(result, 'success')
    else:
        flash(f'Erro ao remover usuário: {result}', 'error')
    
    return redirect(url_for('auth.gerenciar_usuarios'))
