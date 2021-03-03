import dash_bootstrap_components as dbc

def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Tab 1", href="/")),
            dbc.NavItem(dbc.NavLink("Tab 2", href="/")),
        ],
        brand="IPL Data",
        color="primary",
        dark=True,
    )
    return navbar