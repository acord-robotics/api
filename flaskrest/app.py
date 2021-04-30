from flask import render_template
import connexion

# Application instance
app = connexion.App(__name__, specification_dir='./') # current directory

# Read swagger.yml file to configure endpoints
app.add_api('swagger.yml')

# Views/Pages
@app.route('/') # Root url page
def home():
    return render_template('home.html')

if __name__ == '__main__': # Run the application if running in standalone mode
    app.run(host='0.0.0.0', port=5000, debug=True)

