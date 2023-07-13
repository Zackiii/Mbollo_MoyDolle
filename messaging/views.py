from django.shortcuts import render, redirect
from user.models import Demandeur, Association
from django.contrib.auth.decorators import login_required
from .models import Message



# Create your views here.
