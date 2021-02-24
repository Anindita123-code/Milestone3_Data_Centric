![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Views and Reviews

## Project Overview

The Views and Reviews project caters to individuals of interest by Sharing their Reviews about one or more than one book. The reviewers of the books are registered users of the website. And this website helps capturing various perspectives on a book which a reader can reference before they decide on having a personal copy to themselves. 

This website will provide as a reference for any book buyer, to search for reviews and provide a rating for the reviews that has been posted. However, only registered users can post a review. This project has been build using Pyhon and Flask Framework as Backend and MongoDB as the database. Details of this is provided in the detailed sections below.
 
## UX

### Strategy Plane

The "Views and Reviews" project has been concieved having in mind for the book readers community. Readers often require to read a short review of a book to understand whether it would be the one of their next reading lists. This website will help the users get a deeper insight into a book, and post a review on any kind of books ranging from story books, Cookery books, Art books, Biographies, Comics and more. Any user can search the website for reviews that might be posted already. They can also rate a review.

### Scope Plane

The scope of "Views and Reviews" is capped at the following:
    1. Users will be able to register and thereby login into the website to post a review on any book of their choice
    2. All users will be able to search and read a review on any books. They can also rate a review.
    3. Tha Admin user can publish any of the existing reviews as the review of the week. And will have superuser access to remove any reviews from the website.

* Here, the focus is on reviews posted by user, and hence user management in detail is considered outside the scope of this system. 
* Any kind of analysis with the ratings of reviews is outside the scope of this project.

### Structure Plane 

The website is structured so that the user can navigate easily and fulfill their goal of either reading reviews or posting a review for any book. A sitemap of the project is enclosed below

![Project Sitemap](https://github.com/Anindita123-code/Milestone3_Data_Centric/blob/master/Design/Sitemap.png?raw=true)

The Data is stored in the Backend. The database being used to store this is MongoDB. The Data is structured in the form of JSON files. 

{{ ER diagrams here }}

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


***********************************************
In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.
********************************************************************
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
