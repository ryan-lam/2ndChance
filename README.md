## Inspiration
Prisoners and individuals with a criminal background are very isolated from society. Our project aims to help provide a 2nd chance to these individuals by providing them an exclusive CS-related opportunity so they can enter society (after their prison time) and contribute to society. Our project also improves the diversity of workplaces since the individuals would have a non-conventional path.

## What it does
2ndChance connects prisoners to job posts to look for jobs. Their accounts can be monitored by prison administrators where they have full control over prisoner's information and whether they can have an account or not. 

An administrator first registers an account for a specific prisoner by entering the prisoner's personal information such as name, age, criminal ID and etc. then provides username and password for that prisoner. Later, the prisoner can use that username and password to login to his/her account to view profile and browse job posting. However, personal information set by the admin will not be changeable which prevents frauds and misinformation. 

## How we built it
We built this program by using Flask framework for backend and Bootstrap, HTML, and CSS for frontend. The login, user and job information are all stored on a database in Flask while the design and client functionalities of the site are programmed using Bootstrap, HTML, and CSS.

## Challenges we ran into
We ran into many challenges along the way such as adding prisoner information from the admin's dashboard and updating the information on the prisoner's profile. This all stemmed from the challenge of passing data from Flask to HTML and vice versa.

## Accomplishments that we're proud of
- Having a working database where you can add/remove things
- Getting the project done

## What we learned
- Passing info between the frontend and backend
- Using the passed info to make changes in the database/backend

## What's next for 2ndChance
- Build a function to allow for job posters to add their jobs
