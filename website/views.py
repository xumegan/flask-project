from flask import Blueprint,render_template,request,flash,jsonify
from flask_login import login_required,current_user
from .models import Note
from . import db
import json

import investpy as inv
import pandas as pd
views = Blueprint('views', __name__)

@views.route('/',methods=['GET','POST']) #define a route and follow a function
@login_required
def home():
  if request.method == 'POST':
    note = request.form.get('note')
    if len(note)<1:
      flash('too short',category='error')
    else:
      new_note = Note(data=note,user_id=current_user.id)
      db.session.add(new_note)
      db.session.commit()
      flash('added',category='success')
  return render_template("home.html",user=current_user)
  
@views.route('/delete-note',methods=['POST'])
def delete_note():
  note=json.loads(request.data)
  noteId = note['noteId']
  note = Note.query.get(noteId)
  if note:
    if note.user_id == current_user.id:
      db.session.delete(note)
      db.session.commit()
  return jsonify({})

