import matplotlib.pyplot as plt
import numpy as np

TICKSIZE = 15
TITLESIZE = 25
DPI = 600

def calculate_dmg_parts(value_array):
    exp_base_damage = value_array[1]*value_array[3] # BaseDamage * chance2Hit
    exp_crit_damage = value_array[2]*value_array[4] # CritDamage * chance2Crit
    return [exp_base_damage, exp_crit_damage]

def modify_data_4_plot(data_dictionary):
    exp_base_damages = []
    exp_crit_damages = []

    for value in data_dictionary:
        plot_data = calculate_dmg_parts(data_dictionary[value])
        exp_base_damages.append(plot_data[0])
        exp_crit_damages.append(plot_data[1])
    
    plot_dict = {
        "Expected Base Damage":exp_base_damages,
        "Expected Crit Damage":exp_crit_damages,
    }

    return plot_dict

def draw_stacked_bar_plot(plot_dict, labels, title):
    fig, ax = plt.subplots(figsize=(12,10), layout="constrained")
    bottom = np.zeros(len(labels))
    width = 0.5

    for dmgType, dmgValue in plot_dict.items():
        p = ax.bar(x=labels, height=dmgValue, width=width, label=dmgType, bottom=bottom)
        ax.bar_label(p, label_type="center", fontsize=TICKSIZE-1)
        bottom += dmgValue
    ax.bar_label(p, padding=7, fontsize=TICKSIZE)
    ax.set_title(f"{title}", fontsize=TITLESIZE)
    ax.legend(loc="upper left", fontsize=TICKSIZE)

    return fig, ax

def stacked_bar_plot_from_dict(data_dictionary, title):
    plot_dict = modify_data_4_plot(data_dictionary)
    fig, ax = draw_stacked_bar_plot(plot_dict, labels=list(data_dictionary.keys()), title=title)
    return fig, ax, plot_dict