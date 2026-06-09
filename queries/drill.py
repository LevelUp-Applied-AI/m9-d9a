# queries/drill.py

def q1():
    """
    Q1 — Return all (book, title) pairs.
    Result: 5 rows. Variables: ?book ?title.
    """
    return """
PREFIX : <http://example.org/library/>

SELECT ?book ?title
WHERE {
    ?book a :Book ;
          :title ?title .
}
"""


def q2():
    """
    Q2 — Return all books and their year, filtered to books published after 2010.
    Result: 1 row. Variables: ?book ?year.
    """
    return """
PREFIX : <http://example.org/library/>

SELECT ?book ?year
WHERE {
    ?book a :Book ;
          :year ?year .
    FILTER (?year > 2010)
}
"""


def q3():
    """
    Q3 — Return all (book, author_name) pairs via rdfs:label.
    Result: 7 rows. Variables: ?book ?author_name.
    """
    return """
PREFIX : <http://example.org/library/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?book ?author_name
WHERE {
    ?book a :Book ;
          :author ?a .
    ?a rdfs:label ?author_name .
}
"""


def q4():
    """
    Q4 — Return all books and their topic, with topic OPTIONAL.
    Result: 5 rows (every book appears; ?topic unbound when missing).
    Variables: ?book ?topic.
    """
    return """
PREFIX : <http://example.org/library/>

SELECT ?book ?topic
WHERE {
    ?book a :Book .
    OPTIONAL { ?book :topic ?topic }
}
"""


def q5():
    """
    Q5 — ASK if any book has more than one :author triple.
    Result: TRUE.
    """
    return """
PREFIX : <http://example.org/library/>

ASK {
    ?book a :Book ;
          :author ?a1 ;
          :author ?a2 .
    FILTER (?a1 != ?a2)
}
"""