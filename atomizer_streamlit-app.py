import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY = st.secrets("GOOGLE_API_KEY")
PASSWORD_CHECK = st.secrets("PASSWORD_CHECK")

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash-lite")

# Nome della pagina
st.set_page_config(
        page_title="🚀 Atomizer",
)

# Titolo dell'app
st.title("🚀 Atomizer")
st.subheader("Trasforma le notizie in insight!")
st.markdown("**Benvenuto in Atomizer!** ✨ Scrivi una notizia con numeri e lascia che l'IA trovi l'informazione più interessante per creare un riassunto efficace.")

################################################################### Spazio extra
st.markdown("""
    <style>
        .spacer {
            margin-bottom: 20px;
        }
    </style>
    <div class='spacer'></div>
""", unsafe_allow_html=True)

# Parola d'ordine
password = st.text_input("### Prima d'iniziare, parola d'ordine!")

################################################################### Spazio extra
st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

# Scelta dello stile
livello = st.selectbox("### 🎭 Scegli lo stile del tuo Atomic Essay:",
                        ["1️⃣ Freddo e Distaccato", "2️⃣ Coinvolgente ma Professionale",
                         "3️⃣ Originale e Creativo", "🤯 Fuori di Testa"])

################################################################### Spazio extra
st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

with st.expander("ℹ️ Cosa significa ogni livello di stile?"):
    st.markdown("""
    - **1️⃣ Freddo e Distaccato**: Il testo è neutro, obiettivo e privo di emozioni.
    - **2️⃣ Coinvolgente ma Professionale**: Il testo mantiene un tono chiaro e professionale, ma con un tocco più umano.
    - **3️⃣ Originale e Creativo**: Il testo è più narrativo e avvincente, con un pizzico di originalità.
    - **🤯 Fuori di Testa**: Il testo è esagerato, spettacolare e scritto con un tono fuori dagli schemi.
    """)

# Testo input
txt = st.text_area(
    label="### ✍️ Inserisci la tua notizia",
    help="Scrivi una notizia che contenga almeno un numero. Ad esempio: 'Il debito pubblico ha raggiunto i 3.000 miliardi di euro.'",
    placeholder="Es. 'L'inflazione è aumentata del 5% rispetto all'anno scorso...'",
    height = 340
)

# Definizione dello stile in base alla scelta
if livello == "1️⃣ Freddo e Distaccato":
    stile = """🔹 Livello 1 – Freddo e Distaccato
➡️ Tono: Obiettivo, neutrale, senza enfasi.
➡️ Stile: Frasi concise, prive di coinvolgimento emotivo.
➡️ Lessico: Formale, giornalistico, senza metafore o elementi stilistici marcati.

✅ Esempio:
📌 Input:
"Il debito pubblico ha raggiunto i 3.000 miliardi di euro, segnando un aumento del 2% rispetto al trimestre precedente."

📝 Output (Livello 1):
"Il debito pubblico ammonta a 3.000 miliardi di euro, con un incremento del 2% rispetto al trimestre precedente. Questo dato riflette l’andamento della spesa pubblica e delle politiche economiche attuate."
"""

elif livello == "2️⃣ Coinvolgente ma Professionale":
    stile = """🔹 Livello 2 – Coinvolgente ma Professionale
➡️ Tono: Chiarezza ed equilibrio tra professionalità e leggibilità.
➡️ Stile: Testo più fluido, con transizioni naturali tra i concetti.
➡️ Lessico: Accessibile, ma senza perdere autorevolezza. Possono essere usate domande retoriche o analogie leggere per stimolare l’interesse.

✅ Esempio:
📌 Input:
"Il debito pubblico ha raggiunto i 3.000 miliardi di euro, segnando un aumento del 2% rispetto al trimestre precedente."

📝 Output (Livello 2):
"Il debito pubblico italiano ha toccato quota 3.000 miliardi di euro, con un incremento del 2% nell'ultimo trimestre. Questo dato solleva interrogativi sulle strategie economiche future: riuscirà il governo a contenere la crescita del debito, o serviranno nuove misure correttive?"
"""

elif livello == "3️⃣ Originale e Creativo":
    stile = """🔹 Livello 3 – Originale e Creativo
➡️ Tono: Più narrativo e vivace, adattandosi all’argomento.
➡️ Stile: Può includere storytelling, metafore, elementi più espressivi.
➡️ Lessico: Più vario e dinamico, con maggiore libertà stilistica.

✅ Esempio:
📌 Input:
"Il debito pubblico ha raggiunto i 3.000 miliardi di euro, segnando un aumento del 2% rispetto al trimestre precedente."

📝 Output (Livello 3):
"3.000 miliardi di euro: il debito pubblico continua la sua scalata, aggiungendo un altro +2% in pochi mesi. È come se ogni cittadino italiano si trovasse con un conto da oltre 50.000 euro sulle spalle. La domanda è: questa montagna crescerà ancora, o qualcuno troverà il modo di ridurla?"
"""

elif livello == "🤯 Fuori di Testa":
    stile = """🔹 Livello 4 – Fuori di Testa 🤯
➡️ Tono: Esagerato, teatrale, iperbolico, come se l’IA fosse in preda a un delirio creativo.
➡️ Stile: Frasi esplosive, paragoni assurdi, riferimenti epici o surreali.
➡️ Lessico: Ricco di enfasi, onomatopee, riferimenti pop o storici fuori contesto.

✅ Esempio:
📌 Input:
"Il debito pubblico ha raggiunto i 3.000 miliardi di euro, segnando un aumento del 2% rispetto al trimestre precedente."

📝 Output (Livello 4):
"TRE. MILA. MILIARDI. DI. EURO. 🔥🔥🔥 Se ogni banconota fosse impilata, raggiungeremmo la Luna e potremmo ordinare una pizza direttamente su Marte! 🚀 Il debito pubblico è ormai una creatura mitologica che si nutre di bilanci statali e sogni di stabilità economica. Il 2% in più? Roba da far tremare i contabili e mandare in tilt le calcolatrici! Qualcuno chiami un supereroe fiscale, perché qui serve un miracolo! 🦸💸""
"""

# PROMPT
prompt = f"""
Sei un assistente esperto in analisi di notizie e scrittura sintetica.
Il tuo compito è individuare il dato numerico più rilevante in una notizia e scrivere un breve atomic essay chiaro ed efficace.

Istruzioni:
1. Analisi della notizia:
1a. Esamina il testo fornito dall'utente.
1b. Identifica i numeri presenti e il loro contesto.
1c. Scegli il dato numerico più interessante o significativo.

2. Scelta dell'angolo narrativo:
2a. Domandati: "Qual è il dato che rende questa notizia più rilevante o sorprendente?"
2b. Pensa a come evidenziarlo nel modo più chiaro possibile.

3. Scrittura dell'atomic essay:
3a. Struttura il testo in modo chiaro e incisivo.
3b. Il primo paragrafo introduce il contesto.
3c. Il secondo paragrafo enfatizza il dato numerico, spiegandone l'importanza.
3d. Il terzo paragrafo chiude con una riflessione o una sintesi.

4. Tono adeguato:
4a. Stile richiesto: {stile}

5. Output:
5a. La tua risposta deve comprendere solo l'atomic essay in formato Markdown.
5b. La risposta deve comprendere anche un titolo evocativo coerente con lo stile.
5c. La frase più importante in ognuno dei tre paragrafi deve essere evidenziata in grassetto.

Di seguito la notizia da analizzare:

<input>
{txt}
</input>

"""

# Risposta dell'AI
response = model.generate_content(prompt)

# Pulsante per generare il testo
if st.button("✨ Genera Atomic Essay!") and password.lower() == PASSWORD_CHECK:
    st.markdown("---")  # Separatore per evidenziare l'output
    st.subheader("📝 Risultato Generato")
    st.markdown(response.text)

    ############################################################### Spazio extra
    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

    # Tab per mostrare il prompt generato
    with st.expander("📜 Mostra il prompt utilizzato"):
        st.code(prompt, language="text")
else:
    st.write("Parola d'ordine errata!")

################################################################### Spazio extra
st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

st.markdown("---")
st.caption("🔍 Atomizer è un progetto sperimentale. Fai un test e scopri come può aiutarti! 🚀")
