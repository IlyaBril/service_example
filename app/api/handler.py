from flask import jsonify


def dummy_handler():
   return jsonify({"success": True}), 200