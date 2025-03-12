import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')

# Clean data
a =df['value'].quantile(0.025)
b= df['value'].quantile(0.975)
df = df[(df['value'] >= a)]
df=df[ df['value'] <=b ]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(10, 6))
     
    ax.plot(df.index, df['value'], color='red', linewidth=1)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019", fontsize=14)
    ax.set_xlabel("Date", fontsize=14)
    ax.set_ylabel("Page Views", fontsize=14)
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['year'] = df_bar['date'].dt.year
    df_bar['month'] = df_bar['date'].dt.strftime('%B')  # Full month name
    df_gr = df_bar.groupby(['year', 'month'], sort=False)['value'].mean().reset_index()
    month_order = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    df_gr['month'] = pd.Categorical(df_gr['month'], categories=month_order, ordered=True)
    fig, ax = plt.subplots(figsize=(14, 8))
    sns.barplot(
        x='year',
        y='value',
        data=df_gr,
        hue='month',
        ax=ax
    )
    ax.set_title("Average Daily Page Views per Month", fontsize=16)
    ax.set_xlabel("Years", fontsize=14)
    ax.set_ylabel("Average Page Views", fontsize=14)
    ax.legend(title="Months")
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

   
    ax.set_title("Average Daily Page Views per Month")
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title="Months", fontsize=10, title_fontsize=12)




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    month_order = [
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    df_box['month'] = pd.Categorical(df_box['month'], categories=month_order, ordered=True)
    fig, axes = plt.subplots(1, 2, figsize=(18, 6))
    sns.boxplot(
        x='year',
        y='value',
        data=df_box,
        ax=axes[0],
        palette='Set2'
    )
    axes[0].set_title("Year-wise Box Plot (Trend)", fontsize=16)
    axes[0].set_xlabel("Year", fontsize=14)
    axes[0].set_ylabel("Page Views", fontsize=14)
    sns.boxplot(
        x='month',
        y='value',
        data=df_box,
        ax=axes[1],
        palette='Set3'
    )
    axes[1].set_title("Month-wise Box Plot (Seasonality)", fontsize=16)
    axes[1].set_xlabel("Month", fontsize=14)
    axes[1].set_ylabel("Page Views", fontsize=14)
    axes[1].tick_params(axis='x', rotation=45)
   



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
