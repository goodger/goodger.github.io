#!/usr/bin/env python

# Author: David Goodger
# Contact: goodger@python.org
# Revision: $Revision: 1754 $
# Date: $Date: 2008-05-07 11:13:55 -0400 (Wed, 07 May 2008) $
# Copyright: This module has been placed in the public domain.

"""
A minimal front end to the Docutils Publisher, producing HTML.
"""

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline, default_description


description = ('Generates (X)HTML documents from standalone reStructuredText '
               'sources.  ' + default_description)



# Inserted ----------------------------------------
import endnotes
from docutils.readers import standalone

class EndNotesReader(standalone.Reader):

    def get_transforms(self):
        return standalone.Reader.get_transforms(self) + \
            [endnotes.EndNotes]
# Inserted ----------------------------------------


publish_cmdline(reader=EndNotesReader(),
                writer_name='html', description=description)
