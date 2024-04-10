import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(
    page_title="竞赛网站",
    # page_icon="👋",
    layout='wide',
)

st.write("# 用户行为分析！ 👋")

radar_data = pd.read_csv('./rander_data.csv').T
data = pd.read_csv('./mode_data3.csv')
names =["一般价值客户", "低价值客户", "流失客户", "重要发展客户", "重要保持客户"]
categories = radar_data.index
fig = go.Figure()
for i in radar_data.columns:
    fig.add_trace(go.Scatterpolar(
          r=radar_data[i].values,
          theta=categories,
          fill='toself',
          name=names[i]
    ))
fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[radar_data.values.min(), radar_data.values.max()]
    )),
  # showlegend=False
)
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig)
with col2:
    data['客户类别'] = data['客户类别'].map({i:j for i, j in enumerate(names)})
    options = st.multiselect(
        '客户群体',  names)
    ind = data['客户类别'].apply(lambda x: x in options)
    st.dataframe(data.loc[ind, :])