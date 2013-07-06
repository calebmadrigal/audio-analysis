from IPython.core.display import HTML, display
import pylab

def show_audio_player(audio_url, base_path="http://127.0.0.1:8000/"):
    """ Shows an audio player for a given audio file.  But note: if you want ot use
        local files, start a little server to serve them (iPython notebook won't). """

    audio_html = """
    <audio controls>
        <source src="{0}" type="audio/wav">
        Your browser does not support the audio element.
    </audio>""".format(base_path + audio_url)
    display(HTML(audio_html))

def plot_large(*args, **kwargs):
    fig = pylab.figure()
    fig.set_size_inches(14,8)
    pylab.plot(*args, **kwargs)

def specgram_large(*args, **kwargs):
    fig = pylab.figure()
    fig.set_size_inches(14,8)
    pylab.specgram(*args, **kwargs)

