Image encryption: by the original image and the key image by bitwise XOR
operation

Image decryption:definition: the encrypted image and the key image in
the secondary bitwise XOR operation

First Step:Load the image and convert it to NumPy array format. SHAPE is
image (height, width, number of channels)

Second Step:Returns a random integer.

Third Step:Each pixel value in the image performs a binary XOR operation
using the random integer number returned in the previous step.

Fourth Step:According to the results
