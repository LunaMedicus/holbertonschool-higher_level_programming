#!/usr/bin/env python3
"""Flask application with JSON, CSV, and SQLite data sources."""

import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json():
    """Read products from products.json."""
    with open('products.json', 'r') as f:
        return json.load(f)


def read_csv():
    """Read products from products.csv and return as list of dicts."""
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        return [{"id": int(r['id']), "name": r['name'],
                 "category": r['category'], "price": float(r['price'])}
                for r in reader]


def read_sql():
    """Read products from SQLite database."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "name": r[1], "category": r[2], "price": r[3]}
            for r in rows]


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Render items from items.json."""
    with open('items.json', 'r') as f:
        data = json.load(f)
    return render_template('items.html', items=data.get('items', []))


@app.route('/products')
def products():
    """Display products from JSON, CSV, or SQL with optional id filter."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ('json', 'csv', 'sql'):
        return render_template('product_display.html', error='Wrong source')

    try:
        if source == 'json':
            data = read_json()
        elif source == 'csv':
            data = read_csv()
        else:
            data = read_sql()
    except Exception:
        return render_template('product_display.html',
                               error='Product not found')

    if product_id:
        product_id = int(product_id)
        data = [p for p in data if p['id'] == product_id]
        if not data:
            return render_template('product_display.html',
                                   error='Product not found')

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
