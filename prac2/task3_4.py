# plotly_charts.py
import plotly.graph_objs as go
import pandas as pd


def create_bar_chart(data, features):
    """Создание столбчатой диаграммы (Задание 3)"""
    print("\n" + "=" * 50)
    print("ЗАДАНИЕ 3: Построение столбчатой диаграммы")
    print("=" * 50)

    df_for_bar = data.groupby('target_name')[features[0]].mean().reset_index()

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df_for_bar['target_name'],
        y=df_for_bar[features[0]],
        marker=dict(
            color=df_for_bar[features[0]],
            coloraxis="coloraxis",
            line=dict(color='black', width=2)
        )
    ))

    fig.update_layout(
        title=dict(text=f'Среднее значение "{features[0]}" по классам вина', font_size=20, x=0.5, xanchor='center'),
        xaxis_title='Класс вина',
        yaxis_title=f'Ср. значение {features[0]}',
        xaxis=dict(tickangle=315, tickfont=dict(size=14)),
        yaxis=dict(tickfont=dict(size=14)),
        height=700,
        coloraxis=dict(colorscale='Viridis'),
        plot_bgcolor='white',
        margin=dict(l=0, r=0, t=40, b=0)
    )
    fig.update_yaxes(showgrid=True, gridwidth=2, gridcolor='ivory')

    fig.write_html("plotly_bar.html")
    print("Столбчатая диаграмма сохранена в файл 'plotly_bar.html'")


def create_pie_chart(data):
    """Создание круговой диаграммы (Задание 4)"""
    print("\n" + "=" * 50)
    print("ЗАДАНИЕ 4: Построение круговой диаграммы")
    print("=" * 50)

    class_counts = data['target_name'].value_counts()

    fig_pie = go.Figure()
    fig_pie.add_trace(go.Pie(
        labels=class_counts.index,
        values=class_counts.values,
        marker=dict(line=dict(color='black', width=2))
    ))

    fig_pie.update_layout(
        title=dict(text='Распределение выборки по классам вина', font_size=20, x=0.5, xanchor='center'),
        height=700
    )

    fig_pie.write_html("plotly_pie.html")
    print("Круговая диаграмма сохранена в файл 'plotly_pie.html'")


if __name__ == "__main__":
    from task1_2 import load_and_preprocess_data

    data, X_scaled, y, features = load_and_preprocess_data()
    create_bar_chart(data, features)
    create_pie_chart(data)