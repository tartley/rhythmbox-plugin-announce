# Announce

A Rhythmbox plugin which uses a speech synthesiser to announce the title of
each new song as it starts playing.

If the album or artist is different from the previous track, then it
announces those, too.


# Install

Install the 'espeak' speech synthesiser:

    sudo apt-get install espeak

Clone this repo, if you haven't already:

    cd /tmp
    git clone https://github.com/tartley/rhythmbox-plugin-announce.git
    cd rhythmbox-plugin-announce

Then install the plugin:

    cp announce* ~/.local/share/rhythmbox/plugins

# Contact

Jonathan Hartley
Email: tartley@tartley.com
Twitter: @tartley
