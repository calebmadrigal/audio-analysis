# Some code copied from:
# http://nbviewer.ipython.org/urls/raw.github.com/Carreau/posts/master/07-the-sound-of-hydrogen.ipynb
#
# This is a wrapper that take a filename and publish an html <audio> tag to listen to it

import StringIO
import base64
from IPython.core.display import HTML, display
import scikits.audiolab as audio
import numpy as np
import struct
import sys

def wavPlayer(data, rate):
    """ will display html 5 player for compatible browser

    The browser need to know how to play wav through html5.

    there is no autoplay to prevent file playing when the browser opens
    
    Adapted from SciPy.io.
    """
    
    buffer = StringIO.StringIO()
    buffer.write(b'RIFF')
    buffer.write(b'\x00\x00\x00\x00')
    buffer.write(b'WAVE')

    buffer.write(b'fmt ')
    if data.ndim == 1:
        noc = 1
    else:
        noc = data.shape[1]
    bits = data.dtype.itemsize * 8
    sbytes = rate*(bits // 8)*noc
    ba = noc * (bits // 8)
    buffer.write(struct.pack('<ihHIIHH', 16, 1, noc, rate, sbytes, ba, bits))

    # data chunk
    buffer.write(b'data')
    buffer.write(struct.pack('<i', data.nbytes))

    if data.dtype.byteorder == '>' or (data.dtype.byteorder == '=' and sys.byteorder == 'big'):
        data = data.byteswap()

    buffer.write(data.tostring())
    # Determine file size and place it in correct
    #  position at start of the file.
    size = buffer.tell()
    buffer.seek(4)
    buffer.write(struct.pack('<i', size-8))
    
    val = buffer.getvalue()
    
    src = """
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>Simple Test</title>
    </head>
    
    <body>
    <audio controls="controls" style="width:600px" >
      <source controls src="data:audio/wav;base64,{base64}" type="audio/wav" />
      Your browser does not support the audio element.
    </audio>
    </body>
    """.format(base64=base64.encodestring(val))
    display(HTML(src))


def show_wave_player(file_path):
    (input_signal, sample_rate, bits) = audio.wavread(file_path)
    wav_data = input_signal.astype(np.int16)
    wavPlayer(wav_data, sample_rate)

