# nmr-v5

### Python / Conda Environment
The packages, including versions, are documented in the `environment.yml` file.
The `environment.yml` file is created using:
```console
conda env export --no-builds | grep -v '^prefix:' > environment.yml
```
(The grep removes the prefix, which is only useful on a specific machine.)

The environment can be replicated from this yaml file using:
```console
conda env create -f environment.yml
```
