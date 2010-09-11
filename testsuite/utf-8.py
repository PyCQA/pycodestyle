# -*- coding: utf-8 -*-


class Rectangle(Blob):

        def __init__(self, width, height,
                     color='black', emphasis=None, highlight=0):
            if width == 0 and height == 0 and \
               color == 'red' and emphasis == 'strong' or \
               highlight > 100:
                raise ValueError("sorry, you lose")
            if width == 0 and height == 0 and (color == 'red' or
                                               emphasis is None):
                raise ValueError("I don't think so -- values are %s, %s" %
                                 (width, height))
            Blob.__init__(self, width, height,
                          color, emphasis, highlight)


# Some random text with multi-byte characters (utf-8 encoded)
#
# Εδώ μάτσο κειμένων τη, τρόπο πιθανό διευθυντές ώρα μη. Νέων απλό παράγει ροή
# κι, το επί δεδομένη καθορίζουν. Πάντως ζητήσεις περιβάλλοντος ένα με, τη
# ξέχασε αρπάζεις φαινόμενο όλη. Τρέξει εσφαλμένη χρησιμοποίησέ νέα τι. Θα όρο
# πετάνε φακέλους, άρα με διακοπής λαμβάνουν εφαμοργής. Λες κι μειώσει
# καθυστερεί.
