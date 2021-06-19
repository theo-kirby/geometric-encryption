
# Geometric-Encryption

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)   [![Language Python](https://img.shields.io/badge/language-Python3-green)]()


This project implements basic encryption techniques to encode and visualize text data using python3

    - Goal : to experiment with and understand how python deals with reading and writing files, to create something interesting that can produce eye-catching visuals
    - Capabilities : encode text files as basic vector coordinates, decode back into plaintext, accept command line arguments for file i/o, visualize data via matplotlib and blender 
    - Usage >


## Run Locally

Clone the project

```bash
  git clone https://github.com/theo-kirby/geometric-encryption
```

Go to the project directory

```bash
  cd geometric-encryption
```

Install dependencies

```bash
  pip3 install -r Resources/requirements.txt

```

Encrypt (p.csv) -> (c.csv)
```bash
python3 Encrypt.py -i p.csv -o c.csv
```

Decrypt (c.csv) -> (p.csv)
```bash
python3 Decrypt.py
```

  
## Screenshots

![App Screenshot](Resources/images/Cryptography_Reference.png)
![App Screenshot](Resources/images/Visualizations.png)
![App Screenshot](Resources/images/Encrypt_Decrypt_Functions.png)

  
