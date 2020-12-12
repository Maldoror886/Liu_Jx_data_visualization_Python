import matplotlib.pyplot as plt
# total medal
labels = ['women', 'man' ]
values = [1825, 3944]
displace = [0.2, 0]
# Create pie chart here
plt.pie(values, labels=labels,explode=displace)

plt.show()



import matplotlib.pyplot as plt
#total gold medal
labels = ['women', 'man' ]
values = [582, 1337]
colors = ["green", "purple"]
displace = [0.2, 0]

# Create pie chart here
plt.pie(values, labels=labels, colors=colors, explode=displace)

plt.show()



#Number of women in the various competitions
import pyecharts.options as opts
from pyecharts.charts import Line


x_data = ["Biathlon", "Bobsleight", "Curling", "Ice Hockey", "Luge", "Skating", "Skiing"]
y_data = [150, 36, 75, 305, 45, 564, 651]


(
    Line()
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="",
        y_axis=y_data,
        symbol="emptyCircle",
        is_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .render("basic_line_chart.html")
)

# women

import pyecharts.options as opts
from pyecharts.charts import Scatter


data = [
    [1924, 6],
    [1928, 6],
    [1932, 6],
    [1936, 9],
    [1948, 15],
    [1952, 18],
    [1956, 27],
    [1960, 39],
    [1964, 46],
    [1968, 46],
    [1972, 45],
    [1976, 51],
    [1980, 51],
    [1984, 54],
    [1988, 63],
    [1992, 99],
    [1994, 111],
    [1998, 189],
    [2002, 208],
    [2006, 232],
    [2010, 233],
    [2014, 272],

]
data.sort(key=lambda x: x[0])
x_data = [d[0] for d in data]
y_data = [d[1] for d in data]

(
    Scatter(init_opts=opts.InitOpts(width="1600px", height="1000px"))
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="",
        y_axis=y_data,
        symbol_size=20,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_series_opts()
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(
            type_="value", splitline_opts=opts.SplitLineOpts(is_show=True)
        ),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        tooltip_opts=opts.TooltipOpts(is_show=False),
    )
    .render("basic_scatter_chart.html")
)
