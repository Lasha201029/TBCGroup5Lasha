from flask import render_template, redirect, flash, request
from forms import RegisterForm, CardForm, LoginForm, EditCardForm, AddCardForm, EditRegisterForm
from ext import app, db
from models import Reg, Card, AddCard
import os
from os import path
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename

upload_folder = path.join(app.root_path, "/static/photo")


@app.route("/")
def home():
    card = Card.query.all()
    return render_template("travel.html", card=card)


@app.route("/view_card/<int:card_id>")
def view_card(card_id):
    card = db.session.get(AddCard, card_id)

    return render_template("view_card.html", card=card)


@app.route("/add_card", methods=["GET", "POST"])
@login_required
def addcard():
    form = CardForm()
    if form.validate_on_submit():
        new_card = Card(name=form.name.data, link=form.link.data)
        img = form.img.data
        directory = os.path.join(app.root_path, "static", "photo", img.filename)
        img.save(directory)
        new_card.img = img.filename
        db.session.add(new_card)
        db.session.commit()
    print(form.errors)
    return render_template("add_card.html", form=form)


@app.route("/edit_card/<int:card_id>", methods=["GET", "POST"])
@login_required
def card_editor(card_id):
    card = db.session.get(Card, card_id)
    form = EditCardForm(name=card.name, img=card.img)
    if form.validate_on_submit():
        card.name = form.name.data
        file = form.img.data
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join("static", filename))
            card.img = filename

        db.session.commit()

        return redirect("/")
    return render_template("/edit_card.html", form=form)


@app.route("/edit_cards/<int:card_id>", methods=["GET", "POST"])
@login_required
def cards_editor(card_id):
    card = db.session.get(AddCard, card_id)
    form = EditCardForm(name=card.name, img=card.img, part=card.part)
    if form.validate_on_submit():
        card.name = form.name.data
        file = form.img.data
        card.part = form.part.data
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join("static", filename))
            card.img = filename

        db.session.commit()

        return redirect("/")
    return render_template("/edit_cards.html", form=form)


@app.route("/delete_card/<int:card_id>")
@login_required
def delete_card(card_id):
    card = Card.query.get(card_id)
    db.session.delete(card)
    db.session.commit()
    return redirect("/")

@app.route("/deletes_card/<int:card_id>")
@login_required
def deletes_card(card_id):
    card = AddCard.query.get(card_id)
    db.session.delete(card)
    db.session.commit()
    return redirect("/")


@app.route("/ADD_CARDS", methods=["GET", "POST"])
@login_required
def add_cards():
    form = AddCardForm()

    regions = Card.query.order_by(Card.name).all()
    form.part.choices = [('', 'აირჩიე კუთხე')] + [(region.name, region.name) for region in regions]

    if form.validate_on_submit():
        name = form.name.data
        part = form.part.data
        file = form.img.data

        filename = None
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join("static", filename))

        new_card = AddCard(name=name, part=part, img=filename)
        db.session.add(new_card)
        db.session.commit()

        return redirect("/")
    return render_template("/ADD_CARDS.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = Reg.query.filter(Reg.name == form.name.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash("successfully logged in")
        else:
            flash("You are not logged in")
        return redirect("/")
    print(form.errors)
    return render_template("login.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = Reg(name=form.name.data, password=form.password.data,
                       birthday=form.birthday.data, gender=form.gender.data, country=form.country.data)

        db.session.add(new_user)
        db.session.commit()

        flash("successfully registered")

        return redirect("/login")

    return render_template("register.html", form=form)


@app.route("/logout")
def log_out():
    logout_user()
    return redirect("/")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/samegrelo")
def same():
    btn_name = request.args.get("btn_name")
    cards = AddCard.query.all()
    return render_template("samegrelo.html", cards=cards, btn_name=btn_name)


@app.route("/profile/<int:profile_id>", methods=["Get", "Post"])
def edit_profile(profile_id):
    user = Reg.query.get(profile_id)

    form = EditRegisterForm(name=user.name,
                        password=user.password,
                        gender=user.gender,
                        birthday=user.birthday,
                        country=user.country,
                        role=user.role)
    if form.validate_on_submit():
        user.name = form.name.data
        user.password = form.password.data
        user.gender = form.gender.data
        user.birthday = form.birthday.data
        user.country = form.country.data
        user.role = form.role.data
        db.session.commit()
        flash("you have successfully edited!", "success")
        return redirect(f"/profile")
    return render_template("edit_profile.html", form=form)


@app.route("/delete_profile/<int:profile_id>")
@login_required
def delete_profile(profile_id):
    profile = Reg.query.get(profile_id)
    db.session.delete(profile)
    db.session.commit()
    return redirect("/")


@app.route("/edit", methods=["Get", "Post"])
def edit():
    name = request.args.get("name")

    if not name:
        flash("please enter name", "warning")
        return redirect(f"/profile")
    else:
        user = Reg.query.filter_by(name=name).first()
        form = EditRegisterForm(name=user.name,
                            gender=user.gender,
                            birthday=user.birthday,
                            country=user.country,
                            role=user.role)

        if form.validate_on_submit():
            user.name = form.name.data
            user.gender = form.gender.data
            user.birthday = form.birthday.data
            user.country = form.country.data
            user.role = form.role.data
            db.session.commit()

            return redirect(f"/profile")
    return render_template("edit_profile.html", form=form)
