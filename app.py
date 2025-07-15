from flask import Flask, render_template
from forms import RegisterForm, CardForm
from ext import app
from os import path



if __name__ == "__main__":
    import routes
    app.run()
