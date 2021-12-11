# Data Centric Development – Kris Dikkeschei

This is my Data Centric Development project. It's my 3rd milestone project for Code Institute. I came on the idea of Football League Database because I am always curious to look back to sport results in the past. Now it will be possible to get a database for that.
Click [here][DEMO] for my deployed project hosted on Heroku.

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
I created a wireframe using the program:


![front page](https://github.com/Kriz-hub/Football_League_Database/blob/main/static/wireframes/page%201%20home%20small.png) 

![Page2](https://github.com/Kriz-hub/Football_League_Database/blob/main/static/wireframes/page%202%20small.png) ![Page3](https://github.com/Kriz-hub/Football_League_Database/blob/main/static/wireframes/page%203%20small.png) 

![Page4](https://github.com/Kriz-hub/Football_League_Database/blob/main/static/wireframes/page%204%20small.png) ![Page5](https://github.com/Kriz-hub/Football_League_Database/blob/main/static/wireframes/page%205%20small.png)



## Technologies

### Languages
* HTML5
* CSS3
* Javascript
* Python3

### Libraries
* Materialize
* FontAwesome
* jQuery
* Dnspython
* Flask
* Flask-PyMongo
* PyMongo

### Database
* MongoDB

### Hosting
* Github
* Heroku

**Testing**

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
| When clicked on "Edit" on a created club that same input field should appear again with the old name, this can be altered to a (slightly) different name. | No errrors. Works.|        |    :----:   |
| When clicked on "Delete" on a created club a warning should come with a list of matches where this deleted club appears in. When pressed "Delete Club Name" all these shown matches should be deleted also.     | No errrors. Works.|        |    :----:   |

**After pressing "Leagues" on the navigation bar:**
| Test      | Result | 
| :---        |    :----:   |
| After pressing "Leagues" and "Add Leagues", an input field should appear with an input of a minimal 3 characters and a maximum of 25, when filled in less then 3 characters this can't be submitted. When submitted with the button "Add League" that new league name appear on the screen in a rectangle box.| No errrors. Works.|        |    :----:   |
| When clicked on "Edit" on a created league that same input field should appear again with the old name, this can be altered to a (slightly) different name . | No errrors. Works.|        |    :----:   |
| When clicked on "Delete" on a created league a warning should come with a list of matches in this league. When pressed "Delete League Name" all these shown matches should be deleted also.     | No errrors. Works.|        |    :----:   |

**After pressing "Matches" on the navigation bar:**
| Test      | Result | 
| :---        |    :----:   |
| When clicked on "Matches' rectangles with league names should appear if they are added. When not added or when not clubs are added matches can't be made.    | No errrors. Works.|        |    :----:   |
| When clicked on a league on the button "Show and Edit Matches" all created matches appear with an "Edit" button and a "DEL" button. On this page should also appear an "Add Matches" button on the top | No errrors. Works.|        |    :----:   |
| When clicked on "Add Matches" an input form should appear, with Date input, Club1, Club2, Score1, Score2, this form should be validated, when some part aren't filled in it can't be submitted. | No errrors. Works.|        |    :----:   |
| "Club1" and "Club2" are dropdown menus where clubs can be choosen which are filled in at the "Home" area.        | No errrors. Works.|        |    :----:   |
| "Date Input" should be filled in with a calendar device which appear when pressed on.     | No errrors. Works.|        |    :----:   |
| The Form should me submitted when pressed on the button "Add Match". Now the match should be added and the page should return to the beginning of the "Matches" area     | No errrors. Works.|        |    :----:   |
| When pressed "Edit" on existing matches the form should appear with filled in values, and with the same validation rules when pressed on "Add Matches" in the "Matches" area    | No errrors. Works.|        |    :----:   |
| When clicked on "Delete" on existing matches a warning should come that the match is about to be erased. When pressed on the button "Delete Match" this match should be deleted.     | No errrors. Works.|        |    :----:   |

**After pressing "Rankings" on the navigation bar:**
| Test      | Result | 
| :---        |    :----:   |
 When clicked on "Rankings' rectangles with league names should appear if they are added. When not added or when not matches are added rankings can't be made.      | No errrors. Works.|        |    :----:   |
| When clicked on a league on the button "Show ranking" an internal count should be made when matches are filled in. According to FIFA football rules clubs get 3 points when they win and get 1 point when the loose. When clubs have the same point amount the goal difference determines the result of the ranking. This ranking should be displayed. |  No errrors. Works.|        |    :----:   |

**After pressing "Help" on the navigation bar:**
| Test      | Result | 
| :---        |    :----:   |
| When clicked on "Help" a help page should appear with info    | No errrors. Works.|        |    :----:   |
