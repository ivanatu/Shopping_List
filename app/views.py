from flask import render_template, session, request, url_for, redirect, flash
from app.server import ShoppingListApplication
from app import app

the_application = ShoppingListApplication()

@app.route('/', methods=["GET"])
def index():
    """
    This method handles the actions for the default route
    """
    message = None
    if "message" in session:
        message = session["message"]

    if "username" in session:
        username = session['username']
        shares = len(the_application.sharing_pool)
        all_list_dict = the_application.get_all_lists(username)
        return render_template("pages.html", shopping_list_dict=all_list_dict, shares=shares,
                               first_name=the_application.users[username].first_name,
                               number_of_lists=len(all_list_dict), message=message, )

    return render_template("login.html", message=message)


@app.route('/create', methods=["GET", "POST"])
def create():
    """
    This method handles the actions for the /signup route
    """
    if request.method == "GET":
        return render_template("create.html")
    else:
        new_user = the_application.signup(request.form['first_name'], request.form['last_name'],
                                          request.form['username'], request.form['password'])
        if new_user:
            session['username'] = new_user.username
            return render_template("login.html")
        else:
            session["message"] = "User already exists! Please login."
        return redirect(url_for('index'))


@app.route('/login', methods=["GET", "POST"])
def login():
    """
    This method handles the actions for the /login route
    """
    if request.method == "GET":
        return render_template("login.html")
    else:
        if the_application.login(request.form['username'], request.form['password']):
            session['username'] = request.form['username']
            session["message"] = "Login Successful!"
        else:
            session["message"] = "Invalid username or password!"
        return redirect(url_for('index'))


@app.route("/logout")
def logout():
    """
    This method handles the actions for the /logout route
    """
    session["message"] = "Logout Failed, Please try again."
    if not the_application.logout(session['username']):
        session.pop('username', None)
        session["message"] = "Logout Successful!"
    return redirect(url_for('index'))


@app.route("/create_shopping_list", methods=["POST", "GET"])
def create_shopping_list():
    """
    This method handles the actions for the /create_shopping_list route
    """
    session["message"] = "Something went wrong, Please try again."
    if "username" in session:
        if request.method == "GET":
            return render_template("create_list.html")
        else:
            if the_application.create_shopping_list(request.form['title'],  session["username"]):
                session['item'] = request.form['title']
                session["message"] = "List created!"
            else:
                session["message"] = "Error Creating list!"
            return redirect(url_for('index'))

@app.route("/edit_shopping_list", methods=["POST", "GET"])
def edit_shopping_list():
    """
    This method handles the actions for the /edit_shopping_list route
    """
    session["message"] = "Something went wrong, Please try again."
    if "username" in session:
        if request.method == "GET":
            return render_template("edit_list.html")
        else:
            if the_application.edit_shopping_list(request.form['old_title'], request.form['new_title'], session["username"]):
                session['title'] = request.form['new_title']
                session["message"] = "Item edited!"
            else:
                session["message"] = "Error Creating list!"
            return redirect(url_for('index'))

@app.route("/remove_shopping_list/<title>", methods=["POST", "GET"])
def remove_shopping_list(title):
    """
    This method handles the actions for the /remove_shopping_list route
    """
    if "username" in session:
        
        if the_application.remove_shopping_list(title, session["username"]):
            session["message"] = "Item deleted!"
        else:
            session["message"] = "Error Creating list!"
        return redirect(url_for('index'))

# @app.route("/pages/<title>", methods=['GET', 'POST'])
# def pages(title):
#     return render_template("pages.html")

@app.route("/add_item", methods=["POST", "GET"])
def add_item():
    """
    This method handles the actions for the /add_item route
    """
    session["message"] = "Something went wrong, Please try again."
    if "username" in session:
        if request.method == "GET":
            return render_template("add_item.html")
        else:
            if the_application.add_item(request.form['name'], request.form['list_title'], request.form['price'],session["username"]):
                session["message"] = "item added!"
            else:
                session["message"] = "Error Creating list!"
            return redirect(url_for('index'))

@app.route("/edit_item", methods=["POST", "GET"])
def edit_item():
    """
    This method handles the actions for the /edit_item route
    """
    if "username" in session:
        if request.method == "GET":
            return render_template("edit_item.html")
        else:
            if the_application.edit_item(request.form['list_title'], request.form['old_name'], request.form['new_name'], request.form['price'], session["username"]):
                session["message"] = "Edit Successful!"
            else:
                session["message"] = "Error Editing Item!"
            return redirect(url_for('index'))


@app.route("/remove_item/<title>/<name>")
def remove_item(title, name):
    """
    This method handles the actions for the /remove_item route
    """

    if "username" in session:
        
        if the_application.remove_item(title, name, session["username"]):
            session["message"] = "Item removed successfully"
        else:
            session["message"] = "Error Creating list!"
    return redirect(url_for('index'))
    # session["message"] = "Something went wrong, Please try again."
    # if "username" in session:
    #     the_application.remove_item(
    #         request.args.get('list_title'), request.args.get('name'), session["username"])
    #     session["message"] = "Shopping List Item `" + \
    #         request.args.get('name') + "` removed successfully!"
    # return redirect(url_for('index'))


@app.route("/check_item_toggle", methods=["GET", "POST"])
def check_item_toggle():
    """
    This method handles the actions for the /check_item_toggle route
    """
    session["message"] = "Something went wrong, Please try again."
    if "username" in session:
        status = request.args.get('new_status')
        bool_status = False
        status_message = "unchecked"
        if status == "true":
            bool_status = True
            status_message = "checked"
        the_application.check_item_toggle(
            request.args.get('list_title'), request.args.get('name'),
            bool_status, session["username"])
        session["message"] = "Shopping List Item `" + \
            request.args.get('name') + "` " + status_message + " successfully!"
    return redirect(url_for('index'))
