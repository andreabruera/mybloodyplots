import matplotlib
import argparse
import os

from matplotlib import font_manager, pyplot

class MyBloodyPlots():
    def __init__(self, output_folder, font_folder, x_variables, y_variables, x_axis, y_axis, title, labels):
        self.output_folder = output_folder
        self.x_variables = x_variables
        self.y_variables = y_variables
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.title = title
        self.labels = labels
        self.font_selection(font_folder)

    def font_selection(font_folder, font='Helvetica LT Std'):
        # Using Helvetica as a font
        font_folder = os.path.join(os.cwd(), args.font_folder)
        font_dirs = [font_folder, ]
        font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
        font_list = font_manager.createFontList(font_files)
        font_manager.fontManager.ttflist.extend(font_list)
        matplotlib.rcParams['font.family'] = font

    def plot_two_lines(self):

        # Plotting and annotating line 1
        plt.plot(self.x_variables, [v[0] for v in  self.y_variables], label=self.labels[0], marker='o', mec='k', mfc='white', )
        for a, k in zip(self.x_variables, self.y_variables):
            plt.annotate(round(k, 2), (a, k), textcoords='offset points', xytext=(0,10), ha='center')

        # Plotting and annotating line 2
        plt.plot(self.x_variables, [v[1] for v in self.y_variables], label=self.labels[1], marker='o', mec='k', mfc='white')
        for a, k in zip(self.x_variables, [value[1] for value in y_variables]):
            plt.annotate(round(k, 2), (a, k), textcoords='offset points', xytext=(0,10), ha='center')

        # Writing down every single tick
        plt.xticks(self.x_variables, rotation = 45)
    
        # Writing down the title
        plt.title(self.title, fontsize='xx-large')


        # Writing down the axes labels
        plt.xlabel(self.x_axis)
        plt.ylabel(self.y_axis)

        # Adding the legend
        plt.legend()

        # Exporting to output_folder
        plt.tight_layout(pad=3.0)
        plt.savefig(os.path.join(self.output_folder, 'two_lines_plot.png'), transparent=True, dpi=600)
