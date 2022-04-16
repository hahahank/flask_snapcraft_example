from flask import Flask, redirect, render_template, request, session, url_for, Response
from werkzeug.serving import run_simple
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import psutil
import json
import platform
import time
import subprocess
import os
import sys

from app import app


if __name__ == '__main__':
   app.run(host='0.0.0.0',debug = False, port=1234)

