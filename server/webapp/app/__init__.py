from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

from app import main
