AI Problem Solving Assignment

Agarshna R – RA241102650061

Problems Implemented

Sudoku Solver (Constraint Satisfaction Problem)
A Sudoku puzzle consists of a 9×9 grid with some pre-filled values. The objective is to fill the empty cells such that each row, each column, and each 3×3 subgrid contains the digits from 1 to 9 without repetition. The system allows the user to enter values in a grid interface, validate entries, and solve the puzzle automatically using an AI-based approach.

Map Coloring Problem (Constraint Satisfaction Problem)
The map coloring problem involves assigning colors to regions such that no two adjacent regions share the same color. The system enables the user to select colors for each region, validate the assignment, and also generate an optimal solution automatically using an AI algorithm.

Algorithms Used

Sudoku Solver
The solution is implemented using the Backtracking Algorithm under the Constraint Satisfaction Problem framework. The algorithm selects an empty cell, tries possible values from 1 to 9, checks constraints (row, column, and subgrid), and recursively continues. If a conflict occurs, it backtracks and tries a different value until a valid solution is found.

Map Coloring
This problem is solved using Backtracking with Constraint Satisfaction. The algorithm assigns colors to regions one by one while ensuring that no adjacent regions have the same color. If a conflict is detected, the algorithm backtracks and tries a different color until a valid coloring is achieved.

Execution Steps

1. Clone the repository using the provided GitHub link.
2. Navigate to the project directory.
3. Install the required dependencies using the requirements file.
4. Run the application using Streamlit.
5. Open the application in a web browser using the local URL provided by Streamlit.

Commands:
git clone <your-repository-link>
cd AI_ProblemSolving_RA241102650061
pip install -r requirements.txt
streamlit run app.py

Sample Outputs

Sudoku Solver Output
The application displays the initial Sudoku grid and allows user input. After clicking the solve button, the system generates and displays the completed Sudoku grid. If invalid inputs are entered, the system provides validation feedback.

Map Coloring Output
The application allows the user to assign colors to different regions. It validates whether the coloring is correct or not. Additionally, the system can automatically generate a valid coloring solution and visually display the graph with colored regions.

Live Website
https://agarshna-06-ai-problemsolving--ra2411026050061--app-hbzqfk.streamlit.app/
