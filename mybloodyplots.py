import matplotlib
import argparse
import os
import numpy

from matplotlib import font_manager, pyplot

class MyBloodyPlots():
    def __init__(self, output_folder, font_folder, x_variables, y_variables, x_axis, y_axis, title, labels, identifier, colors, y_invert=False, y_ticks=[], x_ticks=True, y_grid=False, y_lim=[], y_err=[], text_coords=[]):
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
        self.bar_width = 0.2
        self.y_grid = y_grid
        self.y_lim = y_lim
        self.y_err = y_err
        self.text_coords = text_coords 
        pyplot.figure(figsize=[10, 5])

    def font_selection(self, font_folder='fonts', font='Helvetica LT Std'):
        # Using Helvetica as a font
        font_folder = self.font_folder
        font_dirs = [font_folder, ]
        font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
        for p in font_files:
            font_manager.fontManager.addfont(p)
        matplotlib.rcParams['font.family'] = font

    def plot_one_line(self):

        # Plotting and annotating line 1
        pyplot.plot(self.x_variables, [v[0] for v in  self.y_variables], label=self.labels[0], marker='o', mec='k', mfc='white', color=self.colors[0])
        for a, k in zip(self.x_variables, [value[0] for value in self.y_variables]):
            pyplot.annotate(round(k, 2), (a, k), textcoords='offset points', xytext=(0,10), ha='center')

    def plot_two_lines(self):

        # Plotting and annotating line 1
        pyplot.plot(self.x_variables, [v[0] for v in  self.y_variables], label=self.labels[0], marker='o', mec='k', mfc='white', color=self.colors[0])
        for a, k in zip(self.x_variables, [value[0] for value in self.y_variables]):
            pyplot.annotate(round(k, 2), (a, k), textcoords='offset points', xytext=(0,10), ha='center')


        # Plotting and annotating line 2
        pyplot.plot(self.x_variables, [v[1] for v in self.y_variables], label=self.labels[1], marker='o', mec='k', mfc='white', color=self.colors[1])
        for a, k in zip(self.x_variables, [value[1] for value in self.y_variables]):

            if len(self.text_coords) > 0:
                text_coords = self.text_coords
            else:
                text_coords = (0, 10)
            pyplot.annotate(round(k, 2), (a, k), textcoords='offset points', xytext=text_coords, ha='center')
    
    def plot_two_lines_with_errorbars(self):

        # Plotting and annotating line 1
        pyplot.plot(self.x_variables, [v[0] for v in  self.y_variables], label=self.labels[0], marker='o', mec='k', mfc='white', color=self.colors[0])
        for a, k in zip(self.x_variables, [value[0] for value in self.y_variables]):
            pyplot.annotate(round(k, 2), (a, k), textcoords='offset points', xytext=(0,-10), ha='center')

        pyplot.errorbar([k for k in range(len(self.x_variables))],[v[0] for v in  self.y_variables], yerr=[v[0] for v in self.y_err], ecolor='black', elinewidth=0.2, capsize=1, fmt = 'h', marker='o')

        # Plotting and annotating line 2
        pyplot.plot(self.x_variables, [v[1] for v in self.y_variables], label=self.labels[1], marker='o', mec='k', mfc='white', color=self.colors[1])
        for a, k in zip(self.x_variables, [value[1] for value in self.y_variables]):
            pyplot.annotate(round(k, 2), (a, k), textcoords='offset points', xytext=(0,10), ha='center')

        pyplot.errorbar([k for k in range(len(self.x_variables))],[v[1] for v in  self.y_variables], yerr=[v[1] for v in self.y_err], ecolor='black', elinewidth=0.2, capsize=1, fmt = 'h', marker='o')

    def plot_three_bars(self):

        # Reorganizing the data

        x_one = [k for k in range(len(self.x_variables))]
        x_two = [k + self.bar_width for k in x_one]
        x_three = [k + self.bar_width for k in x_two]
        x_var = [x_one, x_two, x_three]
        data = [(x_var[index], self.y_variables[index]) for index in range(len(x_var))]

        for variables_tuple, bar_color, bar_label in zip(data, self.colors, self.labels):
            pyplot.bar(variables_tuple[0], variables_tuple[1], width=self.bar_width, edgecolor='white', linewidth=2., color=bar_color, label=bar_label)

    def plot_histogram_two_sets(self):
        quantile = int(max(numpy.quantile(self.y_variables[0], 1), numpy.quantile(self.y_variables[1], 1)))
        pyplot.hist([self.y_variables[0], self.y_variables[1]], bins = numpy.arange(quantile)+1, range = (0, quantile), label=self.labels, align='mid', edgecolor='white', color=self.colors, linewidth=1., width=.4)
        
    def plot_errorbar_two_sets(self):

        one_x = [k - 0.1 for k in range(len(self.x_variables))]
        one_y = [v[0] for v in self.y_variables[0]]
        one_yerr = [v[1] for v in self.y_variables[0]]
        pyplot.errorbar(one_x, one_y, yerr=one_yerr, ecolor='black', elinewidth=0.2, capsize=1, fmt = 'h', label=self.labels[0], color=self.colors[0], mec='k', marker='o')

        two_x = [k + 0.1 for k in range(len(self.x_variables))]
        two_y = [v[0] for v in self.y_variables[1]]
        two_yerr = [v[1] for v in self.y_variables[1]]
        pyplot.errorbar(two_x, two_y, yerr=two_yerr, ecolor='black', elinewidth=0.2, capsize=1, fmt = 'h', label=self.labels[1], color=self.colors[1], mec='k', marker='o')

    def plot_dat(self, plot_type):


        if plot_type == 'one_line':
            self.plot_one_line()
        if plot_type == 'two_lines':
            self.plot_two_lines()
        if plot_type == 'two_lines_with_errorbars':
            self.plot_two_lines_with_errorbars()
        elif plot_type == 'three_bars':
            self.plot_three_bars()
        elif plot_type == 'histogram_two_sets':
            self.plot_histogram_two_sets()
        elif plot_type == 'errorbar_two_sets':
            self.plot_errorbar_two_sets()

        # Writing down every single tick in the x axis
        if self.x_ticks:
            if plot_type == 'three_bars':
                pyplot.xticks([k + self.bar_width for k in range(len(self.x_variables))], self.x_variables, rotation = 45, fontsize='large', fontweight='bold')
            if plot_type == 'histogram_two_sets':
                pyplot.xticks(fontweight='bold')
            else:
                pyplot.xticks([k for k in range(len(self.x_variables))], self.x_variables, rotation = 45, fontsize='large', fontweight='bold')
        else:
            pyplot.xticks([])

        # Writing down every single tick in the y axis

        if type(self.y_ticks) == 'list' and len(self.y_ticks) > 0:
            pyplot.yticks = self.y_ticks
        if self.y_ticks == True:
            pass
        else:
            pyplot.yticks([])

        # Inverting the y axis

        if self.y_invert:
            bottom, top = pyplot.ylim()
            pyplot.ylim(top, bottom)    

        # Plotting the y grid lines in the back

        if self.y_grid:
            pyplot.grid(axis='y', alpha=0.3)

        # Setting ylim

        if len(self.y_lim) > 0:
            pyplot.ylim(self.y_lim)


        # Writing down the title

        if plot_type != 'histogram_two_sets':
            pyplot.title(self.title, fontsize='x-large', fontweight='bold', pad=50., wrap=True, multialignment='left')
        else:        
            pyplot.title(self.title, fontsize='x-large', fontweight='bold', wrap=True, multialignment='left')

        # Writing down the axes labels

        if len(self.x_axis) > 0:
            pyplot.xlabel(self.x_axis, fontweight='bold')
        if len(self.y_axis) > 0:
            pyplot.ylabel(self.y_axis, fontsize='large', fontweight='bold')

        # Adding the legend

        legend_properties = {'weight':'bold'}
        if plot_type != 'histogram_two_sets':
            pyplot.legend(bbox_to_anchor=(1, 1.2), ncol=len(self.labels), prop=legend_properties)
        else:
            pyplot.legend(prop=legend_properties)

        # Exporting to output_folder

        pyplot.box(False)
        pyplot.tight_layout(pad=2.5)
        pyplot.savefig(os.path.join(self.output_folder, '{}_{}.png'.format(self.identifier, plot_type)), dpi=600)
        pyplot.clf()
        pyplot.cla()
        pyplot.close()
