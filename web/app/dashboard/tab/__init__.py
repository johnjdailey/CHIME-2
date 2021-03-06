# -*- coding: utf-8 -*-
"""Card tabs, brings together various tabs."""
import dash_bootstrap_components as dbc
import dash_html_components as html

from app.dashboard.tab import census, parameter, report, upload  # noqa

content = dbc.Card(
    [
        dbc.CardHeader(
            [
                dbc.Tabs(
                    [
                        dbc.Tab(label="Model Parameters", tab_id="parameter-tab"),
                        dbc.Tab(label="Census Data", tab_id="census-tab"),
                        dbc.Tab(label="Upload .csv", tab_id="upload-tab"),
                        dbc.Tab(label="Generate Report", tab_id="report-tab"),
                    ],
                    id="card-tabs",
                    card=True,
                    active_tab="parameter-tab",
                )
            ]
        ),
        dbc.CardBody([html.Div(id="card-content")]),
    ]
)
