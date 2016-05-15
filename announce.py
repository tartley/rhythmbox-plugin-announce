import subprocess
from gi.repository import GObject, RB, Peas


def espeak(text):
    subprocess.Popen(['espeak', text])


prev_album = None
prev_artist = None

def announce(title, album, artist):
    global prev_album, prev_artist
    espeak('{}{}{}'.format(
        title,
        ', from {}'.format(album) if album != prev_album else '',
        ', by {}'.format(artist) if artist != prev_artist else '',
    ))
    prev_album = album
    prev_artist = artist


class AnnouncePlugin(GObject.Object, Peas.Activatable):

    object = GObject.property(type=GObject.Object)

    def __init__(self):
        super().__init__()
        self.prev_entry = None

    def do_activate(self):
        self.player = self.object.props.shell_player
        self.handler = self.player.connect(
            'playing-changed', self.on_playing_changed
        )
        espeak('Activated')

    def do_deactivate(self):
        self.player.disconnect(self.handler)
        espeak('Deactivated')

    def on_playing_changed(self, player, playing):
        entry = self.player.get_playing_entry()
        if playing and entry != self.prev_entry:
            announce(
                entry.get_string(RB.RhythmDBPropType.TITLE),
                entry.get_string(RB.RhythmDBPropType.ALBUM),
                entry.get_string(RB.RhythmDBPropType.ARTIST),
            )
        self.prev_entry = entry

