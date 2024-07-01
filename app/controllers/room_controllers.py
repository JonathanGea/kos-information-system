from app import app
from flask import render_template, redirect, url_for, request, jsonify
from app.utils.auth import login_required
from app.service.room_service  import RoomService   

room_service = RoomService()

@app.route('/api/room', methods=["GET"])
@login_required
def room():
    rooms = room_service.list_rooms()
    return jsonify({"message": "SUKSSES", "data" : rooms}), 200

@app.route('/api/room', methods=["POST"])
@login_required
def add_room():
    if request.method != 'POST':
        return jsonify({"message": "Method not allowed"}), 405

    name = request.form['name']
    
    if not name:
        return jsonify({"message": "Room name is required"}), 400

    room = room_service.add_room(name)
    if room:
        return jsonify({"message": "Room created successfully", "room": room}), 201

    return jsonify({"message": "Failed to add room"}), 500

@app.route('/api/room/<int:id>', methods=["PATCH"])
@login_required
def deactivate_room(id):
    room = room_service.deactivate_room(id)
    if room:
        return jsonify({"message": "Room deactivated successfully", "room": room}), 200

    return jsonify({"message": "Failed to deactivate room"}), 500

@app.route('/api/room/<int:id>', methods=["PUT"])
@login_required
def edit_room(id):
    new_name = request.form['new_name']
    
    if not new_name:
        return jsonify({"message": "New room name is required"}), 400

    room = room_service.edit_room(id, new_name)
    if room:
        return jsonify({"message": "Room updated successfully", "room": room}), 200

    return jsonify({"message": "Failed to update room"}), 500
