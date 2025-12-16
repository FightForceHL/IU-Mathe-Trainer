import streamlit as st
import random
import matplotlib.pyplot as plt
import numpy as np

# --- Konfiguration der Seite ---
st.set_page_config(page_title="IU Mathe-Trainer", page_icon="🎓")

# Helper class to match the user's snippet structure
# It acts as a dict builder
def Question(frage, optionen, antwort):
    return {
        "frage": frage,
        "optionen": optionen,
        "antwort": antwort
    }

# --- Die erweiterte Fragen-Datenbank (30 Fragen) --- 
FRAGEN_DB = [ 
    # --- KAPITEL 1: Grundlagen (Mengen, Terme, Gleichungen) --- 
    Question(
        frage=r"Kapitel 1: Welche Zahlenmenge wird mit dem Symbol $\mathbb{Z}$ bezeichnet?", 
        optionen=[r"Natürliche Zahlen ($\mathbb{N}$)", r"Ganze Zahlen ($\mathbb{Z}$)", r"Rationale Zahlen ($\mathbb{Q}$)", r"Reelle Zahlen ($\mathbb{R}$)"], 
        antwort=1 
    ), 
    Question(
        frage="Kapitel 1: Welche Form muss eine quadratische Gleichung haben, um die p-q-Formel anzuwenden?", 
        optionen=[r"$ax^2 + bx + c = 0$", r"$x^2 + px + q = 0$", r"$a^2 + b^2 = c^2$", r"$y = mx + n$"], 
        antwort=1 
    ), 
    Question(
        frage=r"Kapitel 1: Was ist das Ergebnis von $3^2 \cdot 3^3$?", 
        optionen=[r"$3^6$", r"$3^5$", r"$9^5$", r"$9^6$"], 
        antwort=1 
    ), 
    Question(
        frage=r"Kapitel 1: Wie wird die Menge aller x geschrieben, für die gilt: $2 < x \le 5$?", 
        optionen=[r"$[2; 5]$", r"$]2; 5[$", r"$]2; 5]$", r"$[2; 5[$"], 
        antwort=2 
    ), 
    Question(
        frage=r"Kapitel 1: Was ist die Lösung der Gleichung $\sqrt{x+2} = 3$?", 
        optionen=[r"$x = 7$", r"$x = 1$", r"$x = -1$", r"$x = 5$"], 
        antwort=0 
    ), 
 
    # --- KAPITEL 2: Funktionen --- 
    Question(
        frage="Kapitel 2: Wie verhalten sich die Graphen einer Funktion und ihrer Umkehrfunktion zueinander?", 
        optionen=["Punktsymmetrisch zum Ursprung", "Sie sind identisch", r"Spiegelsymmetrisch zur Geraden $y = x$", "Sie schneiden sich nie"], 
        antwort=2 
    ), 
    Question(
        frage=r"Kapitel 2: Was ergibt $\log(a \cdot b)$?", 
        optionen=[r"$\log(a) \cdot \log(b)$", r"$\log(a) + \log(b)$", r"$\log(a) - \log(b)$", r"$b \cdot \log(a)$"], 
        antwort=1 
    ), 
    Question(
        frage=r"Kapitel 2: Was ist der Definitionsbereich der Funktion $f(x) = \frac{1}{x-2}$?", 
        optionen=[r"$\mathbb{R}$", r"$\mathbb{R} \setminus \{0\}$", r"$\mathbb{R} \setminus \{2\}$", r"$\mathbb{R} \setminus \{-2\}$"], 
        antwort=2 
    ), 
    Question(
        frage="Kapitel 2: Welche Funktion beschreibt exponentielles Wachstum?", 
        optionen=[r"$f(x) = x^2$", r"$f(x) = 2 \cdot x + 5$", r"$f(x) = 5 \cdot 2^x$", r"$f(x) = \sin(x)$"], 
        antwort=2 
    ), 
    Question(
        frage=r"Kapitel 2: Wo liegt der Scheitelpunkt der Parabel $f(x) = (x-3)^2 + 1$?", 
        optionen=[r"$S(3|1)$", r"$S(-3|1)$", r"$S(3|-1)$", r"$S(0|0)$"], 
        antwort=0 
    ), 
 
    # --- KAPITEL 3: Differentialrechnung I --- 
    Question(
        frage=r"Kapitel 3: Wie lautet die Kettenregel für $f(x) = g(h(x))$?", 
        optionen=[r"$f'(x) = g'(h(x)) \cdot h'(x)$", r"$f'(x) = g'(x) \cdot h'(x)$", r"$f'(x) = g'(h(x)) + h'(x)$", r"$f'(x) = g(h'(x))$"], 
        antwort=0 
    ), 
    Question(
        frage="Kapitel 3: Welche Bedingungen müssen für ein lokales Maximum bei $x_0$ erfüllt sein?", 
        optionen=[r"$f'(x_0) = 0$ und $f''(x_0) > 0$", r"$f'(x_0) > 0$ und $f''(x_0) = 0$", r"$f'(x_0) = 0$ und $f''(x_0) < 0$", r"$f'(x_0) = 0$ und $f''(x_0) = 0$"], 
        antwort=2 
    ), 
    Question(
        frage=r"Kapitel 3: Was ist die Ableitung von $f(x) = e^{2x}$?", 
        optionen=[r"$e^{2x}$", r"$2e^{2x}$", r"$2xe^{2x-1}$", r"$\frac{1}{2}e^{2x}$"], 
        antwort=1 
    ), 
    Question(
        frage=r"Kapitel 3: Was gibt die zweite Ableitung $f''(x)$ anschaulich an?", 
        optionen=["Die Steigung der Tangente", "Das Krümmungsverhalten", "Die Nullstellen", "Den Flächeninhalt"], 
        antwort=1 
    ), 
    Question(
        frage=r"Kapitel 3: Wie lautet die Produktregel für $f(x) = u(x) \cdot v(x)$?", 
        optionen=[r"$u' \cdot v + u \cdot v'$", r"$u' \cdot v - u \cdot v'$", r"$u' \cdot v'$", r"$\frac{u'v - uv'}{v^2}$"], 
        antwort=0 
    ), 
 
    # --- KAPITEL 4: Ökonomische Anwendungen --- 
    Question(
        frage="Kapitel 4: Wann spricht man von einer unelastischen Nachfrage?", 
        optionen=[r"Wenn $|\epsilon| > 1$", r"Wenn $|\epsilon| = 1$", r"Wenn $|\epsilon| < 1$", r"Wenn $\epsilon = 0$"], 
        antwort=2 
    ), 
    Question(
        frage=r"Kapitel 4: Was bedeutet 'Grenzkosten = Grenzerlöse' ($MC = MR$)?", 
        optionen=["Kostenminimierung", "Gewinnmaximierung im Monopol", "Umsatzmaximierung", "Break-Even-Point"], 
        antwort=1 
    ), 
    Question(
        frage=r"Kapitel 4: Was beschreibt die Kostenfunktion $K(x) = K_f + k_v \cdot x$?", 
        optionen=["Lineare Gesamtkosten", "Quadratische Kosten", "Nur Fixkosten", "Degressive Kosten"], 
        antwort=0 
    ), 
    Question(
        frage="Kapitel 4: Was ist der Cournotsche Punkt?", 
        optionen=["Der Schnittpunkt von Angebot und Nachfrage", "Der Punkt auf der Preis-Absatz-Funktion beim optimalen Preis", "Der Punkt minimaler Kosten", "Der Punkt, an dem der Gewinn 0 ist"], 
        antwort=1 
    ), 
    Question(
        frage=r"Kapitel 4: Wie berechnet man den Gewinn $G(x)$?", 
        optionen=[r"$G(x) = E(x) + K(x)$", r"$G(x) = E(x) - K(x)$", r"$G(x) = K(x) - E(x)$", r"$G(x) = E'(x)$"], 
        antwort=1 
    ), 
 
    # --- KAPITEL 5: Multivariate Funktionen --- 
    Question(
        frage="Kapitel 5: Wie lautet die Lagrange-Funktion $L$?", 
        optionen=[r"$L = f(x,y) + \lambda \cdot (g(x,y) - c)$", r"$L = f(x,y) - \lambda \cdot (g(x,y) - c)$", r"$L = f(x,y) \cdot \lambda$", r"$L = g(x,y) - f(x,y)$"], 
        antwort=0 
    ), 
    Question(
        frage=r"Kapitel 5: Wie bildest du die partielle Ableitung nach x ($f'_x$)?", 
        optionen=[r"Nach $y$ ableiten, $x$ ist konstant", r"Nach $x$ ableiten, $y$ ist konstant", "Beide gleichzeitig ableiten", r"$x$ gleich 0 setzen"], 
        antwort=1 
    ), 
    Question(
        frage="Kapitel 5: Was beschreiben die Höhenlinien (Isoquanten) einer Produktionsfunktion?", 
        optionen=["Orte gleicher Produktionsmenge", "Orte gleicher Kosten", "Den Gewinn", "Die Grenzkosten"], 
        antwort=0 
    ), 
    Question(
        frage="Kapitel 5: Wie viele Bedingungen erster Ordnung hat ein Lagrange-Ansatz mit 2 Variablen und 1 Nebenbedingung?", 
        optionen=["1", "2", "3", "4"], 
        antwort=2 
    ), 
    Question(
        frage=r"Kapitel 5: Was muss für ein Minimum einer Funktion zweier Variablen gelten (Determinante der Hesse-Matrix $H_f$)?", 
        optionen=[r"det($H_f$) > 0 und $f_{xx} > 0$", r"det($H_f$) < 0", r"det($H_f$) = 0", r"det($H_f$) > 0 und $f_{xx} < 0$"], 
        antwort=0 
    ), 
 
    # --- KAPITEL 6: Folgen und Reihen --- 
    Question(
        frage="Kapitel 6: Wie lautet das n-te Glied einer geometrischen Folge?", 
        optionen=[r"$a_n = a_1 + (n-1)d$", r"$a_n = a_1 \cdot q^{n-1}$", r"$a_n = a_1 \cdot q^n$", r"$a_n = a_1 + q^n$"], 
        antwort=1 
    ), 
    Question(
        frage="Kapitel 6: Wann spricht man von einer 'vorschüssigen' Rente?", 
        optionen=["Zahlung am Ende der Periode", "Zahlung am Anfang der Periode", "Zahlung in der Mitte der Periode", "Wenn die Zinsen negativ sind"], 
        antwort=1 
    ), 
    Question(
        frage="Kapitel 6: Was ist der Barwert einer Zahlung?", 
        optionen=["Der Wert der Zahlung in der Zukunft", "Der heutige Wert einer zukünftigen Zahlung", "Die Summe aller Zahlungen", "Der Zinssatz"], 
        antwort=1 
    ), 
    Question(
        frage=r"Kapitel 6: Welche Reihe konvergiert für $|q| < 1$?", 
        optionen=["Arithmetische Reihe", "Geometrische Reihe", "Harmonische Reihe", "Potenzreihe"], 
        antwort=1 
    ), 
    Question(
        frage=r"Kapitel 6: Wie berechnet man den Endwert $K_n$ bei Zinseszins?", 
        optionen=[r"$K_n = K_0 \cdot (1 + i \cdot n)$", r"$K_n = K_0 \cdot (1+i)^n$", r"$K_n = K_0 \cdot q^{n-1}$", r"$K_n = K_0 + n \cdot i$"], 
        antwort=1 
    ) 
]

# --- Funktionen für die Logik ---

def starte_spiel():
    st.session_state.quiz_aktiv = True
    st.session_state.score = 0
    st.session_state.aktueller_index = 0
    # Hier merken wir uns die Stärken und Schwächen:
    st.session_state.kapitel_stats = {} 
    
    random.shuffle(st.session_state.fragen_liste)
    st.session_state.letzte_antwort_war_korrekt = None

def antwort_checken(antwort_index):
    aktuelle_frage = st.session_state.fragen_liste[st.session_state.aktueller_index]
    
    # --- NEU: Kapitel erkennen und Statistik führen ---
    # Wir holen uns das "Kapitel X" aus dem Fragetext (vor dem Doppelpunkt)
    kapitel_name = aktuelle_frage["frage"].split(":")[0]
    
    # Falls das Kapitel noch nicht in der Liste ist, legen wir es an
    if kapitel_name not in st.session_state.kapitel_stats:
        st.session_state.kapitel_stats[kapitel_name] = {"richtig": 0, "gesamt": 0}
    
    # Wir zählen den Versuch
    st.session_state.kapitel_stats[kapitel_name]["gesamt"] += 1
    
    # --- Ende Neuerungen Teil A ---

    if antwort_index == aktuelle_frage["antwort"]:
        st.session_state.score += 1
        st.session_state.letzte_antwort_war_korrekt = True
        # --- NEU: Erfolg verbuchen ---
        st.session_state.kapitel_stats[kapitel_name]["richtig"] += 1
    else:
        st.session_state.letzte_antwort_war_korrekt = False
    
    st.session_state.aktueller_index += 1

        # Weiter zur nächsten Frage
    st.session_state.aktueller_index += 1
        
def zeige_visualisierung(frage_text):
    # Wir erstellen einen "leeren Rahmen" für das Bild
    fig, ax = plt.subplots()
    
    # --- KAPITEL 1: Quadratische Funktionen (Parabel) ---
    if "quadratische Gleichung" in frage_text:
        x = np.linspace(-4, 4, 100)
        y = x**2
        ax.plot(x, y, label='f(x) = x^2', color='blue')
        ax.set_title("Beispiel: Normalparabel")
        ax.grid(True)
        ax.legend()
    
    # --- KAPITEL 4: Kostenfunktion ---
    elif "Kostenfunktion" in frage_text or "Gewinn" in frage_text:
        x = np.linspace(0, 10, 100)
        K = 20 + 5 * x  # Fixkosten 20, variable Kosten 5
        E = 8 * x       # Preis 8 pro Stück
        ax.plot(x, K, label='Kosten K(x)', color='red')
        ax.plot(x, E, label='Erlöse E(x)', color='green')
        ax.set_title("Break-Even-Analyse")
        ax.grid(True)
        ax.legend()

    # --- KAPITEL 6: Exponentielles Wachstum (Zinsen) ---
    elif "Zins" in frage_text or "geometrische" in frage_text:
        n = np.linspace(0, 10, 100)
        Kn = 1000 * (1.05)**n # Startkapital 1000, 5% Zinsen
        ax.plot(n, Kn, label='Kapitalentwicklung', color='purple')
        ax.set_title("Zinseszinseffekt")
        ax.grid(True)
        ax.legend()
        
    else:
        # Kein passendes Bild für diese Frage? Dann malen wir nichts.
        return

    # Das fertige Bild an Streamlit übergeben
    st.pyplot(fig)

# --- Initialisierung des "Gedächtnisses" (Session State) ---
if 'quiz_aktiv' not in st.session_state:
    st.session_state.quiz_aktiv = False
if 'fragen_liste' not in st.session_state:
    st.session_state.fragen_liste = FRAGEN_DB.copy()

# --- GUI Aufbau ---

if not st.session_state.quiz_aktiv:
    # STARTBILDSCHIRM
    st.title("🎓 IU Wirtschaftsmathe-Trainer")
    st.write("Hallo Kiara! Bereit, dein Wissen aus den Skripten zu testen?")
    st.write("Klicke auf den Button, um zu starten.")
    
    if st.button("🚀 Quiz starten", type="primary"):
        starte_spiel()
        st.rerun()

else:
    # QUIZ LÄUFT
    
    # Prüfen, ob wir am Ende sind
    if st.session_state.aktueller_index >= len(st.session_state.fragen_liste):
        st.title("🎉 Dein Ergebnis")
        st.write(f"Du hast **{st.session_state.score}** von **{len(st.session_state.fragen_liste)}** Punkten erreicht!")
        
        # Gesamt-Fortschrittsbalken
        prozent = st.session_state.score / len(st.session_state.fragen_liste)
        st.progress(prozent)
        
        st.markdown("---")
        st.subheader("📊 Deine Stärken- & Schwächen-Analyse")
        
        # Wir gehen jedes Kapitel durch und zeigen das Ergebnis
        for kapitel, stats in sorted(st.session_state.kapitel_stats.items()):
            quote = stats["richtig"] / stats["gesamt"]
            
            # Farbe und Text je nach Leistung
            if quote >= 0.8:
                feedback = "🌟 Perfekt! Du bist bereit für die Klausur! 🌟"
            elif quote >= 0.5:
                feedback = "✅ Solide. Ein bisschen Wiederholung schadet aber nicht."
            else:
                feedback = "⚠️Kiara??? Hier besteht Wiederholungsbedarf!"
                
            st.write(f"**{kapitel}**: {stats['richtig']} von {stats['gesamt']} richtig ({int(quote*100)}%) -> {feedback}")
            st.progress(quote)

        st.markdown("---")
        if st.button("Nochmal spielen 🔄"):
            starte_spiel()
            st.rerun()
            
    else:
        # FRAGE ANZEIGEN
        frage_data = st.session_state.fragen_liste[st.session_state.aktueller_index]
        
        # Fortschrittsbalken
        fortschritt = st.session_state.aktueller_index / len(st.session_state.fragen_liste)
        st.progress(fortschritt)
        st.caption(f"Frage {st.session_state.aktueller_index + 1} von {len(st.session_state.fragen_liste)}")

        st.subheader(frage_data["frage"])
        zeige_visualisierung(frage_data["frage"])

        # Feedback zur vorherigen Frage anzeigen (falls vorhanden)
        if st.session_state.letzte_antwort_war_korrekt is not None:
            if st.session_state.letzte_antwort_war_korrekt:
                st.success("Letzte Antwort war richtig! ✅")
            else:
                st.error("Letzte Antwort war leider falsch. ❌")
            # Reset für die nächste Anzeige, damit es nicht stehen bleibt
            st.session_state.letzte_antwort_war_korrekt = None

        # Antwort-Buttons
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button(frage_data["optionen"][0], use_container_width=True):
                antwort_checken(0)
                st.rerun()
            if st.button(frage_data["optionen"][1], use_container_width=True):
                antwort_checken(1)
                st.rerun()
        
        with col2:
            if st.button(frage_data["optionen"][2], use_container_width=True):
                antwort_checken(2)
                st.rerun()
            if st.button(frage_data["optionen"][3], use_container_width=True):
                antwort_checken(3)
                st.rerun()

        st.markdown("---")
        st.write(f"Aktueller Punktestand: **{st.session_state.score}**")
