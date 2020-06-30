from flask import Flask, render_template, request, jsonify
from models import Family
import json

app = Flask(__name__)

fam = Family("Jackson")


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/members/", methods=["GET", "POST"])
@app.route("/members/member/<int:id>", methods=["GET", "PUT", "DELETE"])
def members(id=None):

    ####### G E T - M I E M B R O S ########
    if request.method == "GET":

        if id == None:
            miembros = fam.get_all_members()
            return jsonify(miembros), 201

####### G E T - M I E M B R O ########
        if id:
            member = fam.get_member(id)
            if member:
                return jsonify(member), 200
            else:
                return jsonify({"msg": "Miembro no existente"})


####### P O S T - M I E M B R O ########
    if request.method == "POST":

        data = request.get_json()
        for person in fam._members:
            if person["first_name"] == data["first_name"]:
                return jsonify({"msg": f"miembro {data['first_name']} ya existe"}), 400

        if data["first_name"] == None or data["first_name"] == "":
            return jsonify({"Msg": "First_Name no ingresado"})
        if data["age"] == None or type(data["age"]) != int:
            return jsonify({"Msg": "Age no ingresado"})
        if data["lucky_numbers"] == None or len(data["lucky_numbers"]) == 0:
            return jsonify({"Msg": "Lucky Numbers no ingresados"})

        member = {
            "first_name": data["first_name"],
            "age": data["age"],
            "lucky_numbers": data["lucky_numbers"]
        }

        member = fam.add_member(member)
        return jsonify({"msg": "Miembro creado", "member": member}), 201

####### D E L E T E - M I E M B R O ########
    if request.method == "DELETE":
        miembro = fam.get_member(id)
        if not miembro:
            return jsonify({"msg": "Miembro no existe"})
        else:
            fam.delete_member(id)
            return jsonify({"Msg": "Miembro eliminado."})

####### P U T - M I E M B R O ########
    if request.method == "PUT":
        miembro = fam.get_member(id)
        if not miembro:
            jsonify({"msg": "Usuario no existe, no se puede modificar"})

        data= request.get_json()
        if data["first_name"] == None or data["first_name"] == "":
            return jsonify({"Msg": "First_Name no ingresado"})
        if data["age"] == None or type(data["age"]) != int:
            return jsonify({"Msg": "Age no ingresado"})
        if data["lucky_numbers"] == None or len(data["lucky_numbers"]) == 0:
            return jsonify({"Msg": "Lucky Numbers no ingresados"})

        miembro={
            "first_name": data["first_name"],
            "age": data["age"],
            "lucky_numbers": data["lucky_numbers"]
        }
        miembro=fam.update_member(id, miembro)
        return jsonify({"msg": "Miembro editado", "Miembro": miembro}), 201

            


if __name__ == '__main__':
    app.run()


# Otra forma de hacer el post, consiguiendo valor por valor

"""   valor_nombre = request.json.get("first_name")
        valor_edad = request.json.get("age")
        valor_LN = request.json.get("lucky_numbers")
        #datos = request.json_get() Con esto guardo todo lo que esta en el body

        if valor_nombre == None or valor_nombre == "":
            return jsonify({"msg": "Nombre no ingresado"})
        if valor_edad == None or valor_edad == "" or valor_edad <= 0:
            return jsonify({"msg": "Edad no ingresado o no es mayor a 0"})
        if valor_LN == None or valor_LN == "":
            return jsonify({"msg": "Lucky Numbers no ingresados"}) """
