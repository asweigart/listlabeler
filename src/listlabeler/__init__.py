# List Labeler
# By Al Sweigart al@inventwithpython.com

import collections
Span = collections.namedtuple('Span', 'start end')

__version__ = '0.0.1'

class LabeledList:
    def __init__(self, listToLabel):
        assert isinstance(listToLabel, (list, tuple))
        self.labeledList = listToLabel


    def __str__(self):
        return str(self.labeledList)


    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, repr(self.labeledList))


    def __getitem__(self, i):
        # NOTE: We assume that the repr of labeledList begins and ends with a
        # single character (parentheses for tuples, square brackets for
        # lists). If a subclass of tuple or list does someting different,
        # LabeledList's indexes will be off.

        if type(i) == slice:
            raise NotImplementedError('slices are not implemented yet')

        self.labeledList[i] # Sets off any IndexError

        if i < 0:
            i = len(self.labeledList) + i # Convert negative index to postive.

        #                      01234567890123
        # self.labeledList == "['cat', 'dog']""
        listAsStrIndex = 1
        for lli in range(i):
            listAsStrIndex += len(repr(self.labeledList[lli]))
            listAsStrIndex += 2 # Add 2 for the ', '

        return Span(listAsStrIndex, listAsStrIndex + len(repr(self.labeledList[i])))


    def getHighlight(self, i, highlighter='V', highlightingFromTop=True):
        if type(i) != int:
            raise NotImplementedError('Only a single integer can be specified for i right now')

        span = self[i]

        highlightLine = (' ' * span.start) + (highlighter * (span.end - span.start))

        if highlightingFromTop:
            return highlightLine + '\n' + repr(self.labeledList)
        else:
            return repr(self.labeledList) + '\n' + highlightLine

    def highlight(self, i, highlighter='V', highlightingFromTop=True):
        print(self.getHighlight(i, highlighter, highlightingFromTop))
