import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    #DB execution
    c = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
    stocks = db.execute("SELECT symbol, SUM(shares) as shares FROM stocks WHERE userID = ? GROUP BY symbol HAVING (SUM(shares)) > 0;", session["user_id"])
    total = 0

    #Looping every stock from db
    for stock in stocks:
        quote = lookup(stock["symbol"])
        stock["name"] = quote["name"]
        stock["price"] = quote["price"]
        stock["total"] = stock["price"] * stock["shares"]
        total = total + stock["total"]

    k = total + c
    cash = usd(c)
    total_c=usd(k)


    return render_template("index.html", stocks=stocks, cash=cash, total_c=total_c)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        s = request.form.get("symbol")
        stocks = lookup(s)
        amount = request.form.get("shares")
        cash = db.execute("SELECT cash from users WHERE id = ?", session["user_id"])[0]["cash"]

        #Check for Shares INT type and positive
        try:
            amount = int(amount)
            if amount < 1:
                return apology("share must be a positive integer", 400)
        except ValueError:
            return apology("share must be a positive integer", 400)

        #Validate symbol entry
        if not s:
            return apology("must provide ticker", 400)
        if stocks is None:
            return apology("must provide a valid symbol", 400)

        shares_price = amount * stocks["price"]
        if cash < (shares_price):
            return apology("not enough money", 400)
        else:
            #UPD Users cash
            db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", shares_price, session["user_id"])
            #INSERT new stock info
            date = datetime.datetime.now()
            db.execute("INSERT INTO stocks (userID, symbol, shares, price, date, operation) VALUES (?, ?, ?, ?, ?, ?)", session["user_id"], s.upper(), amount, stocks["price"], date, "buy")
            flash("Transaction successful")
            return redirect("/")
    else:
        return render_template("buy.html")



@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    stocks = db.execute("SELECT symbol, shares, price, date, operation FROM stocks WHERE userID = ?", session["user_id"])
    return render_template("history.html", stocks=stocks)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 400)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        stocks = lookup(request.form.get("symbol"))
        if not request.form.get("symbol"):
            return apology("must provide ticker", 400)
        if stocks is None:
            return apology("must provide a valid symbol", 400)
        else:
            return render_template("quoted.html", name=stocks["name"],symbol=stocks["symbol"],price=stocks["price"])


    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
        # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)


        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        elif len(rows) != 0:
            return apology("username already exists", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        elif not request.form.get("confirmation"):
            return apology("must provide a confirmation password", 400)

        # Ensure passwords match
        elif not password == confirmation:
            return apology("passwords must match", 400)

        else:
            # Generate the hash of the password
            hash = generate_password_hash(password, method="pbkdf2:sha256", salt_length=8)
            # Query database for new user
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?) ", username, hash)
            # Redirect user to home page after logging in
            row = db.execute("SELECT * FROM users WHERE username = ?", username)
            session["user_id"] = row[0]["id"]
            return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        s = lookup(symbol)
        shares = request.form.get("shares")
        stocks = db.execute("SELECT symbol, SUM(shares) as shares FROM stocks WHERE userID = ? GROUP BY symbol HAVING (SUM(shares)) > 0;", session["user_id"])

        #Check for Shares INT type and positive
        try:
            shares = int(shares)
            if shares < 1:
                return apology("share must be a positive integer", 400)
        except ValueError:
            return apology("share must be a positive integer", 400)

        #Validate symbol entry
        if not symbol:
            return apology("must provide ticker", 400)
        if s is None:
            return apology("must provide a valid symbol", 400)

        #If not enought shares
        if shares > stocks[0]["shares"]:
            return apology("You don't have this number of shares", 400)
        price = s["price"]
        shares_value = price * shares

        date = datetime.datetime.now()
        db.execute("INSERT INTO stocks (userID, symbol, shares, price, date, operation) VALUES (?, ?, ?, ?, ?, ?)", session["user_id"], symbol.upper(), -shares, price, date, "sell")
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", shares_value, session["user_id"])
        flash("Sold successfully")
        return redirect("/")

    else:
        stocks = db.execute("SELECT symbol, SUM(shares) as shares FROM stocks WHERE userID = ? GROUP BY symbol HAVING (SUM(shares)) > 0;", session["user_id"])
        return render_template("sell.html", stocks=stocks)
