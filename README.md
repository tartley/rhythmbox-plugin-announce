# Announce

A Rhythmbox plugin which uses a speech synthesiser to announce the title of
each new song as it starts playing.

If the song is from a different album than the previous track, then it
announces the album too. Likewise for the artist.


# Install

Install the 'espeak' speech synthesiser:

    sudo apt-get install espeak

Clone this repo, if you haven't already:

    cd /tmp
    git clone https://github.com/tartley/rhythmbox-plugin-announce.git
    cd rhythmbox-plugin-announce

Then install the plugin:

    cp announce* ~/.local/share/rhythmbox/plugins
