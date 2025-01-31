from django.shortcuts import render

# Create your views here.

def index(request):
    

    context = {
        "preferences": {
            "color-scheme": "dark", # dark/light
            "show-note-names": "none", # inside/below/none
            "show-pedal": "true", # true/false
            "show-note": "true", # true/false
            "show-octave": "true", # true/false    # if show-note == true
            "show-staff": "true", # true/false
            "show-chord": "true", # true/false
            "show-chord-function": "true",
            "key": "C", # C, C#, Db, D, D#, Eb, E, F, F#, Gb, G, G#, Ab, A, A#, Bb, B   # if show-chord-function == true
            "key-type": "major", # major, minor, harmonic-minor, melodic-minor  # if show-chord-function == true
        }
    }
    return render(request, "piano/index.html", context)