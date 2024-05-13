from flask import Flask, render_template, request, redirect, session, url_for, flash, current_app, jsonify
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_principal import Principal, Permission, RoleNeed, identity_loaded, UserNeed, Identity, identity_changed, AnonymousIdentity
from db import conexion
import create_controllers
import read_controllers
import controller_person
import update_controller
from flask_mail import Mail, Message
import os
from config import config

from models.ModelUser import ModelUser

from models.entities.User import User


app = Flask(__name__, template_folder='templates')
db = MySQL(app)
principals = Principal(app)
login_manager_app = LoginManager(app)
voluntario_permission = Permission(RoleNeed('voluntario'))
donador_permission = Permission(RoleNeed('donador'))
admin_permission = Permission(RoleNeed('admin'))
receptor_permission = Permission(RoleNeed('receptor'))

app.config['UPLOAD_FOLDER'] = 'statci/img'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'donappetite5@gmail.com'
app.config['MAIL_PASSWORD'] = 'gevh qlbt smcy tlku'

rol = None
carnet = None

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index_main.html', current_user = current_user)

@app.route('/recuperar_contraseña')
def recuperar():
    return render_template('olvide_contraseña.html')

@app.route('/olvide_contraseña', methods=['POST', 'GET'])
def enviar_correo():
    
    if request.method == 'POST' and 'correo' in request.form:
        correo = request.form['correo']
        
        cur=conexion().cursor()
        cur.execute('SELECT * FROM usuario WHERE correo = %s',(correo))
        account = cur.fetchone()

        if account:
            msg = Message('Restablecer contraseña', sender='donappetite5@gmail.com', recipients=[correo])
            msg.body = f'Recupera tu contraseña ingresando a este link: http://127.0.0.1:5000/restablecer/{correo}'
            mail.send(msg)
            return redirect('/')
        
@app.route('/restablecer/<correo>', methods=['POST', 'GET'])
def render_res():
    render_template('restablecer.html')

@app.route('/restablecer/<correo>', methods=['POST', 'GET'])
def restablcer(correo):
    password = request.form['password']
    correo = correo
    cur=conexion().cursor()
    cur.execute('SELECT * FROM usuario WHERE correo = %s',(correo))
    account = cur.fetchone()
    
    if account:
        update_controller.actualizar_pass(password, correo)
    return redirect('/')
#REGISTRO

@app.route('/registrate')
def registrate():
    return render_template('tipo_usuario.html')

@app.route('/voluntario')
def reg_voluntario():
    return render_template('form_persona_vol.html')

@app.route('/voluntario_user')
def reg_voluntario_user():
    return render_template('form_voluntario.html')

@app.route('/user')
def reg_user():
    global rol
    return render_template('form_user.html', rol = rol)

@app.route('/receptor')
def tipo_receptor():
    global rol
    rol = 'receptor'
    return render_template('tipo_receptor.html')

@app.route('/receptor_organizacion')
def reg_receptor_org():
    return render_template('form_receptor.html')

@app.route('/encargado')
def reg_encargado():
    return render_template('form_persona.html')

@app.route('/receptor_natural')
def reg_receptor_nat():
    return render_template('form_persona.html')

@app.route('/donador')
def tipo_donador():
    global rol
    rol = 'donador'
    return render_template('tipo_donador.html')

@app.route('/donador_organizacion')
def reg_donador_org():
    return render_template('form_donador.html')

@app.route('/donador_natural')
def reg_donador_nat():
    return render_template('form_persona.html')



#personas

@app.route('/guardar_voluntario', methods=['POST', 'GET'])
def reg_persona_vol():
    global carnet
    carnet = request.form['ci']
    ci = request.form['ci']
    nombre = request.form['nombre']
    paterno = request.form['apepaterno']
    materno = request.form['apematerno']
    celular = request.form['cel']
    naci = request.form['naci']
    direccion = request.form['direccion']
    sexo = request.form['sexo']
    
    create_controllers.crear_persona(ci, nombre, paterno, materno, celular, naci, direccion, sexo)
    return redirect('/voluntario_user')

@app.route('/guardar_persona', methods=['POST', 'GET'])
def register_persona():
    global carnet
    carnet = request.form['ci']
    ci = request.form['ci']
    nombre = request.form['nombre']
    paterno = request.form['apepaterno']
    materno = request.form['apematerno']
    celular = request.form['cel']
    naci = request.form['naci']
    direccion = request.form['direccion']
    sexo = request.form['sexo']
    
    create_controllers.crear_persona(ci, nombre, paterno, materno, celular, naci, direccion, sexo)
    return redirect('/user')

@app.route('/guardar_user_vol', methods=['POST', 'GET'])
def registrar_user_vol():
    rol = request.form['rol']
    nom_user = request.form['nom_user']
    correo = request.form['correo']
    password = request.form['password']
    r_password = request.form['r_password']
    horario = request.form['horario']
    
    create_controllers.crear_voluntario(rol, nom_user, correo, password, r_password, horario, carnet)
    return redirect('/')

@app.route('/guardar_user', methods=['POST', 'GET'])
def registrar_user():
    rol = request.form['rol']
    nom_user = request.form['nom_user']
    correo = request.form['correo']
    password = request.form['password']
    r_password = request.form['r_password']
    
    create_controllers.crear_usuario(rol, nom_user, correo, password, r_password, carnet)
    return redirect('/')

@app.route('/guardar_org', methods=['POST', 'GET'])
def registrar_org():
    nom_org = request.form['nom_org']
    tipo_org = request.form['tipo_org']
    departamento = request.form['departamento']
    contacto = request.form['contacto']
    
    create_controllers.crear_org(nom_org, tipo_org, departamento, contacto, carnet)
    return redirect('/encargado')

@app.route('/donar')
@login_required
@donador_permission.require()
def donar():
    if 'donacion' not in session:
        session['donacion'] = []
    else:
        session.pop('donacion',  None)
    return render_template('form_donacion.html')

@app.route('/alimentos', methods = ['GET'])
def mostrar_alimentos():
    alimentos = read_controllers.obtener_alimentos()
    indices = range(len(alimentos))
    return render_template('inventarioGaleria.html', alimentos = alimentos, indices = indices)

@app.route('/personas', methods = ['GET'])
def mostrar_personas():
    personas = read_controllers.obtener_personas()
    return render_template('personas.html', personas = personas)

# @app.route("/eliminar_persona", methods=["POST"])
# def eliminar_persona():
#     controller_person.eliminar_persona(request.form["ci"])
#     return redirect("/personas")

# @app.route("/formulario_editar_persona/<int:ci>")
# def editar_persona(id):
#     persona = controller_person.obtener_persona_por_id(id)
#     return render_template("editar_persona.html", persona=persona)

#Organizacion
@app.route('/organizaciones', methods = ['GET'])
def mostrar_organizaciones():
    orgs = read_controllers.obtener_orgs()
    return render_template('organizaciones.html', orgs = orgs)



@app.route('/login')
def mostrar_login():
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def user_dashboard():
    if current_user.rol == 'voluntario':
        return redirect(url_for('vol_dashboard'))
    elif current_user.rol == 'donador':
        return redirect(url_for('donador_dashboard'))
    elif current_user.rol == 'receptor':
        return redirect(url_for('receptor_dashboard'))
    elif current_user.rol == 'admin':
        return redirect(url_for('admin_dashboard'))

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

@app.route('/acceso-login', methods=["GET","POST"])
def login():

    if request.method == 'POST':
        user = User(0, '', '', request.form['txtCorreo'], request.form['txtPassword'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                identity_changed.send(current_app._get_current_object(), identity=Identity(logged_user.id))
                return redirect(url_for('user_dashboard'))
            else:
                flash("Contraseña Invalida")
                return render_template('login.html')
        else:
            flash("Usuario no encontrado")
            return render_template('login.html')
    else:
        return render_template('login.html')

@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    identity.user = current_user
    identity.provides.add(RoleNeed(current_user.rol))

@app.route('/logout')
def logout():
    logout_user()
    
    for key in ('identity.name', 'identity.auth_type'):
        session.pop(key, None)
        session.clear()

    #identity_changed.send(current_app._get_current_object(), identity=AnonymousIdentity())
    return redirect(url_for('login'))

@app.errorhandler(403)
def forbidden(error):
    return render_template('403.html'), 403

def status_401(error):
    return redirect(url_for('mostrar_login'))

from flask_principal import PermissionDenied

@app.errorhandler(PermissionDenied)
def handle_permission_denied(e):
    return render_template('403.html'), 403

@app.route('/admin_dashboard')
@login_required
@admin_permission.require()
def admin_dashboard():
    solicitudes = read_controllers.obtener_solicita()
    donas = read_controllers.obtener_realiza()
    tareas = read_controllers.obtener_actividad()
    vols = read_controllers.obtener_voluntario()
    return render_template('adminDashboard.html', solicitudes = solicitudes, donas = donas, tareas = tareas, vols = vols)


@app.route('/user_control')
@login_required
def user_control():
    usuarios = read_controllers.obtener_users()
    return render_template('adminUsuario.html', usuarios = usuarios)

@app.route('/inv_control')
@login_required
def inv_control():
    alimentos = read_controllers.obtener_alimentos()
    return render_template('adminInventario.html', alimentos = alimentos)

def guardar_alim(prod):
    nom = prod['nombre']
    desc = prod['desc']
    cat = prod['cat']
    fecha_ven = prod['fecha_ven']
    peso = prod['peso']
    estado = prod['estado']
    stock = prod['stock']
    tipon = prod['imagen']
    return create_controllers.crear_alim_inv(nom, desc, cat, fecha_ven, tipon, peso, estado, stock)

@app.route('/recibe_donacion', methods = ['POST'])
@login_required
@donador_permission.require()
def guardar_donacion():
    data = request.json
    if 'donacion' not in session:
        session['donacion'] = []
    session['donacion'] = data
    iddona = create_controllers.crear_donacion("entrada")
    
    idact = create_controllers.crear_actividad("Recojo de Donación y almacenaje en inventario", "recojo", "por asignar")

    create_controllers.crear_realiza(current_user.id, iddona, idact)

    ids = []
    alims = session['donacion']
    for prod in alims:
        id = guardar_alim(prod)
        datos = {
            'id' : id,
            'cant' : prod['stock']
        }
        ids.append(datos)

    for row in ids:
        create_controllers.crear_contiene(iddona, row['id'], row['cant'])

    return jsonify({'message': 'Datos recibidos correctamente'})

@app.route('/donador_dashboard')
@login_required
@donador_permission.require()
def donador_dashboard():
    donas = read_controllers.obtener_realiza()
    return render_template("donadorDashboard.html", donas = donas)

@app.route('/solicitud')
@login_required
@receptor_permission.require()
def solicitud():
    alimentos = read_controllers.obtener_alimentos()
    indices = range(len(alimentos))
    return render_template('form_solicitud.html', alimentos = alimentos, indices = indices)


@app.route('/recibe_sol', methods = ['POST'])
@login_required
@receptor_permission.require()
def recibe_sol():
    data = request.json
    if 'solicitud' not in session:
        session['solicitud'] = data
        
    session['iddona'] = create_controllers.crear_donacion("salida")
    
    idact = create_controllers.crear_actividad("Entrega de la donacion", "entrega", "por asignar")

    create_controllers.crear_solicitud(current_user.id, session['iddona'], idact)

    alims = session['solicitud']
    for prod in alims:
        create_controllers.crear_contiene(session['iddona'], prod['idalim'], prod['cantidad'])

    return redirect(url_for('receptor_dashboard'))

@app.route('/receptor_dashboard')
@login_required
@receptor_permission.require()
def receptor_dashboard():
    solicitudes = read_controllers.obtener_solicita()
    return render_template("receptorDashboard.html", solicitudes = solicitudes)


@app.route('/vol_dashboard')
@login_required
@voluntario_permission.require()
def vol_dashboard():
    tareas = read_controllers.obtener_actividad_id(current_user.id)
    return render_template("voluntarioDashboard.html", tareas = tareas)

@app.route('/contenido_donacion', methods = ['GET'])
@login_required
def mostrar_contenido():
    id = session['iddona']
    alimentos = read_controllers.obtener_contenido_donacion(id)
    indices = range(len(alimentos))
    return render_template('mostrarProductos.html', alimentos = alimentos, indices = indices)

@app.route('/contenido/<int:id>', methods = ['GET'])
@login_required
def contenido(id):
    alimentos = read_controllers.obtener_contenido_donacion(id)
    indices = range(len(alimentos))
    return render_template('mostrarProductos.html', alimentos = alimentos, indices = indices)

@app.route('/asigna_tareas', methods = ['POST', 'PUT'])
@login_required
@admin_permission.require()
def asigna_tareas():
    datas = request.json
    for data in datas:
        update_controller.actualizar_actividad(data['actividad'], current_user.id, data['voluntario'], 'por recoger')
    return redirect(url_for('user_dashboard'))

@app.route('/vol_dashboard/<int:id>', methods = ['GET', 'POST', 'PUT'])
@login_required
@voluntario_permission.require()
def tarea_hecha(id):
    update_controller.actualizar_estado_actividad(id, 'completada')
    return redirect(url_for('vol_dashboard'))

@app.route('/ubicacion', methods = ['GET', 'POST'])
@login_required
def ubicacion():
    return render_template('mapa.html')


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.secret_key='12345'
    app.register_error_handler(401, status_401)
    app.run(debug=True)