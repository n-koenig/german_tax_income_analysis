# Project Overview

This project presents an exploratory data analysis of the federal tax income of the Federal Republic of Germany using data provided by the Federal Statistics Office of Germany.

- `data/` contains only raw data downloaded directly from the statistics office's website
- `results/` contains transformed data and figures
- `bin/` contains notebooks and the necessary helper functions to run the notebooks
- `docs/` directory contains background information and pdf/html-exported versions of the notebook

# Installation

Use any package you like to install the required packages from the given requirements, e.g.

```
conda create -n rse-test --file requirements.txt
```

# Usage

The [computational narrative notebook](./bin/computational_narrative.ipynb) can be used and run as is to explore the analyzed results. The [exploration notebook](./bin/exploration.ipynb) notebook can be used for further testing.

To create the html or pdf documents, simply run

```
jupyter nbconvert bin/computational_narrative.ipynb --to pdf --no-input --output-dir docs/
```

or 

```
jupyter nbconvert bin/computational_narrative.ipynb --to html --output-dir docs/
```

# Documentation

The `docs/` directory contains a more detailed description of the [project motivation](./docs/project_discription.md), as well as a [pdf](./docs/computational_narrative.pdf) and [html](./docs/computational_narrative.html) version of the computational narrative notebook.

# License

Usage permitted under MIT License. More information [provided here](./LICENSE.md).

# Contact Information

Please write to [nikoenig@uni-potsdam.de](mailto:nikoenig@uni-potsdam.de) for any further questions.