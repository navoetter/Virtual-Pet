# Virtual-Pet

---

### 🎮 Das Spielprinzip
Das Spiel ist eine Lebenssimulation eines digitalen Haustiers. Das Ziel ist es, das Pet am Leben und bei guter Laune zu halten. Die Schwierigkeit liegt darin, dass sich die Zustände des Haustiers **dynamisch verschlechtern**, während du nicht interagierst oder während Zeit im Spiel vergeht.

#### 1. Die Bedürfnisse (Stats)
Dein Haustier wird über drei Hauptwerte definiert, die ständig sinken:
*   **Hunger** 
*   **Energie** 
*   **Glück** 

#### 2. Kern-Interaktionen
Du steuerst das Spiel über eine grafische Benutzeroberfläche (GUI) mit folgenden Aktionen:
*   **Füttern:** Füllt den Hunger-Balken auf.
*   **Schlafen:** Das Haustier ist für eine gewisse Zeit inaktiv, regeneriert aber seine komplette Energie.
*   **Spielen:** Startet kleine **Minigames**. Nur durch erfolgreiches Abschließen dieser Spiele wird das Glück deines Pets gesteigert.

---

### 🛠 Technische Umsetzung
Das Projekt wird nicht "am Stück" gebaut, sondern wächst durch die **inkrementelle Entwicklung**:

1.  **Das Grundgerüst (Logik):** Zuerst wird eine Python-Klasse `Pet` erstellt, die nur im Hintergrund rechnet (Werte abziehen, Werte addieren).
2.  **Die GUI (Oberfläche):** Statt Textbefehle tippst du auf Buttons. Die Werte werden visuell als Fortschrittsbalken dargestellt.
3.  **Minigame-Modul:** Ein separates Modul, das aufgerufen wird, wenn du "Spielen" wählst. Das kann ein simples Reaktionsspiel oder ein kurzes Quiz sein.

### 📈 Entwicklungsprozess (Scrum)
Wir nutzen **GitHub Issues**, um das Spiel in kleine, lösbare Aufgaben zu zerteilen:
*   Jedes Feature (z.B. "Hunger-Logik" oder "Button-Design") ist ein eigenes Ticket.
*   Fehler werden als Bugs gemeldet und im nächsten Sprint behoben.
*   So bleibt der Code sauber und das Spiel bleibt jederzeit testbar, auch wenn noch nicht alle Funktionen fertig sind.
