<!-- This flow div controls the row of logos, matching heights, shifts to columns at small screen size -->
:::::{div}
:class: mx-auto flex flex-col md:flex-row md:items-stretch gap-4 p-4

% example of dark-mode only div
````{div}
:class: flex-1 min-w-0 h-64 items-center justify-center hidden dark:block
```{image} https://raw.githubusercontent.com/ProjectPythia/pythia-config/main/logos/UAlbany.svg
:alt: UAlbany Logo
:align: center
```
````

% example of light-mode only div
````{div}
:class: flex flex-1 min-w-0 h-64 items-center justify-center dark:hidden
```{image} https://raw.githubusercontent.com/ProjectPythia/pythia-config/main/logos/UAlbany.svg
:alt: UAlbany Logo
:align: center
```
````

````{div}
:class: flex flex-1 min-w-0 h-64 items-center justify-center
```{image} https://raw.githubusercontent.com/ProjectPythia/pythia-config/main/logos/NSF-NCAR.png
:alt: NCAR Logo
:align: center
```
````

````{div}
:class: flex flex-1 min-w-0 h-64 items-center justify-center
```{image} https://raw.githubusercontent.com/ProjectPythia/pythia-config/main/logos/NSF-Unidata.png
:alt: Unidata Logo
:align: center
```
````

````{div}
:class: flex flex-1 min-w-0 h-64 items-center justify-center
```{image} https://raw.githubusercontent.com/2i2c-org/2i2c-org.github.io/main/assets/media/logo.svg
:alt: 2i2c Logo
:align: center
:width: 64
```
````{div}
:::::

<!-- This flow div controls the following row of logo + text, matching heights and scaling widths, and shifts to columns at small screen size -->
:::::{div}
:class: mx-auto flex flex-col md:flex-row md:items-stretch gap-4 p-4

% TODO: I think this image width spec could be handled better by the divs - not sure
````{div}
:class: flex items-center justify-center
```{image}https://raw.githubusercontent.com/ProjectPythia/pythia-config/main/logos/nsf.jpg
:alt: NSF Logo
:width: 100
```
````

````{div}
:class: flex-1
The [Project Pythia website](https://projectpythia.org), [Pythia Foundations](https://foundations.projectpythia.org), and the shared [Pythia Cookbook](https://cookbooks.projectpythia.org) infrastructure are based upon work supported by the National Science Foundation awards 2026899, 2026863, 2324302, 2324303 and 2324304. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.
````
:::::
