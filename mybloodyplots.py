import matplotlib
import argparse
import os

from matplotlib import font_manager, pyplot

class MyBloodyPlots():
    def __init__(self, output_folder, font_folder, x_variables, y_variables, x_axis, y_axis, title, labels, identifier, colors, y_invert=False, y_ticks=False, x_ticks=True):
        self.output_folder = output_folder
        self.font_folder = font_folder
        self.identifier = identifier
        self.x_variables = x_variables
        self.y_variables = y_variables
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.title = title
        self.labels = labels
        self.font_selection(self.font_folder)
        self.colors = colors
        self.y_invert = y_invert
        self.x_ticks = x_ticks
        self.y_ticks = y_ticks

    def font_selection(self, font_folder='fonts', font='Helvetica LT Std'):
        # Using Helvetica as a font
        font_folder = self.font_folder
        font_dirs = [font_folder, ]
        font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
        font_list = font_manager.createFontList(font_files)
        font_manager.fontManager.ttflist.extend(font_list)
        matplotlib.rcParams['font.family'] = font

    def plot_two_lines(self):

        # Plotting and annotating line 1
        pyplot.plot(self.x_variables, [v[0] for v in  self.y_variables], label=self.labels[0], marker='o', mec='k', mfc='white', color=self.colors[0])
        for a, k in zip(self.x_variables, [value[0] for value in self.y_variables]):
            pyplot.annotate(round(k, 2), (a, k), textcoords='offset points', xytext=(0,10), ha='center')


        # Plotting and annotating line 2
        pyplot.plot(self.x_variables, [v[1] for v in self.y_variables], label=self.labels[1], marker='o', mec='k', mfc='white', color=self.colors[1])
        for a, k in zip(self.x_variables, [value[1] for value in self.y_variables]):
            pyplot.annotate(round(k, 2), (a, k), textcoords='offset points', xytext=(0,10), ha='center')

        # Writing down every single tick in the x axis
        if self.x_ticks:
            pyplot.xticks(self.x_variables, rotation = 45)
        else:
            pyplot.xticks([])

        # Writing down every single tick in the y axis
        if not self.y_ticks:
            pyplot.yticks([])

        # Inverting the y axis

        if self.y_invert:
            bottom, top = pyplot.ylim()
            pyplot.ylim(top, bottom)    
        # Writing down the title
        pyplot.title(self.title, fontsize='xx-large', fontweight='bold', pad=30.)


        # Writing down the axes labels
        if len(self.x_axis) > 0:
            pyplot.xlabel(self.x_axis)
        if len(self.y_axis) > 0:
            pyplot.ylabel(self.y_axis, fontsize='large', fontweight='bold')

        # Adding the legend
        pyplot.legend()

        # Exporting to output_folder
        pyplot.box(False)
        pyplot.tight_layout(pad=2.0)
        pyplot.savefig(os.path.join(self.output_folder, '{}_two_lines_plot.png'.format(self.identifier)), transparent=True, dpi=600)
        pyplot.clf()
        pyplot.cla()
