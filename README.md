![Views and Reviews](https://github.com/Anindita123-code/Milestone3_Data_Centric/blob/master/Design/Readme_header.png)

# Views and Reviews

## Project Overview

The Views and Reviews is a project undertaken as part of Code Institute Diploma Curriculum. This project caters to individuals who loves to Read and share their opinion on Books written by various authors. The reviewers of the books are registered users of the website. This website helps capturing various perspectives on a book which a reader can reference before they decide on having a personal copy of it / buy it. 

This website will provide as a reference for any book buyer, to search for reviews. However, only registered users can post a review. This project has been build using Python and Flask Framework as Backend and MongoDB as the database. More details on follows.
 
## User Experience

### Strategy Plane

The "Views and Reviews" project has been concieved having in mind for the book readers community. Readers / buyers of books almost always like read a short review about the book to understand whether it would be the one of their next reading lists. This website will help the users get a deeper insight into a book, and post a review on any kind of books ranging from story books, Cookery books, Art books, Biographies, Comics and more. Any user can search the website for reviews that might be posted already. 

### Scope Plane

The scope of "Views and Reviews" is capped at the following:
    1. Users will be able to register and thereby login into the website to post a review on any book of their choice
    2. All users will be able to search for books and view a listing of the same. 
    3. Tha Admin user can publish any of the existing reviews as a Featured Review. And will have superuser access to remove any reviews from the website.

* Here, the focus is on reviews posted by user, and hence user management in detail is considered outside the scope of this system. 

### Structure Plane 

The website is structured so that the user can navigate easily and fulfill their goal of either reading reviews or posting a review for any book. A sitemap of the project is enclosed below

![Project Sitemap](https://github.com/Anindita123-code/Milestone3_Data_Centric/blob/master/Design/Sitemap.png?raw=true)

The Data is stored in the Backend. The database being used to store this is MongoDB. The Entity Relationship Diagram is as follows. 

![Entity Relationship Diagram](https://github.com/Anindita123-code/Milestone3_Data_Centric/blob/master/Design/ERDiagram.png)

### Skeleton Plane

The representation of the information of this system is treated differently in different devices. The system uses the rule of three to organize data in accordance with the devices that run the application. The flow of data is depicted as follows:

![Project DFD](https://github.com/Anindita123-code/Milestone3_Data_Centric/blob/master/Design/DFD.png?raw=true)

### User stories

The project aims to address the following user stories
1. As an Admin user, I should be able to create Category / Genre of Books, Edit and Delete this from the database. So that I can have some control on how the books and reviews are organized.
2. As an Admin user, I should be able to mark a review as a featured review which will be displayed on the home page of the website and will be visible to any first time visitor of the site without having to perform a search
3. As an Admin user, I should be able to Edit and Delete information about any Registered User. So that, I can clear up the database for users who has never logged in.
4. As an Admin user, I should be able to Edit and Delete Reviews that has been added by a Registered user of the website. So that I can remove any obnoxious comment written by any reviewer on a book.
5. As a registered user, I should be able to add a review for existing books in the website. So that I do not have to upload duplicate books in for sharing my review.
6. As a registered user, I should be able to add new books to the website and then write a review for it. So that I have the freedom to add new books even if they are not there in the website. 
7. As a registered user, I should be able to view what reviews I have added in my profile page.
8. As a registered user, I should be able to delete or modify the books and reviews that has been added by me.
9. As a guest user, I should be able to read any existing reviews in the website.
10. As a guest user, I should be able to search for reviews on a particular book, book genre, author and content of review. So that I can read any reviews posted in the site
11. As a guest user, I should be able to rate a review after I have read this. So that this is visible to the next reader of the review
12. As user of the website, I should be able to navigate easily through the website, and get appropriate alert messages, when I perform any important action. So that i have a great user experience

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features

Views and Reviews is a book review website and provides its user with the following features. The list of features which have been currently implemented are listed under "Existing Features" and the scope of further enhancements are listed under "Features left to Implement"
 
### Existing Features
- Create a user account (Register) - Any user can create his/her own account which would let him do much more than be able to read reviews in the site.
- Existing users can login - A registered user can login using his userid and password and is routed to their profile page, which has the listing of all the books in the site. 
- Add a book of your choice - A registered user can add a book of their choice, if this is not already available in the listed category of books. 
- Modify and Delete a book - A registered user can modify and delete the record of the book that has been added by them only. Any other book which has not been added by them cannot be modified or deleted by them.
- Add a review - A registered user can add review for any of the books in the site. This new review will be displayed together with all the other reviews for the chosen book
- Edit and Delete review - A registered user can edit or delete any of the reviews that have been posted by them on the books of the website.
- Admin user features - A user who is an admin can log into the website using the userid "admin" and password "admin123". This user will be routed to a different profile page.
- Marking one review as Featured Review by Admin - The admin user will be able to search for a review by date and Publish any one of the review as Featured review on home page Featured Review Section.
- Delete any review by Admin - The admin user will hold the priviledge of deleting any review given by any other user in the website. However.
- Search from Home page - Any user (Registered, unregistered or Admin) will be able to search for books using the search section in the website. The homepage will show up the list of categories below the top nav bar which will allow any user to filter books by categories.
- Logging out - Any logged in user will be able to log out of the website using the logout functionality.
- Change password?? 

### Features Left to Implement
As the number of users grow, There would be additional functionalities that I would look forward to implement.
- Change password with autogenerated email link for verification of the user.
- As the number of Books in the website increases, I would like to implement Pagination for search results and other book and review listing pages
- I would like to have a review and Ratings for the books as part of the reviews which will help a user of the site to gain more insight about the book and its contents. 

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

### Languages
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) for creating the webpages
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) for designing and styling the web pages
- [Python](https://www.python.org/) for the backend development
- [Jinja Templating language](https://jinja.palletsprojects.com/en/2.11.x/) has been used in conjuction with python for the working of the website

### Database
- [MongoDB Atlas](https://www.mongodb.com/) has been used as the primary database for storing and retrieving the information in the website

### Libraries and Frameworks
- [Font Awesome](https://fontawesome.com/) - has been used for the button icons that are used in the website
- [Materialize](https://materializecss.com/) - the various components of materialize has been used to draw the webpage structures and form elements
- [Google Fonts](https://fonts.google.com/) has been used to give the website a uniform look with the help of fonts provided by google
- [JQuery](https://jquery.com) - has been used to simplify DOM manipulation.
- [Flask Framework](https://flask.palletsprojects.com/en/1.1.x/) Jinja and Werkzeug from Flask has been extensively used

### Hosting
- [Github](https://github.com/) has been used for storing the application in public repositories
- [GitPod](https://gitpod.io/workspaces/) has been used as the primary development platform
- [Heroku](https://www.heroku.com/) has been used to host the website

## Testing
As a user selects [Views and Reviews](https://views-and-reviews.herokuapp.com/) he would be directed to the home page of the website.

### Home Page

The following tests have been conducted for the home page:
  
1. The Nav bar links direct the user to the Register, Login and the Search Pages. - All links work and is appropriately redirected
2. I click any of the category buttons below the navbar - This gets me to the book list page, with the listing of the books of the selected category and shows appropriate message
3. There is only one featured review. I can read the Featured Review in Full.. 
4. I click on the "Read More" link and I am redirected to the Review listing page for all reviews given for that book
5. I use the search panel below to search for any book. I select a category and give the name of a book. The book is displayed in the Book list page
6. I click on any of the social links below and I am routed to the respective pages which open up in a separate browser window.
7. I click on the Logo "Views and Reviews" on the upper left hand and I am redirected to the home page from any of the pages of the site

### User Authentication

User authentication involves the following functionalities which have been tested as follows:

1. New User Registration
    * I skip entering username and password in the screen. Message for required fields for Username and Password pops up.
    * I enter a username less than 5 characters and try to register after providing the mandatory fields. I am not allowed to submit as the username doesnot comply with the set pattern.
    * I enter a password less than 5 characters and try to register after providing all the other mandatory fields. I am not allowed to submit as the username doesnot comply with the set pattern.
    * I enter a username and password combination that is already existing in the Database while registering. I am not allowed to create username and a message is displayed "Username / Password already exists"
    * I add valid inputs for username and password which is not a duplicate of any existing username and also fulfills the pattern criteria. I am allowed to Register and "Registration Successful" message is displayed

2. Existing User Login
    * I skip entering the username and/or password in the screen. Mandatory field message is displayed on trying to login.
    * I try to login with a username less than 5 characters. I get a pattern mismatch message from my screen's field.
    * I try to login with a username that is not existing in the database. I get a message "Invalid Username / Password!"
    * I try to login with a username / password combination that is not existing in the database. I get a message "Invalid Username / Password!"
    * I try to login with username / password combination existing in the database. I get a message "Login Successful" and i am transferred to my profile page.

3. Forgot Password for Existing User
    * In the login screen below the button, I use the Generate new Password link. I am routed to the Reset Password screen.
    * I add the username less than 5 characters and try to submit. A mandatory pattern matching error pops up.
    * I add an invalid email id and try to submit. my input is underlined in red indicating that something is wrong.
    * I add the email id which is valid and this has to be the one that I had used during registration, this shows a green underline and i can proceed
    * I add a invalid username and /or emailid and add passwords which are mismatching. I get an error message "invalid User"
    * I add a valid username and wrong emailid and add passwords which are matching. I get an error message "invalid User"
    * I add a valid username and emailid and mismatching passwords. I get an error message saying "Password doesn't match, please try again"
    * I add a valid username and emailid which i had provided during user registration and two matching passwords. I get a message "New Password generated for user" 
    * I click on the link below the button . On selecting Login with new Password. I am redirected to the login page.

4. Logout
    * I have not logged in or registered yet and I am trying to logout. The logout option is not displayed before any user logs in.
    * When I am logged in and I want to logout, I click the logout menu in the navbar. I get a message "Logged out Successfully!" and I am directed back to the home page

### Search the site

Site Search can be invoked from all the pages, The link for this can be seen in the Nav bar on the top right corner. The listing page for book also has the option for searching for books

* I click on "Search Books" in the Navbar, The search book page is displayed.
* I click on search button without any value, I get a book list of all the books that are currently stored in the Database. The total number of records fetched is displayed on the top using a flash message.
* I select a category and then click on search button, In case there are no matching records for this category a suitable flash message is displayed on top otherwise, the number of matching records for the chosen category is displayed in the booklist page with a suitable message
* I don't make a category selection and add a book name for searching, The matching book names are displayed.  with suitable message for number of books fetched.
* I select a category and provide a name for a book, If no matching records are found, with the bookname in the chosen category, suitable message is displayed, else the matching books are displayed in the book list page.

### Registered User Login

#### User Profile Page
* I login successfully as a valid user, I am routed to the profile page.
    - I can see a welcome message and the last login date and time
    - I can see the list of books that are available in the website
    - I can see a cover picture of each book with the book_name and a "Check Reviews.." link, on occasion when the cover picture is not displayed, a placeholder text for the Book Image is displayed.
    - I can click on the three vertical dots at the end of the book name and the card shows details of the book (short description, Genre / book category & author name)
    - I can click on the upper left hand cross sign and the card refreshes to show me the book cover and book name as earlier.
    - I can see the Delete and the Edit button for the books that have been added by me.
    - I cannot see Delete or Edit buttons for the books that are not added by me.

#### Add a Book
* I click on the Add Book link in the navbar, I am routed to the Add Book Page.
* I click on the Categories, I can see a list of all the categories that are there in the website
* I select a category, I can select any one that I wish to. 
* I try to add a book with only category name and no other data, The mandatory marked (*) fields show up in red indicating that those needs to be filled
* I add a book name of 3 characters long and try to submit, It displays an error condition with a red underline
* I add a book name of 5 characters at and try to submit with book name and category, The book name is green now but the Author field shows a red underline indicating it is a mandatory field and cannot be left blank
* I add some characters to the author field, if it is one character the red line stays on, minimum of 2 characters gets a green underline and i am good to go
* I add more characters to the book name (test for longer text), I am able to put upto 50 characters as set in the program
* I add more than one author separated by comma, I am allowed to until 120 characters as indicated in the program
* I skip the URL and description for now and submit the new entry, the new book is created and I get a message for the same, I am routed to the book list page where I can see the book.

#### Edit and Delete Books Added by the logged in user
* I scroll down to the newly created book, which shows a blank Image, and want to put an image now, I can see and edit and delete button with the book card.
* I click on the edit button of the newly created book, I am routed to the Edit book page with the value of the category, book and authorname I have just entered.
* I make some changes in the book name and author name, and add an image link with https://<somelink with image> I add some description and save. I get a message saying this has been saved successfully and I am routed to the book list page.
* I scroll down to the book I just added and I can see the picture it fetches from the new link. 
* I click on the picture and the card refreshes with the details for author and description I had just added.
* I click on the cross on the upper left corner of the card refresh and I am routed back to my original book image again
* I click on the brown delete button at the bottom of the book card which I have added, a modal window pops up, saying this record will be permanently deleted, continue?
* I press "no" in the delete modal window, and the record is shown as it was earlier in the book list page
* I press "yes" in the delete modal window and the record is deleted from the database and is no longer available in the Book list page.

#### Add and Read Reviews of Books
* In the book list page or my profile page, I click on any of the "Check Review.." link on any of the book cards, I am routed to the Book Reviews Page.
* The book review page, has a picture of the book on the left, and the listing of all the reviews that has been given so far, or none if no one has review it yet.
* I write a short review, and press add review. My review is added in the Book review page and a message displayed as "review added successfully".

#### Edit and Delete Reviews Added by the logged in user
* I want to edit the review that I had given, I click on the brown edit button, i am routed to the edit review page.
* I add more text and make some changes to the existing text in the textarea, and then save this. I get a message "Review added Succesfully" and I am routed to the Book Review Page
* My edited review with the new changes are visible in the Book Review Page. I can see the brown buttons of edit and delete with my reviews only, so I can further edit or delete a review that I had posted and not others.
* I want to delete any of my reviews, I select the brown delete button for the review I want to delete, a Modal Delete window pops up for confirmation "This record will be deleted, do you wish to continue?" 
* I select "no" and nothing happens, I select "yes" and my review is removed from the list of reviews for the book.

### Not Registered User
* As a user who has not logged into the site, I can go and search the books by using the search functionality. The book list is displayed.
* I select "check reviews.." of any chosen book, I am shown a message "New user? Register here, Registered User? Login here to read and write reviews"

### Admin User Login

#### Admin Profile Page
* I login successfully as an Admin user, I am routed to the Admins profile page.
    - I can see a welcome message and the last login date and time 
    - I can see the Review that is currently in Feature and displayed on the home page
    - I can search Reviews by either book name, or review date or by both and a list of filtered reviews are displayed
    - I search by not providing values for either book name or review date, i get a message saying "Please filter by Book Name OR Review Date to proceed"
    - I do a search of book name and/or review date, all matching reviews are displayed in the form of cards. I can get details of Book Name, Author, Review and Reviewer name.
    - I mark a review with "On" in the featured section of the card and select save. I can see that review becomes the featured review and all other reviews no longer marked as featured
    - I go to the home page using the navbar for seeing if the featured review is in sync. Bingo! the new review that is marked as featured is displayed in the home page too.

#### Add, Edit and Delete Books
* As an Admin user, I can add a new book. I click on the Add books link in the navbar and I am routed to Add New Book Page
    - I select the book categories dropdown, I can see a list of all the categories that are there in the website
    - I select a category, I can select any one that I wish to. 
    - I try to add a book with only category name and no other data, The mandatory marked (*) fields show up in red indicating that those needs to be filled
    - I add a book name of 3 characters long and try to submit, It displays an error condition with a red underline under the book name
    - I add a book name of 5 characters at and try to submit with book name and category, The book name is green now but the Author field shows a red underline indicating it is a mandatory field and cannot be left blank
    - I add some characters to the author field, if it is one character the red line stays on, minimum of 2 characters gets a green underline and i am good to go
    - I add more characters to the book name (test for longer text), I am able to put upto 50 characters as set in the program
    - I add more than one author separated by comma, I am allowed to until 120 characters as indicated in the program
    - I skip the URL and description for now and submit the new entry, the new book is created and I get a message for the same, I am routed to the book list page where I can see the book.

* As an Admin user, I go to the Display Book option in the navbar, a Book List of all the books are displayed.
    - The books that have been added by the Admin user, will carry brown buttons of Edit and Delete icon buttons in the book card. This means the Admin, like any normal user can Edit and Delete the books he/she has added to the website
    - I click on a brown Edit Icon Button, the Edit book page opens with the existing values for each field, which can be modified.
    - I make the required changes in the Edit Books page, and Save Changes. I get a message "Book Updated Successfully"
    - I click on the brown delete Icon button on the book card that displays, a modal window pops up alerting that the record will be deleted permanently, Do you wish to continue? 
        -  On selecting Yes, the book is removed and the remaining book card orients themselves across the webpage automatically
        -  On selecting No, no book is removed, the modal box closes and I am routed to the Display book page 
    - I click on any one of the red Delete Icon button displayed with the book cards. a modal window with Delete Record message "This Book has been added by [logged in User]. Selecting Yes, will remove this record permanently. Do you wish to continue?" 
        -  On selecting Yes, the book (although added by a different user) can be removed by the Admin user and the remaining book card orients themselves across the webpage automatically
        -  On selecting No, no book is removed, the modal box closes and the Admin user is routed to the Display book page 

### Delete Reviews
* As an Admin user, I click on the Display Books on the navbar. I am taken to the Book List page which shows the books and a "Check Review.." link
    - I click on the "Check Review.." link on any of the selected book. I am routed to the Book Review Page. 
    - I need to login as a normal user in order to post a review. I am given a suitable message and link to the login page, for adding reviews.
    - I can see red delete icon buttons with all the displayed reviews. this can be used to delete a specific review, in case admin finds this review to be unsuitable.
        -  On selecting Yes, the book (although added by a different user) can be removed by the Admin user and the remaining book card orients themselves across the webpage automatically
        -  On selecting No, no book is removed, the modal box closes and the Admin user is routed to the Display book page 
    - I can see a featured review marked with a star icon, When a review is published in the Home Page as featured review, the review cannot be deleted or modified. All the delete button for the featured review is disabled.

### Brouser testing on Computer, Laptop, iPad and mobile devices
The website has been extensively tested in Chrome and Safari web browsers, in iPad and iPhone and adjusts according to the width of the screen

### Known Issues.
1. While testing the Add Book page, I noticed, that the image_url doesnot come up initially but on editing the book after successful record creation, and putting the same image url the book picture is shown
2. All the capitalized works are converted into lower caps word while inserting records in mongoDB. This needs to be edited, and then displays as expected.

## Deployment

The project uses github for hosting and has been deployed using heroku. The github repository is connected to the heroku.

### Deploy to Heroku
The project is connected to Heroku using automatic deployment from GitPod , using the following steps...

**Step 1: Create the requirements.txt and the Procfile.**
    To create a requirements.txt file,  we use the following command in CLI: 
    
        $ pip3 freeze --local > requirements.txt
    
    this will redirect the output of our freeze command into a file called requirements.txt.  Once this is created, now we need to add that file to the staging area, using 'git add -A' and hit enter.
    followed by: git commit -m "Add requirements.txt"
    If we click on the file to open it, you can see that it contains a list of the dependencies needed so far, which are 'Click', 'Flask, 'itsdangerous', and 'Werkzeug'.
    Next, we need to push this file to Heroku, by using: git push 
   
    Now we need to create the Procfile. The Procfile tells Heroku how to run our application.  A Procfile is a Heroku-specific type of file that tells Heroku how to run our project. The following command is used in the CLI to create a Procfile:

        $ echo web: python app.py > Procfile

    We need to add this to github by using the git add -A Procfile command, then git commit and finally push this into the git repository using the git push command.

**Step 2: Creating a New App in Heroku.**
    After usual login into Heroku, we need to create a new App. My new app for this project is named "views-and-reviews". The next step here is to 
    choose the appropriate region, then click 'Create app'.

**Step 3: Connect your git repository to Heroku App.**
    On the Heroku Dashboard, we need to select the deploy tab and select the Deployment method 'GitHub'.

    On the 'Connect to GitHub' section I need to search for my git repository which contains my project code. This is "Milestone3_Data_Centric" that i had created in Github for my project. I will need to search for this repository and connect to this one once the search results are displayed with my repository listing.

    My Github repository "Milestone3_Data_Centric" has my codebase, which is now connected to the new Heroku App.

**Step 4: Setup the Config variables in Heroku App**
    In the Settings tab on Heroku Dashboard, we need to select "Reveal Config Vars" to enter variables (key and value) contained in the env.py file. Following are the keys that have been used in this project and also in the Config Vars of the Heroku App.
        IP
        PORT
        SECRET_KEY
        MONGO_URI
        MONGO_DBNAME

**Step 5: Deploy my project to Heroku.**
    Once all the above 4 steps are done, we need to go to the Deploy tab on Heroku Dashboard and under the Automatic deployment section, click 'Enable Automatic Deploys'. This was done, so that all subsequent git commits in my git repository is reflected in the Heroku App as well. 
    After this is done, We need to select 'Deploy Branch'.

    Heroku will now receive the code from GitHub and start building the app using the required packages.

    Once built you will receive the message 'Your app was successfully deployed' and you can click 'View' to launch your new app.

### Access to code
The codebase in github can be accessed by forking and making a local clone of the repository "Milestone3_Data_Centric"

**Forking the GitHub Repository**
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

    STEP 1 - Log in to GitHub and locate the GitHub Repository
    STEP 2 - At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
    STEP 3 - You should now have a copy of the original repository in your GitHub account.

**Making a Local Clone**

    STEP 1 - Log in to GitHub and locate the GitHub Repository
    STEP 2 - Under the repository name, click "Clone or download".
    STEP 3 - To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
    STEP 4 - Open Git Bash
    STEP 5 - Change the current working directory to the location where you want the cloned directory to be made.
    STEP 6 - Type git clone, and then paste the URL you copied in Step 3.

    $ git clone https://github.com/Anindita123-code/Milestone3_Data_Centric.git
    
    STEP 7 - Press Enter. Your local clone will be created.

    $ git clone https://github.com/Anindita123-code/Milestone3_Data_Centric.git

Note: The repository name and output numbers that you see on your computer, representing the total file size, etc, may differ from the example I have provided above.

Add an env.py file to your workspace to include your environment variables. This should be a copy of the env.py file, and .gitignore file present in the git repository

Note: The env.py mustn't be tracked as any GitHub user can access your confidential data and hence this is included as part of the .GitIgnore file

Once this is done, the Project can be run from the local using the following command in the gitpod CLI

    $ python3 app.py


## Credits
* For creating the sitemap I have used [Gloomaps](https://www.gloomaps.com/EJjeybEnhs)
* For Creating the Data Flow Diagram I have used [Miro] (https://miro.com/app/board/o9J_lWeK1kc=/)
* For generating values for Secret Keys, I have used [RandomKeygen](https://randomkeygen.com/). A SECRET_KEY is required when using the flash and session functions of Flask.
* For creating the favicon.ico I have used [Gauger.io](https://gauger.io/fonticon/)

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
