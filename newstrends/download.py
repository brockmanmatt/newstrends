# AUTOGENERATED! DO NOT EDIT! File to edit: 04_download.ipynb (unless otherwise specified).

__all__ = ['downloadGDELT']

# Cell
def downloadGDELT(filepath, year:"YYYY", month:"MM", day: "DD", hour:"HH"):
    "download and extract .gz, borrowed from https://stackoverflow.com/questions/3548495/download-extract-and-read-a-gzip-file-in-python"

    """
    WARNING: This results in a 1.5gb file per hour, or 30gb/day. Not actually sure best way to go about making this useful.
    """

    url = "http://data.gdeltproject.org/gdeltv3/gfg/alpha/{}{}{}{}0000.LINKS.TXT.gz".format(year, month, day, hour)
    os.makedirs(filepath, exist_ok=True)
    out_file = "{}/{}".format(filepath, url.split("/")[-1][:-3])

    try:
        with urllib.request.urlopen(url) as response:
            with gzip.GzipFile(fileobj=response) as uncompressed:
                file_content = uncompressed.read()

            with open(out_file, 'wb') as f:
                f.write(file_content)
                return file_content


    except Exception as e:
        print(e)
        return -1
