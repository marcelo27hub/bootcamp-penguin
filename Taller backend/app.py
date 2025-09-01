from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tareas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    prioridad = db.Column(db.String(20), nullable=True)
    fecha_inicio = db.Column(db.String(20), nullable=True)
    fecha_fin = db.Column(db.String(20), nullable=True)
    estado = db.Column(db.String(20), nullable=True)

with app.app_context():
    db.create_all()  # Crea la base de datos si no existe

@app.route('/', methods=['GET'])
def home():
    tareas = Tarea.query.all()
    return render_template('index.html', tareas=tareas)

@app.route('/tarea', methods=['POST'])
def manejar_tarea():
    accion = request.form.get('accion')
    tarea_id = request.form.get('id')

    if accion == 'agregar':
        nueva = Tarea(
            titulo=request.form.get('titulo'),
            descripcion=request.form.get('descripcion'),
            prioridad=request.form.get('prioridad'),
            fecha_inicio=request.form.get('fecha_inicio'),
            fecha_fin=request.form.get('fecha_fin'),
            estado=request.form.get('estado')
        )
        db.session.add(nueva)
        db.session.commit()

    elif accion == 'editar' and tarea_id:
        tarea = Tarea.query.get(tarea_id)
        tareas = Tarea.query.all()
        return render_template('index.html', tareas=tareas, tarea_editando=tarea)

    elif accion == 'actualizar' and tarea_id:
        tarea = Tarea.query.get(tarea_id)
        if tarea:
            tarea.titulo = request.form.get('titulo')
            tarea.descripcion = request.form.get('descripcion')
            tarea.prioridad = request.form.get('prioridad')
            tarea.fecha_inicio = request.form.get('fecha_inicio')
            tarea.fecha_fin = request.form.get('fecha_fin')  # ← CORREGIDO
            tarea.estado = request.form.get('estado')
            db.session.commit()

    elif accion == 'eliminar' and tarea_id:
        tarea = Tarea.query.get(tarea_id)
        if tarea:
            db.session.delete(tarea)
            db.session.commit()

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)