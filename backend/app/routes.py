from flask import Blueprint, request, jsonify
from app.models import db, Candidato

bp = Blueprint('main', __name__)

#Consulta la tabla Candidato 
@bp.route('/candidatos', methods=['GET'])
def obtener_candidatos():
    candidatos = Candidato.query.all()
    return jsonify([c.to_dict() for c in candidatos])

#Crea un objeto candidato con los datos pasados por json en el formulario
@bp.route('/candidatos', methods=['POST'])
def agregar_candidato():
    datos = request.json
    nuevo_candidato = Candidato(
        nombre=datos['nombre'],
        anios_experiencia=datos['anios_experiencia'],
        habilidades=datos['habilidades'],
        idiomas=datos['idiomas'],
        expectativa_salarial=datos['expectativa_salarial'],
        email=datos['email']
    )
    db.session.add(nuevo_candidato)
    db.session.commit()
    return jsonify({"mensaje": "Candidato agregado"}), 201
