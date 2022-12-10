## Filter C (from CS50 course Problem Set 4)

#### Description 
Program that applies filters to BMPs.

#### Technologies used:
- *C*

#### Usage example
```
$ ./filter -r IMAGE.bmp REFLECTED.bmp
```
where IMAGE.bmp is the name of an image file and REFLECTED.bmp is the name given to an output image file, now reflected.

#### List of filters:
- -g (Grayscale). Example: ```$ ./filter -g INFILE.bmp OUTFILE.bmp```
- -s (Sepia). Example: ```$ ./filter -s INFILE.bmp OUTFILE.bmp```
- -r (Reflect). Example: ```$ ./filter -r INFILE.bmp OUTFILE.bmp```
- -b (Blur). Example: ```$ ./filter -b INFILE.bmp OUTFILE.bmp```

#### List of images:
- ```yard.bmp```
- ```stadium.bmp```
- ```tower.bmp```
- ```yard.bmp```

#### Contributing
Pull requests are welcome. For major changes please open an issue first to discuss what you would like to change.
