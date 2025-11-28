# 🎲 Quantum Tic-Tac-Toe Game (Qiskit + Streamlit)

A modern twist on the classic Tic-Tac-Toe — powered by **Quantum Computing**!  
This interactive game uses **Qiskit 2.x** to simulate quantum probability effects and **Streamlit** for a clean, responsive web interface.

🧠 How It Works

Each move alternates between X and O turns.
Before every move, the app performs a quantum simulation:
A single-qubit circuit applies a Hadamard gate (H) to create a superposition.
The measurement outcome (|0⟩ or |1⟩) gives a probabilistic strength displayed via progress bars.
The game continues until a player wins or the board is full.

---

## 🚀 Features

- 🧠 **Quantum Integration:** Uses Qiskit’s `AerSimulator` to generate quantum probability values via a Hadamard superposition.  
- 🎮 **Interactive Gameplay:** Play Tic-Tac-Toe with alternating turns for X and O.  
- 🧩 **Live Quantum Visualization:** Displays quantum probability amplitudes for each move.  
- 💻 **Streamlit UI:** Simple, browser-based interface — no terminal required.  
- 🔁 **Restart Anytime:** Instantly reset the board and play again.  

---

🌟 Future Enhancements

Add quantum animation effects for moves.
Show superposition-based move previews.
Integrate IBM Quantum runtime backend for live results.
Multiplayer mode (local or online).

---

## 🧰 Tech Stack

| Component | Description |
|------------|-------------|
| **Python 3.8+** | Programming language |
| **Qiskit 2.2.3** | Quantum simulation backend |
| **Qiskit Aer** | Provides the `AerSimulator` |
| **Streamlit** | Web app framework |

---
## RESULTS

<img width="1897" height="881" alt="Screenshot 2025-11-13 204017" src="https://github.com/user-attachments/assets/1cb3e79a-6cad-4470-9b93-3d8278627462" />


---
## ⚙️ Installation

### 1️⃣ Clone or Download
```bash
git clone https://github.com/yourusername/quantum-tic-tac-toe.git
cd quantum-tic-tac-toe

##  Install Dependencies

pip install streamlit qiskit qiskit-aer

## Run the App

streamlit run game.py







