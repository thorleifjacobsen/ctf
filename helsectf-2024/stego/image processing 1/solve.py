from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load image using PIL
img_data = Image.open('ekorn.png')

ft = np.fft.fft2(img_data)
fshift = np.fft.fftshift(ft)
spectrum = np.log(np.abs(fshift))

# Found this on google to show the thingy.
plt.imshow(spectrum, cmap='gray')
plt.title('Solution')
plt.colorbar()
#plt.savefig('spectrum.png')
plt.show()
