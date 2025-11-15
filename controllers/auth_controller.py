from flask import Blueprint, request, jsonify, current_app  
import logging

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

VALID_USERNAME = "stephen" # AT VAUGHKET HENDE?!
VALID_PASSWORD = "shetkatalagaballabyu" 

@auth_bp.route("/login", methods=["POST"])
def login():
    if not request.is_json:
        current_app.logger.warning("Login failed: Non-JSON request received")
        return jsonify({"error": "Request must be in JSON format"}), 400

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    current_app.logger.info(f"Login attempt by user: {username}")

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        current_app.logger.info(f"Login successful for user: {username}")
        return jsonify({"message": "Login successful!"}), 200
    else:
        current_app.logger.warning(f"Login failed for user: {username}")
        return jsonify({"error": "Invalid username or password"}), 401
