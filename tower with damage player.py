import dash
import json
import requests
import pandas as pd
from dash import dcc, html
from dash.dependencies import Output, Input

external_stylesheets = ['assets/style.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, serve_locally=True)

def get_data():
    # API endpoint
    all_info_url = "http://127.0.0.1:5000/data1"
    # Make API call and parse the JSON response
    all_info_response = requests.get(all_info_url)
    player_data = all_info_response.json()["allinfo"]["TotalPlayerList"]
    # Extract required columns from player_data
    data = [{"teamName": player["teamName"], "playerName": player["playerName"], "damage": player["damage"]} for player in player_data]
    # Create a pandas dataframe from the extracted data
    df = pd.DataFrame(data)
    # Sort the dataframe by the "damage" column
    df = df.sort_values(by=["damage"], ascending=False)
    return df

app.layout = html.Div(
    [
        html.Table(
            [
                html.Thead(
                    [
                        html.Tr(
                            [
                                html.Th("Top Damage Dealers", className="title-name"),
                            ],
                            className="header-row",
                            style={
                                #"background-image": f"url(assets/test.png)",
                                    "background - color":  "#ffc125"
                                    ,"background-size": "cover",
                                    "background-repeat": "no-repeat", "background-position": "center"}
                        )
                    ]
                ),
                html.Tbody(id="table-body"),
            ],
            style={"border-collapse": "collapse", "border": "none", "margin-left": "0", "margin-right": "5px"}
        ),
        dcc.Interval(
            id='interval-component',
            interval=2 * 1000,  # update every 5 seconds
            n_intervals=0
        ),
    ],
    className="animate-bottom-container"
)

page_size = 5
current_page = 0
current_rows = []
total_rows = 0

@app.callback(Output("table-body", "children"), [Input("interval-component", "n_intervals")])
def update_table(n):
    global current_page, current_rows, total_rows
    data = get_data()
    total_rows = len(data)
    start_index = current_page * page_size
    end_index = min(start_index + page_size, total_rows)
    rows = []
    for i in range(start_index, end_index):
        row_data = data.iloc[i]
        row_style = {
            "background-image": f"url(assets/test.png)",
            "background-size": "cover",
            "background-repeat": "no-repeat",
            "background-position": "center"
        }
        row_class = "team-row"
        if row_data["playerName"] in current_rows:
            row_class += " fadeIn"
        else:
            row_class += " fadeOut"
        team_name = row_data["teamName"]
        logo_url = f'/assets/logos/{team_name}.png'
        row = html.Tr(
            [
                html.Td(html.Img(src=logo_url, style={"height": "35px", "padding": "5px"}), className="team-logo"),
                html.Td(row_data["playerName"], className="team-name"),
                html.Td(str(row_data["damage"]), className="team-pts"),
            ],
            className=row_class,
            style=row_style,
        )
        rows.append(row)
    table_body = html.Tbody(rows, className="team-row")
    current_rows = data["playerName"].tolist()
    return table_body



if __name__ == "__main__":
    app.run_server(debug=False, port=8052, host="127.0.0.1")