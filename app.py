import streamlit as st
import time
import matplotlib.pyplot as plt
import networkx as nx

st.set_page_config(page_title="AI Game System", layout="wide")

# ---------------- STYLE ----------------
st.markdown("""
<style>
.stApp {
    background-color: #0e1117;
    color: white;
}
input {
    text-align: center !important;
    font-size: 18px !important;
}
.block {
    border: 2px solid white;
}
</style>
""", unsafe_allow_html=True)

st.title("AI Game Interface")

menu = st.sidebar.radio("Select Module", ["Sudoku", "Map Coloring"])

# ================= SUDOKU =================
initial_board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

def is_valid(board, r, c, num):
    for i in range(9):
        if board[r][i] == num or board[i][c] == num:
            return False

    sr, sc = 3*(r//3), 3*(c//3)
    for i in range(3):
        for j in range(3):
            if board[sr+i][sc+j] == num:
                return False
    return True


def solve(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                for num in range(1,10):
                    if is_valid(board, r, c, num):
                        board[r][c] = num
                        if solve(board):
                            return True
                        board[r][c] = 0
                return False
    return True


if menu == "Sudoku":

    st.subheader("Sudoku Game")

    if "board" not in st.session_state:
        st.session_state.board = [row[:] for row in initial_board]
        st.session_state.start_time = time.time()

    board = st.session_state.board

    # ---- GRID ----
    wrong_cells = []

    for i in range(9):
        cols = st.columns(9)
        for j in range(9):

            val = board[i][j] if board[i][j] != 0 else ""

            disabled = initial_board[i][j] != 0

            new_val = cols[j].text_input(
                "",
                value=val,
                key=f"{i}{j}",
                max_chars=1,
                disabled=disabled
            )

            if not disabled:
                if new_val.isdigit():
                    board[i][j] = int(new_val)
                else:
                    board[i][j] = 0

    # ---- VALIDATION ----
    valid = True
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != 0:
                board[i][j] = 0
                if not is_valid(board, i, j, num):
                    valid = False
                board[i][j] = num

    if not valid:
        st.error("Invalid entries present")
    else:
        st.success("Board looks valid")

    # ---- TIMER ----
    elapsed = int(time.time() - st.session_state.start_time)
    st.write(f"Time: {elapsed} seconds")

    # ---- BUTTONS ----
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Solve"):
            solve(board)
            st.success("Solved")

    with col2:
        if st.button("Reset"):
            st.session_state.board = [row[:] for row in initial_board]
            st.session_state.start_time = time.time()
            st.rerun()


# ================= MAP COLORING =================
def map_coloring(graph, colors, assignment={}):
    if len(assignment) == len(graph):
        return assignment

    node = [n for n in graph if n not in assignment][0]

    for color in colors:
        if all(assignment.get(n) != color for n in graph[node]):
            assignment[node] = color
            result = map_coloring(graph, colors, assignment)
            if result:
                return result
            del assignment[node]
    return None


if menu == "Map Coloring":

    st.subheader("Map Coloring")

    graph = {
        "A": ["B","C"],
        "B": ["A","C","D"],
        "C": ["A","B","D"],
        "D": ["B","C"]
    }

    colors = ["Red", "Green", "Blue"]

    user = {}

    for node in graph:
        user[node] = st.selectbox(f"Region {node}", colors, key=node)

    col1, col2 = st.columns(2)

    # ---- CHECK ----
    with col1:
        if st.button("Check"):
            valid = True
            for n in graph:
                for nb in graph[n]:
                    if user[n] == user[nb]:
                        valid = False
            if valid:
                st.success("Valid coloring")
            else:
                st.error("Invalid coloring")

    # ---- AUTO SOLVE ----
    with col2:
        if st.button("Auto Solve"):
            sol = map_coloring(graph, colors)
            st.write(sol)

    # ---- GRAPH VISUAL ----
    G = nx.Graph()
    for node in graph:
        for nb in graph[node]:
            G.add_edge(node, nb)

    color_map = []
    for node in G:
        color_map.append(user.get(node, "gray").lower())

    fig, ax = plt.subplots()
    nx.draw(G, with_labels=True, node_color=color_map, node_size=2000, font_color='white', ax=ax)
    st.pyplot(fig)
