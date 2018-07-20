<img src="./images/logo.png" align="right" title="MOVIAOW logo" width="240"/>

MOVIAOW
====




This is a python program to generate a webpage showing trailers of the latest movies of 2018.

## How It Works

- **media.py** defines the `Movie` class, which has the following attributes:
- - title
  - poster_image_url
  - trainler_youtube_url
- **fresh_tomatoes.py** defines a set of functions to generate and open a web page;
- **entertainment_center.py** creates `Movie` objects, then generates and open a web page by calling `open_movies_page()` function defined in **fresh_tomatoes.py**.


## Usage

If you just want to check the web page, simply go the directory containing the `HTML` file of `index.html` and open it with your browser. Then, enjoy it.

Or, if you want to rebuild the whole page, you can open your terminal and run the following commands:

```bash
$ python entertainment_center.py
```

which will generate a web page named `index.html` and then open it using you browser.

## Contribute

Contributions are always welcome! Please read the [contribution guidelines](#TBA) first.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)


