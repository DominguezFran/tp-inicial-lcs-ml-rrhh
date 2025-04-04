from flask import Blueprint, request, jsonify
from app.models.Candidato import Candidato
from app import db

bp = Blueprint('main', __name__)

@bp.route('/candidatos', methods=['GET'])
def obtener_candidatos():
    candidatos = Candidato.query.all()
    return jsonify([c.to_dict() for c in candidatos])

@bp.route('/candidatos', methods=['POST'])
def agregar_candidato():
    data = request.get_json()

    nuevo = Candidato(
        nombre=data['nombre'],
        esApto=data['esApto']
    )

    db.session.add(nuevo)
    db.session.commit()
    return jsonify(nuevo.to_dict()), 201
