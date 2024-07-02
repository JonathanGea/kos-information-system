from flask import render_template, redirect, url_for, request, jsonify
from app import app

@app.route('/template', methods=["GET"])
def templateRoute():
    return render_template('kaiadmin-lite-1.0.0/index.html')

@app.route('/components/avatars')
def avatars():
    return render_template('kaiadmin-lite-1.0.0/components/avatars.html')

@app.route('/components/buttons')
def buttons():
    return render_template('kaiadmin-lite-1.0.0/components/buttons.html')

@app.route('/components/gridsystem')
def gridsystem():
    return render_template('kaiadmin-lite-1.0.0/components/gridsystem.html')

@app.route('/components/panels')
def panels():
    return render_template('kaiadmin-lite-1.0.0/components/panels.html')

@app.route('/components/notifications')
def notifications():
    return render_template('kaiadmin-lite-1.0.0/components/notifications.html')

@app.route('/components/sweetalert')
def sweetalert():
    return render_template('kaiadmin-lite-1.0.0/components/sweetalert.html')

@app.route('/components/font-awesome-icons')
def font_awesome_icons():
    return render_template('kaiadmin-lite-1.0.0/components/font-awesome-icons.html')

@app.route('/components/simple-line-icons')
def simple_line_icons():
    return render_template('kaiadmin-lite-1.0.0/components/simple-line-icons.html')

@app.route('/components/typography')
def typography():
    return render_template('kaiadmin-lite-1.0.0/components/typography.html')

@app.route('/sidebar-style-2')
def sidebar_style_2():
    return render_template('kaiadmin-lite-1.0.0/sidebar-style-2.html')

@app.route('/icon-menu')
def icon_menu():
    return render_template('kaiadmin-lite-1.0.0/icon-menu.html')

@app.route('/forms/basic-form')
def basic_form():
    return render_template('kaiadmin-lite-1.0.0/forms/forms.html')

@app.route('/tables/basic-table')
def basic_table():
    return render_template('kaiadmin-lite-1.0.0/tables/tables.html')

@app.route('/tables/datatables')
def datatables():
    return render_template('kaiadmin-lite-1.0.0/tables/datatables.html')

@app.route('/maps/google-maps')
def google_maps():
    return render_template('kaiadmin-lite-1.0.0/maps/googlemaps.html')

@app.route('/maps/jsvectormap')
def jsvectormap():
    return render_template('kaiadmin-lite-1.0.0/maps/jsvectormap.html')

@app.route('/charts/chart-js')
def chart_js():
    return render_template('kaiadmin-lite-1.0.0/charts/charts.html')

@app.route('/charts/sparkline')
def sparkline():
    return render_template('kaiadmin-lite-1.0.0/charts/sparkline.html')

@app.route('/widgets')
def widgets():
    return render_template('kaiadmin-lite-1.0.0/widgets.html')

@app.route('/demo1/index')
def demo1_index():
    return render_template('kaiadmin-lite-1.0.0/demo1/index.html')