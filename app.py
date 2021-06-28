from flask import Flask,render_template
app =Flask(__name__)
@app.route('/')
def home():
    personagens = [
       {
        'nome' : 'Tanjiro',        
        'foto' : '\static\img\_tanjiro.png'
       },

        {
        'nome' : 'Nezuko',         
        'foto' : '\static\img\_nezuko.png'
       },
   
       {
        'nome' : 'Zenitsu',        
        'foto' : '\static\img\zenitsu.png' 
       }   
   ]
    armas = [
       {
        'nome' : 'Faca',        
        'foto' : '\static\img\_faca.gif' 
       },

        {
        'nome' : 'Flecha',        
        'foto' : '\static\img\_flecha.gif' 
       },
   
       {
        'nome' : 'Espada',        
        'foto' : '\static\img\espada.gif' 
       }   
   ]


    return render_template(
       'index.html',
       personagens = personagens,
       armas = armas
     
    )
if __name__ == '__main__':
    app.run(debug=True)