# countparticles

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4139778.svg)](https://doi.org/10.5281/zenodo.4139778)

Report the number of particles in each class from a `run_data.star` file
produced by RELION.

A single-particle cryo-EM reconstruction comes from a set of particle images
corresponding to projections of identical particles in different orientations.
All datasets are heterogeneous, to various degrees, and data analysis involves
classification of particle images. Knowing how many particles contributed to
any given class is important to decide how to follow up after a classification
job. This command-line tool reports a count of particles in each class in a
`run_it???_data.star` file from a RELION Class2D or Class3D job. It can also
optionally produce a bar plot of these particle counts.

## Acknowledgments

I would not have been able to put this tool together without the
[`starfile`](https://github.com/alisterburt/starfile) library.

## Installation

```
$ pip install countparticles
```

## Usage

```
$ countparticles --help
Usage: countparticles [OPTIONS] <run_data.star>

  Report the number of particles in each class from a run_data.star file
  produced by RELION.

Options:
  -p, --plot         Optional. Display a bar plot of the particle counts. This
                     is most helpful with only a few classes, e.g. for typical
                     Class3D results (but not for typical Class2D results with
                     many classes).

  -o, --output TEXT  Optional. File name to save the barplot (recommended file
                     formats: .png, .pdf, .svg or any format supported by
                     matplotlib). This option has no effect without the
                     -p/--plot option.

  -h, --help         Show this message and exit.
```
