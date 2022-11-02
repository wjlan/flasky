from flask import Blueprint, jsonify, request, abort, make_response
# request can get the body of the requset
from app import db
from app.models.breakfast import Breakfast
# Now the database is connected and can be interacted



# a class let us to organize routes
breakfast_bp = Blueprint("breakfast", __name__, url_prefix="/breakfast")


@breakfast_bp.route('', methods=['GET'])
def get_all_breakfasts():
    # request object, args allows to get all the arguments at the endpoint after "rating"
    rating_query_value = request.args.get("rating")
    if rating_query_value is not None:
        breakfasts = Breakfast.query.filter_by(rating=rating_query_value)
    else:
        breakfasts = Breakfast.query.all()

    result =[]
    for item in breakfasts:
        result.append(item.to_dict())

    return jsonify(result),200

@breakfast_bp.route('/<breakfast_id>', methods=['GET'])
def get_one_breakfast(breakfast_id):
    chosen_breakfast = get_breakfast_from_id(breakfast_id)
    
    return jsonify(chosen_breakfast.to_dict()), 200

@breakfast_bp.route('', methods=['POST'])
def create_one_breakfast():
    request_body = request.get_json()

    new_breakfast = Breakfast(name=request_body['name'], 
                            rating=request_body['rating'], 
                            prep_time=request_body['prep_time'])


    db.session.add(new_breakfast)
    db.session.commit()

    return jsonify({'msg': f"Successfully created Breakfast with id ={new_breakfast.id}"}), 201


@breakfast_bp.route('<breakfast_id>', methods=['PUT'])
def update_one_breakfast(breakfast_id):
    update_breakfast = get_breakfast_from_id(breakfast_id)

    request_body = request.get_json()

    try:
        update_breakfast.name = request_body["name"]
        update_breakfast.rating = request_body["rating"]
        update_breakfast.prep_time = request_body["prep_time"]
    except KeyError:
        return jsonify({"msg": "Missing needed data"}), 400

    db.session.commit()

    return jsonify({"msg": f"Successfully updated breakfast with id {update_breakfast.id}"}), 200


@breakfast_bp.route('/<breakfast_id>', methods=['DELETE'])
def delete_one_breakfast(breakfast_id):
    breakfast_to_delete = get_breakfast_from_id(breakfast_id)

    db.session.delete(breakfast_to_delete)
    db.session.commit()

    return jsonify({"msg": f"Successfully deleted breakfast with id {breakfast_to_delete.id}"}), 200




def get_breakfast_from_id(breakfast_id):
    try:
        breakfast_id = int(breakfast_id)
    except ValueError:
        return abort(make_response({"message": f"invalid date type: {breakfast_id}"}, 400))
    
    chosen_breakfast = Breakfast.query.get(breakfast_id)
   
    if chosen_breakfast is None:
        return abort(make_response({"message": f"Could not find breakfast item with id {breakfast_id}"}, 404))
    
    return chosen_breakfast










