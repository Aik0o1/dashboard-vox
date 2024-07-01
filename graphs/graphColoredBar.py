import plotly.express as px
def plotColorodBar():
    df = px.data.tips()
    fig = px.histogram(df, x="sex", y="total_bill",
                color='smoker', barmode='group',
                height=350)
    
    return fig