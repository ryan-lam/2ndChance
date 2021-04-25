from flask import Flask, redirect, url_for, render_template, request, session
app = Flask(__name__)
app.secret_key = "1234"



# username: [password, name, dob, age, gender, ID Num, Criminal Status, Prison Name]
# username: [password, name, dob, age, gender, ID Num, Criminal Status, Prison Name]
db = {
    "criminal1":["1234", "Bob Bishop", "Jan 1, 2000", "21", "Male", "1564", "Good", "New York City Jail"],
    "criminal2":["1234", "Nicole Ng", "Mar 1, 1993", "28", "Female", "7864", "Excellent", "Brooklyn Jail"],
    "criminal3":["1234", "Johnny John", "Feb 29, 1990", "31", "Male", "5722", "Good", "Rochester Jail"],
    "criminal4":["1234", "Sally Smith", "Sept 31, 1999", "22", "Female", "8425", "Poor", "New York City Jail"]
}
# [job name, company name, date, job description, location, status requirements]
jobs_db = [
    ["Front-End Developer", "Google", "April 24, 2021", 
    "Google's software engineers develop the next-generation technologies that change how billions of users connect, explore, and interact with information and one another. Our products need to handle information at massive scale, and extend well beyond web search. We're looking for engineers who bring fresh ideas from all areas, including information retrieval, distributed computing, large-scale system design, networking and data storage, security, artificial intelligence, natural language processing, UI design and mobile; the list goes on and is growing every day. As a software engineer, you will work on a specific project critical to Google’s needs with opportunities to switch teams and projects as you and our fast-paced business grow and evolve. We need our engineers to be versatile, display leadership qualities and be enthusiastic to take on new problems across the full-stack as we continue to push technology forward.", 
    "Los Angeles, USA", 
    "As a Front End Software Engineer at Google, you will specialize in building responsive and elegant web applications that scale to millions of users in dozens of languages.", 
    ["Design, develop, test, deploy, maintain and improve software", "Manage individual project priorities, deadlines and deliverables", "Be responsible for server-side and client-side feature work", "Identify and establish patterns and best practices for building excellent web experiences"]],

    ["Software Engineer", "Facebook", "April 23, 2021", 
    "Facebook is actively seeking software engineers to help build and scale our rapidly evolving network infrastructure. We are looking for software engineers with a passion for networking and aptitude for building scalable distributed systems. As a member of this small and growing team, you will be in charge of designing and implementing how we build, model, analyze and monitor Facebook’s current and next generation networks. In addition to software development, your duties may involve evaluating third party and open source software, interacting with various other Engineering teams and working with network hardware vendors. There is a wide range of areas to work on, spanning next-gen datacenter networking architecture (e.g., OpenFlow or similar technologies for software defined networking), software systems to configure, monitor, analyze, model, and manage our datacenter, backbone, and content delivery networks. ", 
    "London, United Kingdom", 
    "As a member of this small and growing team, you will be in charge of designing and implementing how we build, model, analyze and monitor Facebook’s current and next generation networks.", 
    ["Develop software to scale the Facebook production network", "Work with networking devices and protocols", "Integrate with other systems, evaluate third party solutions", "Collaborate with Network Engineering team to automate various processes, build software infrastructure for network monitoring and analysis, aid in capacity planning and architecture change analysis."]],

    ["Python Developer", "IBM", "April 22, 2021", 
    "Software Developers at IBM are the backbone of our strategic initiatives to design, code, test, and provide industry-leading solutions that make the world run today – planes and trains take off on time, bank transactions complete in the blink of an eye and the world remains safe because of the work our software developers do.  Whether you are working on projects internally or for a client, software development is critical to the success of IBM and our clients worldwide.  At IBM, you will use the latest software development tools, techniques and approaches and work with leading minds in the industry to build solutions you can be proud of.", 
    "Bangalore, India", 
    "You are a Python Developer, who will be responsible for the management of all aspects of data and information (both structured and unstructured) from business requirements to logical and physical design in an IT solution.",
    ["Implement new tool functionalities that support changing business requirements", "Develop functions that automate provisioning and access management primary/secondary controls", "Develop functions that help improve user experience", "Work on the implementation of Risk Based Access Control model"]],

    ["Graphic Designer", "Apple", "April 21, 2021", 
    "job At Apple great ideas have a way of becoming great products, services, and customer experiences. Apple Media products combines unparalleled user interface design with world-class content across TV, Music, Apps, Games and more. We are seeking an experienced visual designer to join our Media Products Design team in an exciting and fast-paced organization. The ideal designer will have a passion for taking on complex problems and designing elegant, simple solutions that surprise and delight users. We’ll provide you with unparalleled levels of opportunity and resources, with the goal of creating experiences that influence the industry, as well as people’s lives. By constantly focusing on the consumer, you’ll create products that are not only amazing to look at, but also intuitive and useful to billions of people worldwide. Join this team if you’re committed to making every human interaction — visual, audial, and haptic — amazing for our users.", 
    "Santa Clara Valley, USA", 
    "You will be responsible for bringing an uncompromising bar of quality to the look and feel of digital experiences and how they’re represented across platforms. You have experience working across a variety of design areas, including branding, visual design, art direction and interactive.", 
    ["You are a natural collaborator and a phenomenal communicator, able to develop and present design ideas in a large team environment", "You will work closely with cross-functional teams such as Engineering, Production, Product Marketing, and Senior Management", "You have an affinity for consistency, color use, typography, and a keen eye for subtle details", "You should be a self-starter, self-motivated, able to work independently, and perform multiple tasks under minimal supervision"]]
]
#Actually, it looks a dried mango
# ###############################################################################################################

# home page + login
@app.route("/") #HOME BUTTON PRESSED
def home():
    return render_template("index.html")


# admin page
@app.route("/admin", methods=['POST', 'GET']) 
def adminPage():
    if request.method == "POST":
        username = request.form["name"]
        password = request.form["password"]

        if username in db and db[username][0] == password:
            session["user"] = username
            return render_template("joblist.html", user=username, job_db=jobs_db, job_db_len=len(jobs_db))
            # return render_template("joblist.html", user=username, job_db=jobs_db, job_db_len=len(jobs_db))
        if username == "admin" and password == "1234":
            return render_template("admin.html", db=db, user_list=list(db.keys()), list_len=(len(db)))
            # return render_template("admin.html", db=db, user_list=list(db.keys()), list_len=(len(db)))
        else:
            return render_template("index.html", login_status="False")

    # else:
    #     try: 
    #         username = session["user"]
    #         return render_template("joblist.html", user=username)
    #     except:
    #         return render_template("index.html")

    return render_template("index.html")

# ADD ACCOUNT
@app.route("/add_acc", methods = ['POST'])
def add_acc():
    if request.method == "POST":
        if request.form.get("remove") == "remove":
            remove_username = request.form["add_username"]
            del(db[remove_username])
            return render_template("admin.html", db=db, user_list=list(db.keys()), list_len=(len(db)))

        else:
            add_username = request.form['add_username']
            add_name = request.form.get('add_name')
            add_password = request.form.get('add_password')
            add_birthday = request.form.get('add_birthday')
            add_age = request.form.get('add_age')
            add_gender = request.form.get('add_gender')
            add_criminalid = request.form.get('add_criminalid')
            add_criminalstatus = request.form.get('add_criminalstatus')
            add_prisonname = request.form.get('add_prisonname')
            # dd info into db
            db[add_username] = [add_password, add_name, add_birthday, add_age, add_gender, add_criminalid, add_criminalstatus, add_prisonname]
            return render_template("admin.html", db=db, user_list=list(db.keys()), list_len=(len(db)))







@app.route("/jobdescription", methods=['POST', 'GET']) #HOME BUTTON PRESSED
def jobsite():
    print("HEYHEYHEY")
    if request.method == "POST":
        value = request.form["content"]
        print(value + "HIHIHI")
    return render_template("jobsite.html", user=session["user"], job=jobs_db[int(value)])  


@app.route("/joblist") #HOME BUTTON PRESSED
def backJob():
    return render_template("joblist.html", user=session["user"], job_db=jobs_db, job_db_len=len(jobs_db))

@app.route("/profile") #HOME BUTTON PRESSED
def profile():
    return render_template("profile.html", criminal=session["user"], db=db)

if __name__ == "__main__":
    app.run(debug=True)