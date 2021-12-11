# Data Centric Development – Kris Dikkeschei

This is my Data Centric Development project. It's my 3rd milestone project for Code Institute. I came on the idea of Football League Database because I am always curious to look back to sport results in the past. Now it will be possible to get a database for that.
Click [HERE](https://football-league-database.herokuapp.com) for my deployed project hosted on Heroku.


## User stories
* As a user : As a new visitor to the Football League Database, I want the page to be easily navigated.
* As a user: As a new visitor I want clear instructions on how to add, view, update matches.
* As a user: I want a web app that responds quickly to my interaction.
* As a user: I want also good access on smaller devices.


## Strategy
* The goal of the website is to provide the visitor the option to create their own database of matches and organize them to get it displayed in a ranking list
* The user is allowed to add, delete and edit clubs, leagues and matches.
* When club names are changed, the database as a whole will be searched to get the ranking list updated
* When club or league is deleted a warning is shown that all references will be deleted as well. Those references are all shown so the user can see what the consequences are.


## Database
* The database chosen for this is a non-relational database hosted on MongoDB Atlas.
* The web application uses 3 database collections, 'Clubs', Leagues and 'Matches'.


## Skeleton
I created a wireframe using the program [Balsamic Wireframes](https://balsamiq.com):

![front page](https://github.com/Kriz-hub/Football_League_Database/blob/main/static/wireframes/page%201%20home%20small.png) 

![Page2](https://github.com/Kriz-hub/Football_League_Database/blob/main/static/wireframes/page%202%20small.png) ![Page3](https://github.com/Kriz-hub/Football_League_Database/blob/main/static/wireframes/page%203%20small.png) 

![Page4](https://github.com/Kriz-hub/Football_League_Database/blob/main/static/wireframes/page%204%20small.png) ![Page5](https://github.com/Kriz-hub/Football_League_Database/blob/main/static/wireframes/page%205%20small.png)


## Surface
* The colors of my website are black, white (rgb(228, 230, 221)) with red/orange color. Materialize calls that "deep-orange darken-4"
* For the background picture I was looking for a football related picture with red colors in it. When I found the picture of the Wembley Stadium it nearly felt good, after I saw a method to bring the background back to half opacity it was right for me. The background color itself is dark red (rgb(37, 0, 0));
* The HTML site is build with Materialize code.
* I choosed "Roboto" for my text on the website, Arial for the Help Section.


## Technologies

*Languages*
* HTML5
* CSS3
* Javascript
* Python3

*Libraries*
* Materialize
* FontAwesome
* jQuery
* Dnspython
* Flask
* Flask-PyMongo
* PyMongo

*Database*
* MongoDB

*Hosting*
* Github
* Heroku

## Features
The website has been built with a mobile-first approach and is responsive. This is achieved by using the front end framework from Materialize and custom-written css.

## CRUD functions

**Users can create Clubs, Leagues and Matches to the database. (Create)**
* In the area "Clubs" and "Leagues" allows the user to create those.
* The area of "Matches" allows the user to enter fields Date, Club1, Club2, Score Club1, Score Club2 to create a match

**Users can browse through all Clubs, Leagues and Matches contained in the database. (Read)**
* The areas "Clubs" and "Leagues" and "Matches" allows the user to look back all of them what is added.

**Users can edit Clubs, Leagues and Matches in the database. (Update)**
* In the area "Clubs" and "Leagues" allows the user to click on the created item to alter there names.
* The area of "Matches" allows the user to later fields Date, Club1, Club2, Score Club1, Score Club2 when he clicks on an existing match.

**Users can delete Clubs, Leagues and Matches in the database. (Delete)**
* In all areas items can be deleted, all match items can be deleted as well when the erasing have effect on those items. For example when a league is deleted, all matches which are related have to be deleted as well.


## Challenge
At a certain moment I discovered that I couldn't edit or delete anything from MongoDB anymore. I was considering to do a complete new signing in to Mongo. When I talked about that with mentor Marcel he looked a little bit to the code, there he discovered that the problem was in these codes: "mongo.db.update", "mongo.db.remove", the ones who are used in the miniproject. When it was replaced by "mongo.db.matches.update_one", "mongo.db.clubs.delete_one", everything worked again.


## Testing

**All testing carried out was done manually**
**Testing General:**
| Test      | Result | 
| :---        |    :----:   |   
| Navbar links and homepage     | No errrors. Works.|        |    :----:   |
| Drag out menu when smaller devices  are used  | No errrors. Works.|        |    :----:   |

**After pressing "Home" on the navigation bar:**
| Test      | Result | 
| :---        |    :----:   |
| After pressing "Home" and "Add Clubs", an input field should appear with an input of a minimal 3 characters and a maximum of 12, when filled in less then 3 characters this can't be submitted. When submitted with the button "Add Club" that new club name appear on the screen in a rectangle box.| No errrors. Works.|        |    :----:   |
| When clicked on "Edit" on a created club, that same input field should appear again with the old name, this can be altered to a (slightly) different name. | No errrors. Works.|        |    :----:   |
| When clicked on "Delete" on a created club, a warning should come with a list of matches where this deleted club appears in. When pressed "Delete Club Name" all these shown matches should be deleted also.     | No errrors. Works.|        |    :----:   |

**After pressing "Leagues" on the navigation bar:**
| Test      | Result | 
| :---        |    :----:   |
| After pressing "Leagues" and "Add Leagues", an input field should appear with an input of a minimal 3 characters and a maximum of 25, when filled in less then 3 characters this can't be submitted. When submitted with the button "Add League" that new league name appear on the screen in a rectangle box.| No errrors. Works.|        |    :----:   |
| When clicked on "Edit" on a created league, that same input field should appear again with the old name, this can be altered to a (slightly) different name . | No errrors. Works.|        |    :----:   |
| When clicked on "Delete" on a created league, a warning should come with a list of matches in this league. When pressed "Delete League Name" all these shown matches should be deleted also.     | No errrors. Works.|        |    :----:   |

**After pressing "Matches" on the navigation bar:**
| Test      | Result | 
| :---        |    :----:   |
| When clicked on "Matches' rectangles with league names should appear if they are added. When not, the area remains empty so no matches can be made.    | No errrors. Works.|        |    :----:   |
| When clicked on a league on the button "Show and Edit Matches" all created matches appear with an "Edit" button and a "DEL" button. On this page should also appear an "Add Matches" button on the top | No errrors. Works.|        |    :----:   |
| When clicked on "Add Matches" an input form should appear, with Date input, Club1, Club2, Score1, Score2, this form should be validated, when some part aren't filled in it can't be submitted. | No errrors. Works.|        |    :----:   |
| "Club1" and "Club2" are dropdown menus where clubs can be choosen which are filled in at the "Home" area.        | No errrors. Works.|        |    :----:   |
| When clubs are not added this drop down menus remains empty so no submitting of the form is possible.        | No errrors. Works.|        |    :----:   |
| "Date Input" should be filled in with a calendar device which appear when pressed on.     | No errrors. Works.|        |    :----:   |
| The Form should me submitted when pressed on the button "Add Match". Now the match should be added and the page should return to the beginning of the "Matches" area.     | No errrors. Works.|        |    :----:   |
| When pressed "Edit" on existing matches the form should appear with filled in values, and with the same validation rules when pressed on "Add Matches" in the "Matches" area    | No errrors. Works.|        |    :----:   |
| When clicked on "Delete" on existing matches a warning should come that the match is about to be erased. When pressed on the button "Delete Match" this match should be deleted.     | No errrors. Works.|        |    :----:   |

**After pressing "Rankings" on the navigation bar:**
| Test      | Result | 
| :---        |    :----:   |
 When clicked on "Rankings', rectangles with league names should appear if they are added.       | No errors. Works.|        |    :----:   |
| When clicked on a league on the button "Show ranking" an internal count should be made when matches are filled in. According to FIFA football rules clubs get 3 points when they win and get 1 point when the loose. When clubs have the same point amount the goal difference determines the result of the ranking. This ranking should be displayed. |  No errrors. Works.|        |    :----:   |
|When clicked on a league on the button "Show ranking", but there are no matches added, this ranking area stays empty    | No errors. Works.|        |    :----:   |

**After pressing "Help" on the navigation bar:**
| Test      | Result | 
| :---        |    :----:   |
| When clicked on "Help" a help page should appear with info    | No errors. Works.|        |    :----:   |


## Responsive design
Football League Database is tested on the Chrome browser and on multiple virtual mobile devices (iPhone 5, 6, 7, 8, iPad, Ipad-pro, Iphone X, Moto G4, Galaxy S5, Pixel 2 and Pixel2XL) by "inspect" to ensure compatibility and responsiveness. The actual Samsung S7 and A51 didn't give anomalies.


## Features Left to Implement
Going forward I would like to implement the following features:
* Login and registration feature: Enabling users to create an account and log in.
* Storing user data, so the data is owned by one and can not be latered by many.
* There is a bug that a club can play against itself in the "Matches" area, when filling in the forms. That should be fixed as well.
* It's also possible to create identical clubs and leagues, that could also made better.

## Deployment

The project is stored in a [GitHub repository](https://github.com/Kriz-hub/Football_League_Database) and hosted on Heroku.

I followed the next steps to deploy Football_League_Database on the GitHub pages:

* Log into GitHub.
* Select kriz-hub/Football_Leage_Database in the repository list.
* Go to Settings
* Scroll down to the GitHub Pages section.
* Select the Master Branch
* On selecting Master Branch the page is automatically refreshed.
* The link can be retrieved to the deployed website

I followed the next steps to host this app on Heroku:

* Created a new application using the Heroku dashboard.
* Go to settings tab, click on 'reveal config vars' and add config vars such as IP (0.0.0.0), PORT (5000), MongoDB Name, MongoDB URI (URL with DB name and password).
* Log into Heroku via the gitpod terminal using 'heroku login -i' and follow the on screen instructions to log in.
* Create a requirements.txt using 'pip3 freeze > requirements.txt'.
* Create a Procfile using 'echo web: python app.py > Procfile'.
* Connect GitHub to Heroku in deployment method in Heroku
* Deploy project to Heroku in the Gitpod terminal using 'git push heroku main'.
* Open app in Heroku, succesfully deployed app.


## Credits

**Content**
* The text content on the website was written by me.
* The stadium image of Wembley was obtained from Google Images.
* Making the background with a lower opacity: https://www.digitalocean.com/community/tutorials/how-to-change-a-css-background-images-opacity

## Acknowledgements
I got inspiration from The Data Centric Development mini project from the Code Institute Course: building a taskmanager application.

I want to thank mentor Marcel for the tips he gave and the guiding through this project.


