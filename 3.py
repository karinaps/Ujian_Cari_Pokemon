# Cari Pokemon

from flask import Flask, request, send_from_directory, render_template, redirect, url_for
import json, requests

app = Flask(__name__)

#HOME ROUTE======================================================================================
@app.route('/')
def welcome():
    return render_template('1ujian.html')

#HASIL ROUTE=====================================================================================

@app.route('/hasil', methods=['POST', 'GET'])
def berhasil():
    namapokemon = request.form['nama']
    urlpoke = 'https://pokeapi.co/api/v2/pokemon/'+namapokemon
    pokemon = requests.get(urlpoke)
    
    if str(pokemon) == '<Response [404]>':
        return redirect('/error')
    filepoke = pokemon.json()['forms']
    nama = filepoke[0]['name'].replace(filepoke[0]['name'][0], filepoke[0]['name'][0].upper())
    gambarpoke = pokemon.json()['sprites']
    gmb = gambarpoke['front_default']
    idPokemon = pokemon.json()['id']
    beratpokemon = pokemon.json()['weight']
    tinggipokemon = pokemon.json()['height']
    filesPoke = [nama, gmb, idPokemon, beratpokemon, tinggipokemon]
    
    return render_template('2ujian.html', x = filesPoke)

#ERROR ROUTE==================================================================================================
@app.route('/error')
def errornotfound():
    return render_template('errorujian.html')

#404 error handler=================================================================================================
@app.errorhandler(404)
def notFound404(error):
    return render_template('errorujian.html')

#DEBUG TRUE======================================================================================

if __name__ == '__main__':
    app.run(debug = True)