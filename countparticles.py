import starfile as star
import matplotlib.pyplot as plt
import click

# Building blocks

def load_particles(starfile):
    """Load rlnClassNumber column from a run_data.star file."""
    star_data = star.open(starfile)
    particles = star_data[1]['rlnClassNumber']
    return particles

def count_particles(particles):
    """Count particles in each class."""
    total = len(particles)
    class_indices = particles.value_counts().index
    particle_counts = particles.value_counts()
    fractions_of_total = particles.value_counts(normalize=True) * 100
    return total, class_indices, particle_counts, fractions_of_total

def print_table(total, class_indices, particle_counts, fractions_of_total):
    """Pretty-print a count and frequency table from a raw classes vector."""
    print('Total number of particles:', total)
    print('Class', 'Particles', '% of total', sep='\t')
    for (index, count, fraction) in zip(class_indices, particle_counts, fractions_of_total):
        print(index, '\t', count, '\t\t', f'{fraction:.2f}', sep='')

def build_barplot(class_indices, particle_counts, starfile):
    """Builds a bar plot of particle counts per class."""
    fig, ax = plt.subplots()
    ax.bar(class_indices, particle_counts)
    ax.set_xlabel('Class')
    ax.set_ylabel('Number of particles')
    ax.set_title(f'Class distribution of {starfile}')
    ax.yaxis.grid(True)
    ax.xaxis.grid(False)
    ax.set_xticks(class_indices)
    fig.tight_layout()
    return fig

# Command-line tool made from the buidling blocks

@click.command(context_settings = dict(help_option_names=['-h', '--help']))
@click.argument('starfile', metavar='<run_data.star>')
@click.option('-p', '--plot', 'plot', is_flag=True, help='Optional. Display a bar plot of the particle counts. This is most helpful with only a few classes, e.g. for typical Class3D results (but not for typical Class2D results with many classes).')
@click.option('-o', '--output', 'output_file', help='Optional. File name to save the barplot (recommended file formats: .png, .pdf, .svg or any format supported by matplotlib). This option has no effect without the -p/--plot option.')
def cli(starfile, plot, output_file):
    """Report the number of particles in each class from a run_data.star file produced by RELION."""
    print('Analyzing star file:', starfile)
    particles = load_particles(starfile)
    total, class_indices, particle_counts, fractions_of_total = count_particles(particles)
    print_table(total, class_indices, particle_counts, fractions_of_total)
    if plot:
        if len(class_indices) > 10:
            print('NOTE: Looks like you have many classes. Plot might take a long time to appear.')
            print('NOTE: This bar plot is not very informative with that many classes.')
            print('NOTE: It is most helpful for typical Class3D results (few classes).')
            print('NOTE: It is not so helpful for typical Class2D results (many classes).')
        barplot = build_barplot(class_indices, particle_counts, starfile)
        if output_file:
            barplot.figsize = (11.80, 8.85)
            barplot.dpi = 300
            plt.savefig(output_file)
        else:
            plt.show()
