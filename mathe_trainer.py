import streamlit as st
import random

# --- Konfiguration der Seite ---
st.set_page_config(page_title="IU Mathe-Trainer", page_icon="🎓")

# --- Die Fragen-Datenbank (Deine Fragen aus den Skripten) ---
FRAGEN_DB = [
    # --- KAPITEL 1: Grundlagen ---
    {
        "frage": "Kapitel 1: Welche Zahlenmenge wird mit dem Symbol Z bezeichnet?",
        "optionen": ["Natürliche Zahlen", "Ganze Zahlen", "Rationale Zahlen", "Reelle Zahlen"],
        "antwort": 1
    },
    {
        "frage": "Kapitel 1: Welche Form muss eine quadratische Gleichung haben, um die p-q-Formel anzuwenden?",
        "optionen": ["ax^2 + bx + c = 0", "x^2 + px + q = 0", "a^2 + b^2 = c^2", "y = mx + n"],
        "antwort": 1
    },
    # --- KAPITEL 2: Funktionen ---
    {
        "frage": "Kapitel 2: Wie verhalten sich die Graphen einer Funktion und ihrer Umkehrfunktion zueinander?",
        "optionen": ["Punktsymmetrisch zum Ursprung", "Sie sind identisch", "Spiegelsymmetrisch zur Geraden y = x", "Sie schneiden sich nie"],
        "antwort": 2
    },
    {
        "frage": "Kapitel 2: Was ergibt log(a * b)?",
        "optionen": ["log(a) * log(b)", "log(a) + log(b)", "log(a) - log(b)", "b * log(a)"],
        "antwort": 1
    },
    # --- KAPITEL 3: Differentialrechnung I ---
    {
        "frage": "Kapitel 3: Wie lautet die Kettenregel für f(x) = g(h(x))?",
        "optionen": ["f'(x) = g'(h(x)) * h'(x)", "f'(x) = g'(x) * h'(x)", "f'(x) = g'(h(x)) + h'(x)", "f'(x) = g(h'(x))"],
        "antwort": 0
    },
    {
        "frage": "Kapitel 3: Welche Bedingungen müssen für ein lokales Maximum bei x0 erfüllt sein?",
        "optionen": ["f'(x0) = 0 und f''(x0) > 0", "f'(x0) > 0 und f''(x0) = 0", "f'(x0) = 0 und f''(x0) < 0", "f'(x0) = 0 und f''(x0) = 0"],
        "antwort": 2
    },
    # --- KAPITEL 4: Ökonomische Anwendungen ---
    {
        "frage": "Kapitel 4: Wann spricht man von einer unelastischen Nachfrage?",
        "optionen": ["Wenn |epsilon| > 1", "Wenn |epsilon| = 1", "Wenn |epsilon| < 1", "Wenn epsilon = 0"],
        "antwort": 2
    },
    {
        "frage": "Kapitel 4: Was bedeutet 'Grenzkosten = Grenzerlöse' (MC = MR)?",
        "optionen": ["Kostenminimierung", "Gewinnmaximierung im Monopol", "Umsatzmaximierung", "Break-Even-Point"],
        "antwort": 1
    },
    # --- KAPITEL 5: Multivariate Funktionen ---
    {
        "frage": "Kapitel 5: Wie lautet die Lagrange-Funktion L?",
        "optionen": ["L = f(x,y) + lambda * (g(x,y) - c)", "L = f(x,y) - lambda * (g(x,y) - c)", "L = f(x,y) * lambda", "L = g(x,y) - f(x,y)"],
        "antwort": 1
    },
    {
        "frage": "Kapitel 5: Wie bildest du die partielle Ableitung nach x (f'_x)?",
        "optionen": ["Nach y ableiten, x ist konstant", "Nach x ableiten, y ist konstant", "Beide gleichzeitig ableiten", "x gleich 0 setzen"],
        "antwort": 1
    },
    # --- KAPITEL 6: Folgen und Reihen ---
    {
        "frage": "Kapitel 6: Wie lautet das n-te Glied einer geometrischen Folge?",
        "optionen": ["an = a1 + (n-1)d", "an = a1 * q^(n-1)", "an = a1 * q^n", "an = a1 + q^n"],
        "antwort": 1
    },
    {
        "frage": "Kapitel 6: Wann spricht man von einer 'vorschüssigen' Rente?",
        "optionen": ["Zahlung am Ende der Periode", "Zahlung am Anfang der Periode", "Zahlung in der Mitte der Periode", "Wenn die Zinsen negativ sind"],
        "antwort": 1
    }
]

# --- Funktionen für die Logik ---

def starte_spiel():
    st.session_state.quiz_aktiv = True
    st.session_state.score = 0
    st.session_state.aktueller_index = 0
    random.shuffle(st.session_state.fragen_liste)
    st.session_state.letzte_antwort_war_korrekt = None

def antwort_checken(antwort_index):
    # Prüfen ob richtig
    aktuelle_frage = st.session_state.fragen_liste[st.session_state.aktueller_index]
    if antwort_index == aktuelle_frage["antwort"]:
        st.session_state.score += 1
        st.session_state.letzte_antwort_war_korrekt = True
    else:
        st.session_state.letzte_antwort_war_korrekt = False
    
    # Weiter zur nächsten Frage
    st.session_state.aktueller_index += 1

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
        st.title("🎉 Ergebnis")
        st.write(f"Du hast **{st.session_state.score}** von **{len(st.session_state.fragen_liste)}** Punkten erreicht!")
        
        prozent = st.session_state.score / len(st.session_state.fragen_liste)
        if prozent == 1.0:
            st.balloons()
            st.success("Perfekt! Du bist bereit für die Klausur! 🌟")
        elif prozent >= 0.5:
            st.info("Gute Arbeit! Ein bisschen Wiederholung schadet aber nicht.")
        else:
            st.warning("Da ist noch Luft nach oben. Schau dir die Skripte nochmal an!")

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
