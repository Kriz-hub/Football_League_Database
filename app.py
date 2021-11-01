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


@app.route("/add_leagues", methods=["GET", "POST"])
def add_league():
    if request.method == "POST":
        league = {
            "league_name": request.form.get("league_name")
        }
        mongo.db.leagues.insert_one(league)
        flash("New League Added")
        return redirect(url_for("get_leagues"))

    return render_template("leagues_add.html")


@app.route("/get_leagues")
def get_leagues():
    leagues = list(mongo.db.leagues.find().sort("league_name", 1))
    return render_template("leagues.html", leagues=leagues)

    
@app.route("/edit_league/<league_id>", methods=["GET", "POST"])
def edit_league(league_id):
    if request.method == "POST":
        submit = {
            "league_name": request.form.get("league_name")
        }
        mongo.db.leagues.update({"_id": ObjectId(league_id)}, submit)
        flash("League Successfully Updated")
        return redirect(url_for("get_leagues"))

    league = mongo.db.leagues.find_one({"_id": ObjectId(league_id)})
    return render_template("leagues_edit.html", league=league)


@app.route("/delete_league/<league_id>")
def delete_league(league_id):
    mongo.db.leagues.remove({"_id": ObjectId(league_id)})
    flash("League Successfully Deleted")
    return redirect(url_for("get_leagues"))


@app.route("/get_matches")
def get_matches():
    leagues = list(mongo.db.leagues.find().sort("league_name", 1))
    clubs = list(mongo.db.clubs.find().sort("club_name", 1))
    matches = list(mongo.db.matches.find().sort("league_name", 1))
    return render_template("matches.html", matches=matches, leagues=leagues, clubs=clubs)


@app.route("/add_matches", methods=["GET", "POST"])
def add_matches():
    if request.method == "POST":
        match = {
            "league_name": request.form.get("league_name"),
            "match_date": request.form.get("match_date"),
            "club1_name": request.form.get("club1_name"),
            "club2_name": request.form.get("club2_name"),
            "club1_score": request.form.get("club1_score"),
            "club2_score": request.form.get("club2_score")
        }
        mongo.db.matches.insert_one(match)
        flash("Match Successfully Added")
        return redirect(url_for("get_matches"))

    leagues = list(mongo.db.leagues.find().sort("league_name", 1))
    clubs = list(mongo.db.clubs.find().sort("club_name", 1))
    return render_template("matches_add.html", leagues=leagues, clubs=clubs)


@app.route("/edit_match/<match_id>", methods=["GET", "POST"])
def edit_match(match_id):
    if request.method == "POST":
        submit = {
            "league_name": request.form.get("league_name"),
            "match_date": request.form.get("match_date"),
            "club1_name": request.form.get("club1_name"),
            "club2_name": request.form.get("club2_name"),
            "club1_score": request.form.get("club1_score"),
            "club2_score": request.form.get("club2_score")
        }
        mongo.db.matchs.update({"_id": ObjectId(match_id)}, submit)
        flash("match Successfully Updated")
        return redirect(url_for("get_matchs"))

    match = mongo.db.matches.find_one({"_id": ObjectId(match_id)})
    return render_template("matches_edit.html", match=match)  


@app.route("/delete_match/<match_id>")
def delete_match(match_id):
    mongo.db.matches.remove({"_id": ObjectId(match_id)})
    flash("Match Successfully Deleted")
    return redirect(url_for("get_matches"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)