@app.route("/api/poem", methods=["POST"])
def poem():

    response = client.responses.create(
        model="gpt-4.1-mini",
        input="Напиши абсурдное четверостишие без смысла."
    )

    return jsonify({"poem": response.output_text})
