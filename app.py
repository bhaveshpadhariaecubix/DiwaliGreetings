from flask import Flask, render_template, jsonify, url_for
from gtts import gTTS
from io import BytesIO
import os
import uuid
import random

app = Flask(__name__)

# List of default Gujarati Diwali messages
default_gujarati_text = [
    [
        "સુખ અને સમૃદ્ધિ તમારા આંગણામાં ચમકે… "
        "દીવા શાંતિના ચારેય દિશાઓમાં ઝળકે… "
        "ખુશીઓ તમારા ઘર આંગણે આવીને ઉજવણી કરે… "
        "દિવાળીના તહેવારની તમને હાર્દિક શુભકામનાઓ!!",
    ],
    [
        "દીપાવલીનો તહેવાર, લાવે જીવનમાં નવા રંગ, "
        "ઉજાસ અને આનંદથી રહે ભરી દુનિયા આખી, "
        "ખુશીઓની ઝલક ભરાયે આપણું જીવન, "
        "દિવાળીની હાર્દિક શુભકામનાઓ!",
    ],
    [
        "પ્રેમ અને સુખનો દીપ જલે ઘરે ઘરે, "
        "સમૃદ્ધિનો પ્રકાશ ચમકે બધી તરફે, "
        "આનંદ અને હર્ષ સાથે દોસ્તી સજાવે, "
        "દીપાવલીની તમને ખૂબ ખૂબ શુભેચ્છાઓ!",
    ],
    [
        "દિવાળીએ તમારી ઈચ્છા અને સપના પુરા થાય, "
        "દરેક ક્ષણ ખુશીઓથી ભરી જતી રહે, "
        "નવી આશા અને નવું ઉલ્લાસ મળે, "
        "દિવાળીની શુભેચ્છા સાથે હાસ્ય રહે!",
    ],
    [
        "અંધકાર દૂર થઈ પ્રકાશનો માર્ગ બતાવે, "
        "હર અંતર સજાગ અને ખુશી ફેલાવે, "
        "ઘરોમાં ખુશીઓની મીઠી ખુશબૂ આવે, "
        "દીપાવલીની શુભકામનાઓ!",
    ],
    [
        "આ દિવાળીનો તહેવાર લાવે ખુશીઓની વહે, "
        "આપના જીવનમાં આનંદનો વારો ચાલે, "
        "સપના સાકાર કરવા શુભ ધારો મળે, "
        "દિવાળીની શુભકામનાઓ સાથ આપે!",
    ],
    [
        "દીપકની રોશનાઈથી ચારે બાજુ ઉજાશ રહે, "
        "જીવનમાં ખુશીઓનો બગીચો ખીલતો રહે, "
        "હંમેશા શાંતિ અને આનંદ ભરી રહે, "
        "હેપ્પી દિવાળી, આનંદની ઉજવણી કરી લે!",
    ],
    [
        "દિવાળીના દીપક જેવા શાનથી જીવન મહેંકે, "
        "દરેક ક્ષણે સુખનો ઉજાસ ફેલાતો રહે, "
        "દરેક ઘરમાં ખુશીઓની રમઝટ રહે, "
        "દિવાળીનો પાવન તહેવાર આનંદ આપે!",
    ],
    [
        "આ દિવાળી પરમ શાંતિનો સંદેશ લાવે, "
        "તમારું જીવન હંમેશા પ્રકાશિત રહે, "
        "દીપકના ચમકમાં ખુશીઓના રંગ ફેલાવે, "
        "શુભ દીપાવલી, આશીર્વાદ નિત્ય તરે!",
    ],
    [
        "ખુશીઓ, શાંતિ અને સમૃદ્ધિનો અનંત વરદાન, "
        "જીવનમાં ખુશીઓ અને સ્નેહના ઘા રહે, "
        "દીપાવલીનો પર્વ આનંદથી ભરી દે, "
        "હેપ્પી દિવાળી, દરેક દુઃખ દૂર કરે!",
    ],
    [
        "સુખ અને સમૃદ્ધિનો આ પાવન પર્વ, "
        "જીવનમાં પ્રકાશ અને ઊર્જાનો હંમેશા ભરોસો, "
        "દીપાવલીના દીપકનો સંદેશ સુખ આપે, "
        "શુભ દીપાવલી, આનંદ અને પ્રેમ સાથે!",
    ]
]


@app.route('/')
def index():
    # Default greeting
    default_greeting = random.choice(default_gujarati_text)[0]  # Accessing the first element of the list

    # Convert selected text to speech
    mp3_fp = BytesIO()
    tts = gTTS(text=default_greeting, lang='gu')
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)

    # Generate a unique filename
    audio_filename = f"diwali_greeting_{uuid.uuid4().hex}.mp3"
    audio_file_path = os.path.join("static", audio_filename)

    # Save audio
    with open(audio_file_path, "wb") as audio_file:
        audio_file.write(mp3_fp.read())

    return render_template('index.html', audio_url=url_for('static', filename=audio_filename))


@app.route('/random_greeting')
def random_greeting():
    # Select a random Gujarati greeting
    selected_greeting = random.choice(default_gujarati_text)[0]  # Accessing the first element of the list

    # Convert to speech
    mp3_fp = BytesIO()
    tts = gTTS(text=selected_greeting, lang='gu')
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)

    # Generate a unique filename
    audio_filename = f"diwali_greeting_{uuid.uuid4().hex}.mp3"
    audio_file_path = os.path.join("static", audio_filename)

    # Save audio
    with open(audio_file_path, "wb") as audio_file:
        audio_file.write(mp3_fp.read())

    return jsonify({"audio_url": url_for('static', filename=audio_filename)})


if __name__ == '__main__':
    app.run(debug=True)
