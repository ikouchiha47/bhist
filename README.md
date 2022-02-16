# bhist

Search through browser history

- Get history from browser profiles
    - plugglable module firefox, chrome
- Browse urls and index content
- Return result based on most matched followed by recency, limit results


### Requirments

- python3
- geckodriver binary
- pip
- selenium with firefox driver
- xapian for indexing

### Todo
- decouple the indexers from actual indexing
- xapian db path, make configurable
- enable search
- handle html parsing. (unexpected </ in html handle_endttag)
