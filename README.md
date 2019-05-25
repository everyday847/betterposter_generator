# betterposter_generator
Take a batch of figures and captions and feed them into the canonical 'betterposter' template.

The 'betterposter' LaTeX template is really wonderful if you want to write LaTeX to generate your poster, but that is usually not necessary! Most of the time all you actually need is to display figures, captions, and paragraphs in a sensible way. The details of how LaTeX layouts might accomplish this for you are just irritating! You just need a template structure and to trust that you'll get some kind of natural flow layout. Of course, you can always edit the LaTeX after, but you shouldn't need to do much.

So, how can we get to this point? Let's take a simple starting point: a poster is just a list of figure/caption pairs plus paragraphs of text. To compose a poster, you run the python script on an ordered list of files containing these components (just your argv). Permitting different files is a nice way to maintain some kind of modularity, but you can also combine all your content seed files into one, or into a few files (for example, if a figure/caption pair and a paragraph share a topic, and you might reuse those two components together, it's nice to have them in one file.

Figures are specified by a path. Captions and paragraphs are written out unless it can identify that the first item in the caption/paragraph is a file, in which case it imports the file contents.
