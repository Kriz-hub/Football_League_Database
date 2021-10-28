import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_clubs")
def get_clubs():
    clubs = list(mongo.db.clubs.find().sort("club_name", 1))
    return render_template("clubs.html", clubs=clubs)


@app.route("/add_clubs", methods=["GET", "POST"])
def add_club():
    if request.method == "POST":
        club = {
            "club_name": request.form.get("club_name")
        }
        mongo.db.clubs.insert_one(club)
        flash("New Club Added")
        return redirect(url_for("get_clubs"))

    return render_template("clubs_add.html")


@app.route("/edit_club/<club_id>", methods=["GET", "POST"])
def edit_club(club_id):
    if request.method == "POST":
        submit = {
            "club_name": request.form.get("club_name")
        }
        mongo.db.clubs.update({"_id": ObjectId(club_id)}, submit)
        flash("Club Successfully Updated")
        return redirect(url_for("get_clubs"))

    club = mongo.db.clubs.find_one({"_id": ObjectId(club_id)})
    return render_template("clubs_edit.html", club=club)


@app.route("/delete_club/<club_id>")
def delete_club(club_id):
    mongo.db.clubs.remove({"_id": ObjectId(club_id)})
    flash("Club Successfully Deleted")
    return redirect(url_for("get_clubs"))
    

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)