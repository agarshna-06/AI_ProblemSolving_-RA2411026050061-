import streamlit as st

st.set_page_config(page_title="AI Problem Solving", layout="centered")

# ---------------- SUDOKU ----------------
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True


# ---------------- MAP COLORING ----------------
def is_valid_color(node, color, assignment, graph):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


def map_coloring(graph, colors, assignment={}):
    if len(assignment) == len(graph):
        return assignment

    unassigned = [n for n in graph if n not in assignment]
    node = unassigned[0]

    for color in colors:
        if is_valid_color(node, color, assignment, graph):
            assignment[node] = color
            result = map_coloring(graph, colors, assignment)
            if result:
                return result
            del assignment[node]

    return None


# ---------------- UI ----------------
st.title("AI Problem Solving")
st.write("Solve problems using CSP and backtracking")

option = st.selectbox("Choose Problem", ["Sudoku Solver", "Map Coloring"])


# ---------- SUDOKU ----------
if option == "Sudoku Solver":
    st.subheader("Sudoku Solver")

    board = [
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

    st.write("Initial Sudoku:")
    for row in board:
        st.write(row)

    if st.button("Solve Sudoku"):
        solve_sudoku(board)
        st.write("Solved Sudoku:")
        for row in board:
            st.write(row)


# ---------- MAP COLORING ----------
elif option == "Map Coloring":
    st.subheader("Map Coloring Problem")

    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['B', 'C']
    }

    colors = ['Red', 'Green', 'Blue']

    st.write("Graph:")
    st.write(graph)

    if st.button("Solve Map Coloring"):
        solution = map_coloring(graph, colors)
        st.write("Solution:")
        st.write(solution)
