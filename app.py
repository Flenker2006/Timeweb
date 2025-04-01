from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')

def showTimeDate():
    try:
        now = datetime.now()
        #result = supbrocess.run(['date'], stdout=subprocess.PIPE, text=True)
        
        format = now.strftime('%b %-d, %Y, %H:%M')
        #currentTimeDate = result.stdout.strip()
        
        #return f"<h1>{currentTimeDate}</h1><p> is the current date and time.</p>"
        return f"<h1>{format}</h1><p> is the current date and time.</p>" 
    except Exception as Err:
        return f"<p>ErrorL {str(Err)}</p>"

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 6969)

