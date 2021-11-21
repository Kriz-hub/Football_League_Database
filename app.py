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
global_deleted_matches = "0"
global_last_matchdate = "0"
global_match_id = "0"
global_league_id = "0"

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
            "club_name": request.form.get("club_name"),
        }
        mongo.db.clubs.update({"_id": ObjectId(club_id)}, submit)
        matches = list(mongo.db.matches.find().sort("club1_name", 1))
        for match in matches:
            if match["club1_nr"] == ObjectId(club_id):
                submit = {
                      "league_nr": match ["league_nr"],
                      "club1_nr": match ["club1_nr"],
                      "club2_nr": match ["club2_nr"],
                      "league_name": match ["league_name"],
                      "match_date": match ["match_date"],
                      "club1_name": request.form.get("club_name"),
                      "club2_name": match ["club2_name"],
                      "club1_score": match ["club1_score"],
                      "club2_score": match ["club2_score"]       
                }
                mongo.db.matches.update({"_id": match["_id"]}, submit)
        for match in matches:
            if match["club2_nr"] == ObjectId(club_id):
                submit = {
                      "league_nr": match ["league_nr"],
                      "club1_nr": match ["club1_nr"],
                      "club2_nr": match ["club2_nr"],
                      "league_name": match ["league_name"],
                      "match_date": match ["match_date"],
                      "club1_name": match ["club1_name"],
                      "club2_name": request.form.get("club_name"),
                      "club1_score": match ["club1_score"],
                      "club2_score": match ["club2_score"]       
                }
                mongo.db.matches.update({"_id": match["_id"]}, submit)
        flash("Club Successfully Updated")
        return redirect(url_for("get_clubs"))

    club = mongo.db.clubs.find_one({"_id": ObjectId(club_id)})
    return render_template("clubs_edit.html", club=club)


@app.route("/delete_club_question/<club_id>")
def delete_club_question(club_id):
    global global_deleted_matches
    matches = list(mongo.db.matches.find())
    deleted_matches = matches
    del_match_nr = -1
    for match in matches:
        if (match ["club1_nr"] == ObjectId(club_id)) or (match ["club2_nr"] == ObjectId(club_id)):
           del_match_nr = del_match_nr + 1
           deleted_matches [del_match_nr] = match
    
    for a in range(del_match_nr + 1, len(matches)): 
        deleted_matches.pop(len(deleted_matches)-1)
    global_deleted_matches = deleted_matches
    return render_template("clubs_delete.html", deleted_matches=deleted_matches, club_id=club_id)


@app.route("/delete_club/<club_id>")
def delete_club(club_id):
      global global_deleted_matches
      mongo.db.clubs.remove({"_id": ObjectId(club_id)})
      for match in global_deleted_matches:
         mongo.db.matches.remove({"_id": match ["_id"]})
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
        matches = list(mongo.db.matches.find().sort("league_name", 1))
        for match in matches:
            if match["league_nr"] == ObjectId(league_id):
                submit = {
                      "league_nr": match ["league_nr"],
                      "club1_nr": match ["club1_nr"],
                      "club2_nr": match ["club2_nr"],
                      "league_name": request.form.get("league_name"),
                      "match_date": match ["match_date"],
                      "club1_name": match ["club1_name"],
                      "club2_name": match ["club2_name"],
                      "club1_score": match ["club1_score"],
                      "club2_score": match ["club2_score"]       
                }
                mongo.db.matches.update({"_id": match["_id"]}, submit)
        flash("League Successfully Updated")
        return redirect(url_for("get_leagues"))

    league = mongo.db.leagues.find_one({"_id": ObjectId(league_id)})
    return render_template("leagues_edit.html", league=league)


@app.route("/delete_league_question/<league_id>")
def delete_league_question(league_id):
    global global_deleted_matches
    matches = list(mongo.db.matches.find())
    deleted_matches = matches.copy()
    del_match_nr = -1
    for match in matches:
        if match ["league_nr"] == ObjectId(league_id):
           del_match_nr = del_match_nr + 1
           deleted_matches [del_match_nr] = match
    
    for a in range(del_match_nr + 1, len(matches)): 
        deleted_matches.pop(len(deleted_matches)-1)
    global_deleted_matches = deleted_matches
    return render_template("leagues_delete.html", deleted_matches=deleted_matches, league_id=league_id)


@app.route("/delete_league/<league_id>")
def delete_league(league_id):
      global global_deleted_matches
      mongo.db.leagues.remove({"_id": ObjectId(league_id)})
      for match in global_deleted_matches:
         mongo.db.matches.remove({"_id": match ["_id"]})
      flash("League Successfully Deleted")
      return redirect(url_for("get_leagues"))

@app.route("/get_matches")
def get_matches():
    leagues = list(mongo.db.leagues.find().sort("league_name", 1))
    return render_template("matches.html", leagues=leagues)


@app.route("/manage_matches/<league_id>")
def manage_matches(league_id):
    league = mongo.db.leagues.find_one({"_id": ObjectId(league_id)})
    clubs = list(mongo.db.clubs.find().sort("club_name", 1))
    matches = list(mongo.db.matches.find().sort("match_date", 1))
    global global_league_id 
    global_league_id = ObjectId(league_id)
    return render_template("matches_manage.html", matches=matches, league=league, clubs=clubs)


@app.route("/add_matches", methods=["GET", "POST"])
def add_matches():
    global global_last_matchdate
    global global_league_id 
    if global_last_matchdate == "0":
        matches = list(mongo.db.matches.find())
        if len(matches) > 0:
            match = matches [len(matches)-1]
            last_matchdate = match ["match_date"]
        else:
            last_matchdate = "14 November, 2021"
    else:
        last_matchdate = global_last_matchdate

    match = {
            "match_date": last_matchdate,
            "club1_name": "x",
            "club2_name": "x",
            "club1_score": "x",
            "club2_score": "x",
        }
    
    if request.method == "POST":
        club1 = mongo.db.clubs.find_one({"club_name":  request.form.get("club1_name")})
        club2 = mongo.db.clubs.find_one({"club_name":  request.form.get("club2_name")})
        league = mongo.db.leagues.find_one({"_id": global_league_id })
        match = {
            "league_nr": league ["_id"],
            "club1_nr": club1 ["_id"],
            "club2_nr": club2 ["_id"],
            "league_name": league ["league_name"],
            "match_date": request.form.get("match_date"),
            "club1_name": request.form.get("club1_name"),
            "club2_name": request.form.get("club2_name"),
            "club1_score": request.form.get("club1_score"),
            "club2_score": request.form.get("club2_score")
        }
        
        if match ["club1_name"] == match ["club2_name"]:
            flash("Error: Club's can't have the same name")
            return redirect(url_for("add_matches"))
        else:
          flash("Match Successfully Added")
          global_last_matchdate = request.form.get("match_date")
          mongo.db.matches.insert_one(match)
          return redirect(url_for("get_matches"))
    
    clubs = list(mongo.db.clubs.find().sort("club_name", 1))
    return render_template("matches_add.html", clubs=clubs, match=match)


@app.route("/edit_match/<match_id>", methods=["GET", "POST"])
def edit_match(match_id):
    clubs = list(mongo.db.clubs.find().sort("club_name", 1))
    match = mongo.db.matches.find_one({"_id": ObjectId(match_id)})
    if request.method == "POST":
        club1 = mongo.db.clubs.find_one({"club_name":  request.form.get("club1_name")})
        club2 = mongo.db.clubs.find_one({"club_name":  request.form.get("club2_name")})
        submit = {
            "league_nr": match ["league_nr"],
            "club1_nr": club1 ["_id"],
            "club2_nr": club2 ["_id"],
            "league_name": match ["league_name"],
            "match_date": request.form.get("match_date"),
            "club1_name": request.form.get("club1_name"),
            "club2_name": request.form.get("club2_name"),
            "club1_score": request.form.get("club1_score"),
            "club2_score": request.form.get("club2_score")
        }
        mongo.db.matches.update({"_id": ObjectId(match_id)}, submit)
        flash("Match Successfully Updated")
        return redirect(url_for("get_matches"))
    return render_template("matches_edit.html", match=match, clubs=clubs)  


@app.route("/delete_match/<match_id>")
def delete_match(match_id):
    mongo.db.matches.remove({"_id": ObjectId(match_id)})
    flash("Match Successfully Deleted")
    return redirect(url_for("get_matches"))


@app.route("/get_rankings")
def get_rankings():
    leagues = list(mongo.db.leagues.find().sort("league_name", 1))
    return render_template("rankings.html", leagues=leagues)


@app.route("/show_ranking<league_id>", methods=["GET"])
def show_ranking(league_id):
  if request.method == "GET":
    league = mongo.db.leagues.find_one({"_id": ObjectId(league_id)})
    clubs = list(mongo.db.clubs.find().sort("club_name", 1))
    matches = list(mongo.db.matches.find().sort("match_date", 1))
    nr = -1
    for club in clubs:
       nr = nr + 1
       name = club ["club_name"]
       club = {
           "club_name": name,
           "total_played": 0,
           "total_won": 0,
           "total_draw": 0,
           "total_lost": 0,
           "total_points": 0,
           "total_goals_made": 0,
           "total_goals_against": 0 
       }
       for match in matches:
          if (league["_id"] == match ["league_nr"]) and (club ["club_name"] == match ["club1_name"]): 
             club ["total_played"] = club ["total_played"] + 1
             club ["total_goals_made"] = club ["total_goals_made"] + int(match ["club1_score"])
             club ["total_goals_against"] = club ["total_goals_against"] + int(match ["club2_score"])
             if match ["club1_score"] > match ["club2_score"]:
                 club ["total_won"] = club ["total_won"] + 1
                 club ["total_points"] = club ["total_points"] + 3
             if match ["club1_score"] == match ["club2_score"]:
                 club ["total_draw"] = club ["total_draw"] + 1
                 club ["total_points"] = club ["total_points"] + 1
             if match ["club1_score"] < match ["club2_score"]:
                 club ["total_lost"] = club ["total_lost"] + 1

          if (league["_id"] == match ["league_nr"]) and (club ["club_name"] == match ["club2_name"]): 
             club ["total_played"] = club ["total_played"] + 1
             club ["total_goals_made"] = club ["total_goals_made"] + int(match ["club2_score"])
             club ["total_goals_against"] = club ["total_goals_against"] + int(match ["club1_score"])
             if match ["club2_score"] > match ["club1_score"]:
                 club ["total_won"] = club ["total_won"] + 1
                 club ["total_points"] = club ["total_points"] + 3
             if match ["club2_score"] == match ["club1_score"]:
                 club ["total_draw"] = club ["total_draw"] + 1
                 club ["total_points"] = club ["total_points"] + 1
             if match ["club2_score"] < match ["club1_score"]:
                 club ["total_lost"] = club ["total_lost"] + 1
       clubs [nr]=club
    club_amount = nr + 1
    nr = -1
    nr_sorted = -1
    ranked_clubs = clubs.copy()
    for club in clubs:
        nr = nr + 1
        if club ["total_played"] > 0:
            nr_b = 0
            while_ready = False
            if nr_sorted > -1:
              while (nr_b <= nr_sorted) and (while_ready == False):
                points_a = club ["total_points"]
                ranked_club = ranked_clubs [nr_b]
                points_b = ranked_club ["total_points"]
                goal_diff_a = club ["total_goals_made"] - club ["total_goals_against"]
                goal_diff_b = ranked_club ["total_goals_made"] - ranked_club ["total_goals_against"]
                goals_a = club ["total_goals_made"]
                goals_b = ranked_club ["total_goals_made"]
                if points_a > points_b: 
                  while_ready = True
                else:
                  if (points_a == points_b) and (goal_diff_a > goal_diff_b): 
                    while_ready = True
                  else:
                    if (points_a == points_b) and (goal_diff_a == goal_diff_b) and (points_a>points_b):
                      while_ready = True
                if while_ready == False: nr_b = nr_b + 1
              
              if while_ready == True:
                if nr_b <= nr_sorted:
                  for nr_c in range(nr_sorted + 1, nr_b, -1):
                    ranked_clubs [nr_c] = ranked_clubs [nr_c-1]
                else:
                  nr_b = nr_sorted + 1
              else:
                if nr_b < nr_sorted:
                  for nr_c in range(nr_sorted + 1, nr_b, -1):
                    ranked_clubs [nr_c] = ranked_clubs [nr_c-1]
                else:
                  nr_b = nr_sorted + 1
            nr_sorted = nr_sorted + 1
            ranked_clubs [nr_b] = clubs [nr]  
    b = club_amount - 1
    for a in range(nr_sorted + 1, club_amount): 
        ranked_clubs.pop(b)
        b = b - 1
  return render_template("rankings_show.html", ranked_clubs=ranked_clubs, matches=matches)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)