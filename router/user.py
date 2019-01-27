from flask import Flask, Blueprint, jsonify, request
from controller import user as dbManager

# sub module
api_users_router = Blueprint('apiUserRouter', __name__, template_folder='')


@api_users_router.route('/api/<api_version>/users', methods=['GET'])
def index(api_version):
    response = dbManager.findAll()
    return jsonify({'data': response, 'api-version': api_version})


@api_users_router.route('/api/<api_version>/users/<int:id>', methods=['GET'])
def show(api_version, id):
    response = dbManager.findById(id)
    return jsonify({'data': response, 'api-version': api_version})


@api_users_router.route('/api/<api_version>/users', methods=['POST'])
def create(api_version):
    body = request.json
    response = dbManager.add(body)
    return jsonify({'data': response, 'api-version': api_version})


@api_users_router.route('/api/<api_version>/users/<int:id>', methods=['DELETE'])
def delete(api_version, id):
    response = dbManager.remove(id)
    return jsonify({'data': response, 'api-version': api_version})


@api_users_router.route('/api/<api_version>/users/<int:id>', methods=['PUT'])
def update(api_version, id):
    body = request.json
    response = dbManager.modify(id, body)
    return jsonify({'data': response, 'api-version': api_version})
