# -----------------------------------------------------------------------
# Author:   Takayoshi Hagiwara (KMD)
# Created:  2024/9/18
# Summary:  A tool for drawing significant differences on a graph created with matplotlib.
#           This tool does not check the statistics of the data.
#           Therefore, significant differences should be checked in advance with some statistical tool.
# -----------------------------------------------------------------------

import matplotlib.pyplot as plt

def significance(text, data, i, j, column_name, x_txt_offset=0, y_txt_offset=0, x_line_offset_l=0, x_line_offset_r=0, y_line_offset_l=0, y_line_offset_r=0, shrink_l=20, shrink_r=20, line_width=1.5, font_size=20, font_weight='bold', ax=None):
    """
    Draw the significant difference on a graph.

    Parameters
    ----------
    text: str
        String to display. 
        e.g. *, **, ***
    data: pandas.DataFrame
        Data.
    i, j: int
        Display the significant difference between the i-th and j-th of the horizontal axis of the graph.
    column_name: str
        Column name set on the horizontal axis.
    x_txt_offset, y_txt_offset: (Optional) int or float
        Offset of the text.
        Default: 0.
    x_line_offset_l, x_line_offset_r, y_line_offset_l, y_line_offset_r: (Optional) int or float
        Offset of the line.
        Default: 0.
    shrink_l, shrink_r: (Optional) int
        Length of vertical line of significant difference. 
        shrinkA is right side, shrinkB is left side.
        Default: 20.
    line_width: (Optional) float
        Line width.
        Default: 1.5
    font_size: (Optional) float
        Font size of the text.
        Default: 20.
    font_weight: (Optional) str
        Weight of the text.
        Default: bold.
    ax: (Optional) matplotlib.axes._subplots.AxesSubplot
        For subplot. Pass the axes object you want to annotate.
        Default: None
    """

    # get axis parameters
    x_ticks, x_tick_labels = plt.xticks()
    y_ticks, y_tick_labels = plt.yticks()

    # calc x location
    x = (x_ticks[i] + x_ticks[j]) / 2

    # calc y location
    y_i = data[data[column_name] == x_tick_labels[i].get_text()].select_dtypes(include='number').max().values[0]
    y_j = data[data[column_name] == x_tick_labels[j].get_text()].select_dtypes(include='number').max().values[0]
    y = max(y_i, y_j)

    # set line properties
    props = {'connectionstyle': 'bar', 'arrowstyle': '-',
            'shrinkA': shrink_r, 'shrinkB': shrink_l, 'linewidth': line_width}
    
    xy_text = (x - len(text)/10/2 + x_txt_offset, y + max(y_ticks)/10 + y_txt_offset)
    xy_line = (x_ticks[i] + x_line_offset_l, y + y_line_offset_l)
    xy_text_line = (x_ticks[j] + x_line_offset_r, y + y_line_offset_r)

    # draw significance line and text
    if ax:
        ax.annotate(text, xy=xy_text, fontsize=font_size, weight=font_weight, zorder=10)
        ax.annotate('', xy=xy_line, xytext=xy_text_line, arrowprops=props)
    else:
        plt.annotate(text, xy=xy_text, fontsize=font_size, weight=font_weight, zorder=10)
        plt.annotate('', xy=xy_line, xytext=xy_text_line, arrowprops=props)