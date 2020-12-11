# coding: utf-8
# todos os imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

# configuração
DATABASE = '/tmp/flaskr.db'
# DEBUG = True
# SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = '123457'

# criar nossa pequena aplicação :)
app = Flask(__name__)
# app.config.from_object(__name__)

def conectar_bd():
    return sqlite3.connect(DATABASE)