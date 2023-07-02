# PUBGm-DMG-Tower


**Description**:

The Real-Time Damage Tracker is a web application built using the Dash framework. It fetches data from an API and displays a table of the top damage dealers in a gaming competition. The application periodically updates the table based on the live data obtained from the API. The table is sorted based on the "damage" column, showcasing the players with the highest damage at the top. The application provides a visually appealing layout with team logos, player names, and their respective damage values. **Installation**

1. Clone the repository

2. Install the required dependencies:

pip install dash,requests,pandas

**Usage:**

1.  Make sure you have Python installed on your system.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where the program is located.
4.  Run the program using the following command:

python TowerDMG.py

1.  Access the application in your web browser by navigating to http://127.0.0.1:8052.
2.  The application will periodically fetch data from the API and update the table with the top damage dealers. The table is sorted in descending order based on the damage values.

**Customization:**

-   Team Logos: Place the team logos in the assets/logos/ directory. The logos should be in PNG format and named after the respective team. For example, the logo for a team named "TeamA" should be named TeamA.png.
-   Styling: The CSS styles for various elements of the application are defined in the assets/style.css file. You can modify this file to change the visual appearance of the application.

**Dependencies:**

-   Dash
-   Requests
-   Pandas

**Screenshot:**

![image](https://github.com/NotJeket/PUBGm-DMG-Tower/assets/37781149/5f363618-d6ce-499d-96f1-5662326c98ae)


**Flowchart:**

![image](https://github.com/NotJeket/PUBGm-DMG-Tower/assets/37781149/413828a1-8ad1-454f-a619-69e4162bd510)


**License**

This project is licensed under the MIT License. See the [LICENSE](https://github.com/NotJeket/PUBGm-DMG-Tower/blob/main/LICENSE) file for details.
