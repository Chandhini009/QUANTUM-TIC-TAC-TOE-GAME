# quantum_tictactoe_streamlit.py
import streamlit as st
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit_aer.backends import AerSimulator
import numpy as np

# ---------------------------------------------------------------------
# 🎮 QUANTUM TIC-TAC-TOE (Qiskit 2.x + Streamlit)
# ---------------------------------------------------------------------

st.set_page_config(page_title="Quantum Tic Tac Toe", page_icon="🎲", layout="centered")

st.title("🎲 Quantum Tic-Tac-Toe Game")
st.write("Play a **Quantum Tic-Tac-Toe**")

# ---------------------------------------------------------------------
# Board setup
# ---------------------------------------------------------------------
if "board" not in st.session_state:
    st.session_state.board = [" "] * 9
if "current_player" not in st.session_state:
    st.session_state.current_player = "X"
if "winner" not in st.session_state:
    st.session_state.winner = None

# ---------------------------------------------------------------------
# Quantum helper functions
# ---------------------------------------------------------------------
def quantum_strength():
    """Simulate a quantum probability using a Hadamard superposition."""
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)

    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    result = simulator.run(compiled_circuit, shots=100).result()
    counts = result.get_counts()
    prob_0 = counts.get("0", 0) / 100
    prob_1 = counts.get("1", 0) / 100
    return prob_0, prob_1

# ---------------------------------------------------------------------
# Game logic
# ---------------------------------------------------------------------
def check_winner(board):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    if " " not in board:
        return "Draw"
    return None


def make_move(position):
    """Player makes a move on the board."""
    if st.session_state.winner:
        return

    board = st.session_state.board
    player = st.session_state.current_player

    if board[position] == " ":
        board[position] = player
        winner = check_winner(board)
        if winner:
            st.session_state.winner = winner
        else:
            st.session_state.current_player = "O" if player == "X" else "X"

# ---------------------------------------------------------------------
# UI rendering
# ---------------------------------------------------------------------
st.sidebar.header("Game Info")
st.sidebar.write(f"**Current Player:** {st.session_state.current_player}")
st.sidebar.write(f"**Qiskit Version:** 2.2.3")

try:
    import qiskit_aer
    st.sidebar.write(f"**Aer Version:** {qiskit_aer.__version__}")
except Exception:
    st.sidebar.warning("Aer version not detected")

# Quantum visualization
st.subheader("🧠 Quantum Move Strength (Simulated Probabilities)")
p0, p1 = quantum_strength()
st.progress(int(p0 * 100))
st.caption(f"Quantum probability (|0⟩={p0:.2f}, |1⟩={p1:.2f})")

# Board layout (3x3)
cols = st.columns(3)
for i in range(3):
    for j in range(3):
        idx = 3 * i + j
        with cols[j]:
            if st.button(st.session_state.board[idx] or " ", key=idx, use_container_width=True):
                make_move(idx)

# Display winner
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.success("It's a draw!")
    else:
        st.success(f"🎉 Player {st.session_state.winner} wins!")

# Reset option
if st.button("🔄 Restart Game"):
    st.session_state.board = [" "] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None
    
